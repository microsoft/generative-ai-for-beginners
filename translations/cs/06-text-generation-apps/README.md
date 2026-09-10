# Tvorba aplikací pro generování textu

[![Tvorba aplikací pro generování textu](../../../translated_images/cs/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

Zatím jste v tomto kurzu viděli, že existují základní koncepty jako promptování a dokonce celá disciplína zvaná „prompt engineering“. Mnoho nástrojů, se kterými můžete komunikovat, jako ChatGPT, Office 365, Microsoft Power Platform a další, podporuje použití promptů k dosažení určitého cíle.

Abychom mohli takovou zkušenost přidat do aplikace, je potřeba pochopit koncepty jako prompty, completions a zvolit knihovnu, se kterou budeme pracovat. To přesně se naučíte v této kapitole.

## Úvod

V této kapitole se naučíte:

- Seznámit se s knihovnou openai a jejími základními koncepty.
- Vytvořit aplikaci pro generování textu pomocí openai.
- Pochopit, jak používat koncepty jako prompt, temperature a tokens k tvorbě aplikace pro generování textu.

## Cíle učení

Na konci této lekce budete schopni:

- Vysvětlit, co je aplikace pro generování textu.
- Vytvořit aplikaci pro generování textu pomocí openai.
- Nastavit aplikaci tak, aby používala více či méně tokenů a také změnit teplotu pro rozmanitější výstup.

## Co je aplikace pro generování textu?

Obvykle když vytváříte aplikaci, má nějaké uživatelské rozhraní, například:

- Na příkazové bázi. Konzolové aplikace jsou typické aplikace, kde zadáváte příkaz a aplikace vykoná úkol. Například `git` je aplikace na příkazové bázi.
- Uživatelské rozhraní (UI). Některé aplikace mají grafické uživatelské rozhraní (GUI), kde klikáte na tlačítka, zadáváte text, vybíráte možnosti a další.

### Konzolové a UI aplikace mají omezení

Porovnejte to s aplikací na příkazové bázi, kde zadáváte příkaz:

- **Je omezená**. Nemůžete zadávat jakýkoliv příkaz, pouze ty, které aplikace podporuje.
- **Jazykově specifická**. Některé aplikace podporují mnoho jazyků, ale výchozí aplikace je vytvořená pro konkrétní jazyk, i když můžete přidat podporu dalších.

### Výhody aplikací pro generování textu

Jak se tedy aplikace pro generování textu liší?

V aplikaci pro generování textu máte větší flexibilitu, nejste omezeni na sadu příkazů ani konkrétní vstupní jazyk. Místo toho můžete použít přirozený jazyk k interakci s aplikací. Další výhodou je, že již komunikujete se zdrojem dat, který byl vytrénován na rozsáhlém korpusu informací, zatímco tradiční aplikace může být omezená tím, co je v databázi.

### Co mohu vytvořit pomocí aplikace pro generování textu?

Můžete vytvořit mnoho věcí, například:

- **Chatbota**. Chatbot odpovídající na otázky o tématech, jako je vaše firma a její produkty, může být dobrou volbou.
- **Pomocníka**. Velké jazykové modely (LLM) jsou skvělé na věci jako shrnutí textu, získání poznatků z textu, tvorbu textů jako životopisy a další.
- **Asistenta kódu**. V závislosti na použitém jazykovém modelu můžete vytvořit asistenta, který vám pomůže psát kód. Například můžete použít produkt jako GitHub Copilot i ChatGPT pro pomoc s psaním kódu.

## Jak začít?

Potřebujete najít způsob, jak se integrovat s LLM, což obvykle znamená tyto dvě možnosti:

- Použití API. V tomto případě vytváříte webové požadavky s vaším promptem a získáváte generovaný text zpět.
- Použití knihovny. Knihovny pomáhají zapouzdřit API volání a usnadňují jejich použití.

## Knihovny/SDK

Existuje několik známých knihoven pro práci s LLM, například:

- **openai**, tato knihovna zjednodušuje připojení k vašemu modelu a odesílání promptů.

Pak jsou zde knihovny operující na vyšší úrovni, jako například:

- **Langchain**. Langchain je známý a podporuje Python.
- **Semantic Kernel**. Semantic Kernel je knihovna od Microsoftu podporující jazyky C#, Python a Java.

## První aplikace s openai

Podívejme se, jak můžeme vytvořit naši první aplikaci, jaké knihovny potřebujeme, kolik je třeba a tak dále.

### Instalace openai

Existuje mnoho knihoven pro práci s OpenAI nebo Azure OpenAI. Je možné použít mnoho programovacích jazyků jako C#, Python, JavaScript, Java a další. Rozhodli jsme se použít knihovnu `openai` pro Python, takže ji nainstalujeme pomocí `pip`.

```bash
pip install openai
```

### Vytvoření zdroje

Musíte provést následující kroky:

- Vytvořit účet na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Získat přístup k Azure OpenAI. Přejděte na [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) a požádejte o přístup.

  > [!NOTE]
  > V době psaní je potřeba požádat o přístup do Azure OpenAI.

- Nainstalovat Python <https://www.python.org/>
- Vytvořit Azure OpenAI službu. Viz průvodce, jak [vytvořit zdroj](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Najděte API klíč a endpoint

Teď musíte knihovně `openai` říct, jaký API klíč má použít. Pro nalezení API klíče přejděte do sekce "Keys and Endpoint" ve vašem Azure OpenAI zdroji a zkopírujte hodnotu „Key 1“.

![Klíče a endpoint zdroje v Azure Portálu](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nyní když máte tuto informaci zkopírovanou, nastavme knihovny, aby ji používaly.

> [!NOTE]
> Stojí za to oddělit váš API klíč od kódu. Můžete to udělat pomocí proměnných prostředí.
>
> - Nastavte proměnnou prostředí `OPENAI_API_KEY` na váš API klíč.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavení konfigurace pro Azure

Pokud používáte Azure OpenAI (nyní součást Microsoft Foundry), zde je nastavení konfigurace. Používáme standardního klienta `OpenAI` směřujícího na endpoint Azure OpenAI `/openai/v1/`, který pracuje s Responses API a nevyžaduje `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Výše nastavujeme následující:

- `api_key`, což je váš API klíč nalezený v Azure Portal nebo portálu Microsoft Foundry.
- `base_url`, což je endpoint vašeho Foundry zdroje s připojeným `/openai/v1/`. Stabilní v1 endpoint funguje napříč OpenAI a Azure OpenAI bez správy `api_version`.

> [!NOTE] > `os.environ` čte proměnné prostředí. Můžete ji použít k načtení proměnných prostředí jako `AZURE_OPENAI_API_KEY` a `AZURE_OPENAI_ENDPOINT`. Nastavte tyto proměnné prostředí v terminálu nebo pomocí knihovny jako `dotenv`.

## Generování textu

Způsob generování textu je použití Responses API přes metodu `responses.create`. Zde je příklad:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # toto je název nasazení vašeho modelu
    input=prompt,
    store=False,
)
print(response.output_text)
```

Ve výše uvedeném kódu vytvoříme odpověď, zadáme model, který chceme použít, a prompt. Pak vypíšeme generovaný text přes `response.output_text`.

### Vícekolové konverzace

Responses API je vhodné pro generování textu jednorázově i pro vícekolové chatboty - poskytnete seznam zpráv v `input` pro vytvoření konverzace:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Více o této funkčnosti v následující kapitole.

## Cvičení - vaše první aplikace pro generování textu

Teď, když jsme se naučili, jak nastavit a konfigurovat openai, je čas vytvořit vaši první aplikaci pro generování textu. Postupujte podle těchto kroků:

1. Vytvořte virtuální prostředí a nainstalujte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Pokud používáte Windows, zadejte `venv\Scripts\activate` místo `source venv/bin/activate`.

   > [!NOTE]
   > Najděte svůj Azure OpenAI klíč na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), vyhledejte `Open AI`, vyberte `Open AI resource` a poté `Keys and Endpoint` a zkopírujte hodnotu `Key 1`.

1. Vytvořte soubor _app.py_ a vložte do něj následující kód:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # přidejte svůj dokončovací kód
   prompt = "Complete the following: Once upon a time there was a"

   # proveďte požadavek pomocí Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # vytiskněte odpověď
   print(response.output_text)
   ```

   > [!NOTE]
   > Pokud používáte čisté OpenAI (ne Azure), použijte `client = OpenAI(api_key="<nahraďte tuto hodnotu vaším OpenAI klíčem>")` (bez `base_url`) a jako model zadejte název modelu například `gpt-5-mini` místo názvu nasazení.

   Měli byste vidět výstup podobný následujícímu:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Různé typy promptů pro různé účely

Nyní jste viděli, jak generovat text pomocí promptu. Dokonce máte spuštěný program, který můžete upravovat a měnit tak, aby generoval různé typy textu.

Prompty lze použít pro různé úkoly. Například:

- **Generování určitého typu textu**. Například generovat báseň, otázky do kvízu atd.
- **Vyhledávání informací**. Můžete použít prompty k vyhledání informací, například „Co znamená CORS ve webovém vývoji?“.
- **Generování kódu**. Můžete použít prompty k generování kódu, například vytvoření regulárního výrazu pro validaci emailů nebo třeba generování celé aplikace jako webové aplikace.

## Praktický případ: generátor receptů

Představte si, že máte doma ingredience a chcete něco uvařit. K tomu potřebujete recept. Jeden způsob, jak najít recepty, je použít vyhledávač nebo můžete použít LLM.

Můžete napsat prompt třeba takto:

> „Ukáž mi 5 receptů na jídlo s následujícími ingrediencemi: kuře, brambory a mrkev. U každého receptu vyjmenuj všechny použité ingredience.“

Na základě výše uvedeného promptu můžete získat odpověď podobnou:

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

Tento výsledek je skvělý, vím, co uvařit. V tuto chvíli by mohly být užitečné následující vylepšení:

- Odfiltrování ingrediencí, které nemám rád nebo jsem na ně alergický.
- Vytvoření nákupního seznamu, pokud doma nemám všechny ingredience.

Pro výše uvedené případy přidáme další prompt:

> „Prosím odstraň recepty s česnekem, protože jsem na něj alergický, a nahraď je něčím jiným. Také prosím vytvoř nákupní seznam pro recepty, vezmeme-li v úvahu, že doma už mám kuře, brambory a mrkev.“

Nyní máte nový výsledek, konkrétně:

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

To jsou vaše pět receptů bez česneku a také nákupní seznam s ohledem na to, co už máte doma.

## Cvičení - vytvořte generátor receptů

Nyní když jsme provedli scénář, napišme kód odpovídající demonstrovanému scénáři. Postupujte podle těchto kroků:

1. Použijte stávající soubor _app.py_ jako výchozí bod
1. Najděte proměnnou `prompt` a změňte její kód na následující:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Pokud nyní kód spustíte, měli byste vidět výstup podobný:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > POZNÁMKA: váš LLM je nedeterministický, takže můžete dostat pokaždé jiný výsledek.

   Skvělé, podívejme se, jak to můžeme zlepšit. Chceme, aby byl kód flexibilní, takže ingredience i počet receptů by měly být snadno měnitelné.

1. Změňme kód následovně:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolovat počet receptů do promptu a ingrediencí
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testovací spuštění kódu může vypadat takto:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Vylepšení přidáním filtru a nákupního seznamu

Nyní máme funkční aplikaci na generování receptů a je flexibilní, protože spoléhá na vstupy od uživatele, jak v počtu receptů, tak v použitých ingrediencích.

Pro další zlepšení chceme přidat následující:

- **Filtrovat ingredience**. Chceme mít možnost vyřadit ingredience, které nemáme rádi nebo na které jsme alergičtí. Pro tuto změnu můžeme upravit náš existující prompt a přidat podmínku filtru na konec takto:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Výše přidáváme `{filter}` na konec promptu a také zachytáváme hodnotu filtru od uživatele.

  Příklad vstupu při spuštění programu může vypadat takto:

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

  Jak vidíte, všechny recepty obsahující mléko byly odfiltrovány. Ale pokud jste laktózově intolerantní, mohli byste chtít také vyfiltrovat recepty se sýrem, takže je potřeba být jasný.


- **Vytvořte nákupní seznam**. Chceme vytvořit nákupní seznam s ohledem na to, co už máme doma.

  Pro tuto funkci bychom mohli buď zkusit vyřešit vše v jednom promptu, nebo to rozdělit do dvou promptů. Zkusme ten druhý přístup. Zde navrhujeme přidat další prompt, ale aby to fungovalo, musíme výsledek prvního promptu přidat jako kontext do druhého promptu.

  Najděte část v kódu, která vypisuje výsledek z prvního promptu, a přidejte níže následující kód:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # vytisknout odpověď
  print("Shopping list:")
  print(response.output_text)
  ```

  Všimněte si následujícího:

  1. Vytváříme nový prompt tak, že přidáme výsledek z prvního promptu do nového promptu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Vytvoříme nový požadavek, ale zároveň zohledňujeme počet tokenů, o které jsme žádali v prvním promptu, takže tentokrát nastavujeme `max_output_tokens` na 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Po spuštění tohoto kódu dostaneme následující výstup:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Vylepšete své nastavení

Co zatím máme, je funkční kód, ale existují některé úpravy, které by měly věci dále zlepšit. Některé věci, které bychom měli udělat, jsou:

- **Oddělte tajné klíče od kódu**, například API klíč. Tajné údaje nepatří do kódu a měly by být uloženy na bezpečném místě. Pro oddělení tajných klíčů od kódu můžeme použít proměnné prostředí a knihovny jako `python-dotenv`, které je načítají ze souboru. Takto by to v kódu vypadalo:

  1. Vytvořte soubor `.env` s následujícím obsahem:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Poznámka, pro Azure OpenAI v Microsoft Foundry je místo toho potřeba nastavit následující proměnné prostředí:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     V kódu byste načítali proměnné prostředí takto:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Slovo o délce tokenů**. Měli bychom zvážit, kolik tokenů potřebujeme k vygenerování požadovaného textu. Tokeny něco stojí, takže tam, kde je to možné, bychom měli snažit se být ekonomičtí s jejich počtem. Můžeme například formulovat prompt tak, abychom mohli použít méně tokenů?

  Pro změnu počtu použitých tokenů můžete použít parametr `max_output_tokens`. Například pokud chcete použít 100 tokenů, uděláte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentování s teplotou**. Teplota je něco, o čem jsme zatím nemluvili, ale je to důležitý kontext pro výkon našeho programu. Čím vyšší hodnota teploty, tím náhodnější bude výstup. Naopak čím nižší hodnota teploty, tím předvídatelnější výstup bude. Zvažte, zda chcete mít ve výstupu variace, nebo ne.

  Pro změnu teploty můžete použít parametr `temperature`. Například pokud chcete použít teplotu 0,5, uděláte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Poznámka, čím blíže je hodnota k 1,0, tím je výstup různorodější.

- **Modely pro odvozování nepoužívají `temperature`**. Toto je důležitá změna pro rok 2026. Aktuální, nepřestárlé modely v Microsoft Foundry jsou **modely pro odvozování** (rodina GPT-5, o-series) - a ty **nepodporují `temperature` ani `top_p`** (ani `max_tokens`; místo toho používejte `max_output_tokens`). Pokud pošlete `temperature` do `gpt-5-mini`, dostanete chybu "parameter not supported". Pro vyzkoušení příkladu s teplotou výše použijte model, který ještě podporuje řízení vzorkování - například otevřený model **Llama** jako `Llama-3.3-70B-Instruct` z [Microsoft Foundry katalogu modelů](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), volaný pomocí Foundry Models / Azure AI Inference endpointu (stejným způsobem jako vzorky `githubmodels-*`). U modelů pro odvozování jako GPT-5 se výstup řídí jinak:
  - **Inženýrství promptů** - jasné instrukce, příklady a strukturovaný výstup (viz lekce [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) zastanou práci, kterou dříve dělala nastavení vzorkování.
  - **Řízení odvozování** - parametry jako snaha o odvozování/verbosity vyvažují hloubku odvozování vůči latenci a nákladům.

  Stručně: `temperature`/`top_p` jsou stále platné u mnoha modelů (Llama, Mistral, Phi a rodina GPT-4.x - ačkoli GPT-4.x je ve fázi vyřazování), ale směřování je inženýrství promptů + řízení odvozování u modelů pro odvozování jako GPT-5.

## Zadání

Pro toto zadání si můžete vybrat, co postavíte.

Zde jsou některé návrhy:

- Vylepšete aplikaci generátoru receptů, zkuste si hrát s hodnotami teploty a prompty, abyste zjistili, co můžete vytvořit.
- Vytvořte „studijního kamaráda“. Tato aplikace by měla být schopná odpovídat na otázky k určitému tématu, například Python, můžete mít prompty jako „Co je určitý pojem v Pythonu?“ nebo prompt, který říká, ukaž mi kód pro určitý pojem atd.
- Historický bot, oživte historii, nařiďte botovi, aby hrál určitou historickou osobu a ptejte se ho na otázky o jeho životě a době.

## Řešení

### Studijní kamarád

Níže je počáteční prompt, podívejte se, jak ho můžete použít a upravit podle svých představ.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historický bot

Zde jsou některé prompty, které byste mohli používat:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Kontrola znalostí

Co dělá koncept teploty?

1. Řídí, jak náhodný je výstup.
1. Řídí, jak velká je odpověď.
1. Řídí, kolik tokenů se použije.

## 🚀 Výzva

Při práci na zadání zkuste měnit teplotu, nastavte ji na 0, 0,5 a 1. Pamatujte, že 0 znamená nejmenší variabilitu a 1 největší. Jaká hodnota funguje nejlépe pro vaši aplikaci?

## Skvělá práce! Pokračujte ve vzdělávání

Po dokončení této lekce si prohlédněte naši [kolekci vzdělávání o Generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde můžete dál vylepšovat své znalosti Generativní AI!

Přejděte do Lekce 7, kde se podíváme, jak [stavět chatovací aplikace](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->