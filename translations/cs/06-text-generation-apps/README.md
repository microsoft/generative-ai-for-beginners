# Vytváření aplikací pro generování textu

[![Vytváření aplikací pro generování textu](../../../translated_images/cs/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klikněte na obrázek výše pro přehrání videa této lekce)_

Dosud jste v tomto kurzu viděli, že existují základní koncepty jako prompty a dokonce celá disciplína nazvaná „prompt engineering“. Mnoho nástrojů, se kterými můžete interagovat, jako ChatGPT, Office 365, Microsoft Power Platform a další, vás podporuje v používání promptů k dosažení nějakého cíle.

Abychom takovou zkušenost přidali do aplikace, musíte rozumět konceptům jako prompty, dokončení a vybrat si knihovnu, se kterou budete pracovat. To je přesně to, co se naučíte v této kapitole.

## Úvod

V této kapitole se naučíte:

- Seznámit se s knihovnou openai a jejími základními koncepty.
- Vytvořit aplikaci pro generování textu pomocí openai.
- Pochopit, jak používat koncepty jako prompt, teplota (temperature) a tokeny k vytvoření aplikace pro generování textu.

## Výukové cíle

Na konci této lekce budete schopni:

- Vysvětlit, co je to aplikace pro generování textu.
- Vytvořit aplikaci pro generování textu pomocí openai.
- Nakonfigurovat aplikaci tak, aby používala více či méně tokenů a také změnit teplotu pro různorodý výstup.

## Co je to aplikace pro generování textu?

Obvykle, když vytváříte aplikaci, má nějaké rozhraní, například toto:

- Řádkové rozhraní (příkazové). Konzolové aplikace jsou typické aplikace, kde napíšete příkaz a ten provede nějaký úkol. Například `git` je aplikace s příkazovým řádkem.
- Uživatelské rozhraní (UI). Některé aplikace mají grafické uživatelské rozhraní (GUI), kde klikáte na tlačítka, zadáváte text, vybíráte možnosti a další.

### Konzolové a UI aplikace mají omezení

Porovnejte to s aplikací založenou na příkazech, kde zadáte příkaz:

- **Je omezená**. Nemůžete zadat jakýkoliv příkaz, pouze ty, které aplikace podporuje.
- **Jazykově specifická**. Některé aplikace podporují mnoho jazyků, ale ve výchozím nastavení jsou vytvořeny pro konkrétní jazyk, i když je možné přidat další jazykovou podporu.

### Výhody aplikací pro generování textu

Takže v čem se aplikace pro generování textu liší?

V aplikaci pro generování textu máte větší flexibilitu, nejste omezeni na sadu příkazů nebo konkrétní vstupní jazyk. Místo toho můžete používat přirozený jazyk pro interakci s aplikací. Další výhodou je, že už pracujete se zdrojem dat, který byl vytrénován na rozsáhlém korpusu informací, zatímco tradiční aplikace může být omezená na obsah databáze.

### Co mohu s aplikací pro generování textu vytvořit?

Můžete vytvořit mnoho věcí. Například:

- **Chatbota**. Chatbot, který odpovídá na otázky o tématech, jako je vaše společnost a její produkty, může být dobrý příklad.
- **Pomocníka**. LLM jsou skvělé na věci jako shrnutí textu, získávání přehledů z textu, tvorba textů jako životopisů a další.
- **Asistenta pro kódování**. Podle použitého jazykového modelu lze vytvořit asistenta, který pomáhá psát kód. Například můžete využít produkt jako GitHub Copilot nebo ChatGPT ke pomoč při psaní kódu.

## Jak začít?

Potřebujete najít způsob, jak integrovat LLM, což obvykle znamená tyto dva přístupy:

- Použít API. Zde tvoříte webové požadavky s vaším promptem a dostáváte generovaný text zpět.
- Použít knihovnu. Knihovny pomáhají zapouzdřit volání API a usnadnit jejich použití.

## Knihovny/SDK

Existuje několik dobře známých knihoven pro práci s LLM, například:

- **openai**, tato knihovna usnadňuje připojení k modelu a odesílání promptů.

Pak jsou knihovny, které operují na vyšší úrovni, například:

- **Langchain**. Langchain je dobře známý a podporuje Python.
- **Semantic Kernel**. Semantic Kernel je knihovna od Microsoftu, která podporuje jazyky C#, Python a Java.

## První aplikace pomocí openai

Podívejme se, jak můžeme vytvořit naši první aplikaci, jaké knihovny potřebujeme, kolik je třeba a tak dále.

### Instalace openai

Existuje mnoho knihoven pro interakci s OpenAI nebo Azure OpenAI. Je možné použít různé programovací jazyky jako C#, Python, JavaScript, Java a další. My jsme zvolili knihovnu `openai` v Pythonu, proto použijeme `pip` k její instalaci.

```bash
pip install openai
```

### Vytvoření zdroje

Musíte provést následující kroky:

- Vytvořit účet na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Získat přístup k Azure OpenAI. Jděte na [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) a požádejte o přístup.

  > [!NOTE]
  > V době psaní této lekce je třeba žádat o přístup k Azure OpenAI.

- Nainstalovat Python <https://www.python.org/>
- Vytvořit zdroj Azure OpenAI Service. Podívejte se na tento návod, jak [vytvořit zdroj](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Najít klíč API a endpoint

Teď musíte knihovně `openai` říct, jaký klíč API použít. Aby jste našli svůj klíč API, přejděte do sekce "Keys and Endpoint" svého zdroje Azure OpenAI a zkopírujte hodnotu „Key 1“.

![Klíče a Endpoint v Azure Portálu](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Když máte tyto informace zkopírované, ukažme knihovnám, aby je používaly.

> [!NOTE]
> Stojí za to oddělit klíč API od vašeho kódu. Můžete to udělat pomocí proměnných prostředí.
>
> - Nastavte proměnnou prostředí `OPENAI_API_KEY` na svůj klíč API.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavení konfigurace Azure

Pokud používáte Azure OpenAI (nyní součást Microsoft Foundry), zde je postup, jak nastavit konfiguraci. Používáme standardního klienta `OpenAI` nasměrovaného na Azure OpenAI endpoint `/openai/v1/`, který pracuje s Responses API a není potřeba `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Výše nastavujeme následující:

- `api_key`, což je váš klíč API nalezený v Azure Portálu nebo Microsoft Foundry portálu.
- `base_url`, což je endpoint vašeho zdroje Foundry s připojeným `/openai/v1/`. Stabilní v1 endpoint funguje pro OpenAI i Azure OpenAI bez správy `api_version`.

> [!NOTE] > `os.environ` čte proměnné prostředí. Můžete ji použít k načtení proměnných jako `AZURE_OPENAI_API_KEY` a `AZURE_OPENAI_ENDPOINT`. Nastavte tyto proměnné ve vašem terminálu nebo pomocí knihovny jako `dotenv`.

## Generování textu

Text generujete pomocí Responses API přes metodu `responses.create`. Zde je příklad:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # toto je název nasazení vašeho modelu
    input=prompt,
    store=False,
)
print(response.output_text)
```

V uvedeném kódu vytvoříme odpověď, předáme model, který chceme použít, a prompt. Poté vytiskneme generovaný text přes `response.output_text`.

### Vícekolové konverzace

Responses API je vhodné jak pro jednorázové generování textu, tak pro vícekolové chatboty – poskytujete seznam zpráv v `input`, aby se vytvořila konverzace:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Více o této funkci v nadcházející kapitole.

## Cvičení - vaše první aplikace pro generování textu

Nyní, když jsme se naučili nastavit a konfigurovat openai, je čas vytvořit vaši první aplikaci pro generování textu. Postupujte podle těchto kroků:

1. Vytvořte virtuální prostředí a nainstalujte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Pokud používáte Windows, napište `venv\Scripts\activate` místo `source venv/bin/activate`.

   > [!NOTE]
   > Najděte svůj klíč Azure OpenAI návštěvou [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), vyhledejte `Open AI`, vyberte `Open AI resource` a poté zvolte `Keys and Endpoint`, kde zkopírujete hodnotu `Key 1`.

1. Vytvořte soubor _app.py_ a vložte do něj tento kód:

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

   # proveďte požadavek pomocí API Responses
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # vytiskněte odpověď
   print(response.output_text)
   ```

   > [!NOTE]
   > Pokud používáte čisté OpenAI (nikoli Azure), použijte `client = OpenAI(api_key="<nahraďte tuto hodnotu vaším OpenAI klíčem>")` (bez `base_url`) a předávejte jméno modelu jako `gpt-4o-mini` místo jména nasazení.

   Měli byste vidět výstup zhruba jako tento:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Různé typy promptů pro různé účely

Nyní jste viděli, jak generovat text pomocí promptu. Máte dokonce spuštěný program, který můžete upravovat a měnit k generování různých typů textu.

Prompt lze použít pro různé úlohy, například:

- **Generovat typ textu**. Například můžete generovat báseň, otázky pro kvíz atd.
- **Vyhledávat informace**. Prompt lze použít k hledání informací, například „Co znamená CORS ve webovém vývoji?“.
- **Generovat kód**. Prompt lze použít k vytvoření kódu, například vytvoření regulárního výrazu pro validaci e-mailů nebo dokonce generování celé aplikace, jako je webová aplikace.

## Praktický případ: generátor receptů

Představte si, že máte doma suroviny a chcete něco uvařit. K tomu potřebujete recept. Recepty můžete najít vyhledávačem nebo použít LLM.

Můžete napsat prompt takto:

> „Ukáž mi 5 receptů na pokrm s následujícími surovinami: kuře, brambory a mrkev. U každého receptu vypiš všechny použité suroviny.“

Podle výše uvedeného promptu můžete získat odpověď podobnou této:

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

Tento výsledek je skvělý, vím, co uvařit. Nyní by bylo užitečné zlepšení jako:

- Filtrování surovin, které nemám rád nebo na které jsem alergický.
- Vytvoření nákupního seznamu, pokud doma nemám všechny suroviny.

Pro výše uvedené případy přidáme další prompt:

> „Odstraň prosím recepty s česnekem, protože jsem na něj alergický, a nahraď je něčím jiným. Také prosím vytvoř nákupní seznam pro tyto recepty, přičemž zohledni, že doma už mám kuře, brambory a mrkev.“

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

To jsou vaše pět receptů bez česneku a také máte nákupní seznam s ohledem na suroviny, které už doma máte.

## Cvičení - vytvořte generátor receptů

Nyní, když jsme rozehráli scénář, napišme kód, který odpovídá ukázanému scénáři. Postupujte takto:

1. Použijte existující soubor _app.py_ jako výchozí bod.
1. Najděte proměnnou `prompt` a změňte její kód na následující:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Pokud kód nyní spustíte, měli byste vidět výstup podobný tomuto:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > POZNÁMKA, vaše LLM není deterministické, takže při každém spuštění programu můžete získat odlišné výsledky.

   Skvělé, nyní uvidíme, jak věci zlepšit. Chceme, aby byl kód flexibilní, aby bylo možné měnit suroviny i počet receptů.

1. Změňme kód tímto způsobem:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # vložte počet receptů do výzvy a ingrediencí
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Ukázka testovacího spuštění kódu může vypadat takto:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Vylepšení přidáním filtru a nákupního seznamu

Nyní máme funkční aplikaci, která umí vygenerovat recepty, a je flexibilní, protože se spoléhá na vstupy uživatele, jak počet receptů, tak suroviny.

Pro další vylepšení chceme přidat toto:

- **Filtrovat suroviny**. Chceme mít možnost filtrovat suroviny, které nemáme rádi nebo na které jsme alergičtí. Abychom toho dosáhli, můžeme upravit náš existující prompt a přidat na konec podmínku filtru takto:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Výše přidáváme `{filter}` na konec promptu a také zachytáváme hodnotu filtru od uživatele.

  Příklad vstupu při spuštění programu nyní může vypadat takto:

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

  Jak vidíte, všechny recepty obsahující mléko byly vyfiltrovány. Pokud jste například laktózově intolerantní, můžete chtít vyfiltrovat i recepty sýrů, proto je důležité být specifický.


- **Vytvořte nákupní seznam**. Chceme vytvořit nákupní seznam s ohledem na to, co již doma máme.

  Pro tuto funkci bychom mohli vše vyřešit v jednom promptu, nebo to rozdělit do dvou promptů. Zkusme druhý přístup. Zde navrhujeme přidat další prompt, ale aby to fungovalo, musíme přidat výsledek prvního promptu jako kontext k druhému promptu.

  Najděte část kódu, která vypisuje výsledek z prvního promptu, a přidejte níže následující kód:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # vytiskni odpověď
  print("Shopping list:")
  print(response.output_text)
  ```

  Vezměte na vědomí následující:

  1. Konstruujeme nový prompt přidáním výsledku z prvního promptu do nového promptu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Provádíme nový požadavek, ale také s ohledem na počet tokenů, o které jsme žádali v prvním promptu, takže tentokrát nastavíme `max_output_tokens` na 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Když tento kód vyzkoušíme, dostaneme následující výstup:

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

To, co máme zatím, je kód, který funguje, ale existují některé úpravy, které by ho měly dále zlepšit. Některé věci, které bychom měli udělat, jsou:

- **Oddělte tajné údaje od kódu**, například API klíč. Tajné údaje nepatří přímo do kódu a měly by být uložené na bezpečném místě. K oddělení tajných údajů od kódu můžeme využít prostředí proměnné a knihovny jako `python-dotenv`, která je načte ze souboru. Zde je, jak by to v kódu vypadalo:

  1. Vytvořte `.env` soubor s následujícím obsahem:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Poznámka, pro Azure OpenAI v Microsoft Foundry musíte nastavit následující proměnné prostředí:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     V kódu byste pak načetli proměnné prostředí takto:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Slovo k délce tokenů**. Měli bychom zvážit, kolik tokenů potřebujeme k vygenerování požadovaného textu. Tokeny něco stojí, takže pokud možno, měli bychom být ekonomičtí v počtu použitých tokenů. Například, lze prompt formulovat tak, abychom použili méně tokenů?

  Pro změnu počtu tokenů můžete použít parametr `max_output_tokens`. Například, pokud chcete použít 100 tokenů, uděláte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentování s teplotou**. Teplota je něco, o čem jsme zatím nemluvili, ale je důležitý kontext pro to, jak náš program funguje. Čím vyšší je hodnota teploty, tím náhodnější je výstup. Naopak čím nižší hodnota teploty, tím předvídatelnější výstup je. Uvažujte, zda chcete vyladit variabilitu výstupu, nebo ne.

  Pro změnu teploty můžete použít parametr `temperature`. Například, pokud chcete nastavit teplotu na 0,5, uděláte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Poznámka, čím blíže k 1.0, tím rozmanitější výstup.

## Zadání

Pro toto zadání si můžete vybrat, co chcete vytvořit.

Zde jsou některé návrhy:

- Vylepšete aplikaci pro generování receptů. Vyzkoušejte si různé hodnoty teploty a prompty, abyste viděli, co dokážete vytvořit.
- Vytvořte "studijního parťáka". Tato aplikace by měla být schopná odpovídat na otázky o nějakém tématu, například Python, můžete mít prompty jako "Co je určité téma v Pythonu?", nebo prompt, který říká, ukaž mi kód pro určité téma atd.
- Historický bot, oživte historii, zadejte botovi hraní určité historické postavy a ptejte se ho na jeho život a dobu.

## Řešení

### Studijní parťák

Níže je výchozí prompt, podívejte se, jak ho můžete použít a upravit podle svého.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historický bot

Zde jsou některé prompty, které byste mohli použít:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Kontrola znalostí

Co dělá koncept teploty?

1. Řídí, jak náhodný je výstup.
1. Řídí, jak velká je odpověď.
1. Řídí, kolik tokenů je použito.

## 🚀 Výzva

Při práci na zadání vyzkoušejte měnit teplotu, nastavte ji na 0, 0,5 a 1. Pamatujte, že 0 je nejméně proměnlivá a 1 nejvíc. Která hodnota vyhovuje vaší aplikaci nejlépe?

## Skvělá práce! Pokračujte ve vzdělávání

Po dokončení této lekce se podívejte na naši [kolekci nauky o generativním AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kde můžete dále rozšiřovat své znalosti o generativním AI!

Přejděte na lekci 7, kde se podíváme na to, jak [vytvářet chatové aplikace](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->