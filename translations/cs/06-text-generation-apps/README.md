# Tvorba aplikací pro generování textu

[![Tvorba aplikací pro generování textu](../../../translated_images/cs/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

Dosud jste v tomto kurikulu viděli, že existují základní pojmy, jako jsou prompty, a dokonce celá disciplína zvaná "prompt engineering". Mnoho nástrojů, se kterými můžete interagovat, jako ChatGPT, Office 365, Microsoft Power Platform a další, vás podporuje v použití promptů k dosažení určitého výsledku.

Abychom do aplikace přidali takovou zkušenost, musíte pochopit pojmy jako prompty, dokončení a vybrat knihovnu, se kterou budete pracovat. To je přesně to, co se v této kapitole naučíte.

## Úvod

V této kapitole:

- Naučíte se o knihovně openai a jejích základních pojmech.
- Vytvoříte aplikaci pro generování textu s využitím openai.
- Pochopíte, jak používat pojmy jako prompt, teplota a tokeny k vytvoření aplikace pro generování textu.

## Cíle učení

Na konci této lekce budete schopni:

- Vysvětlit, co je aplikace pro generování textu.
- Vytvořit aplikaci pro generování textu pomocí openai.
- Konfigurovat vaši aplikaci tak, aby používala více či méně tokenů a také změnit teplotu pro různorodý výstup.

## Co je aplikace pro generování textu?

Obvykle, když vytváříte aplikaci, má nějaké uživatelské rozhraní jako následující:

- Na příkazové bázi. Konzolové aplikace jsou typické aplikace, kde napíšete příkaz a ten vykoná úkol. Například `git` je aplikace na příkazové bázi.
- Uživatelské rozhraní (UI). Některé aplikace mají grafické uživatelské rozhraní (GUI), kde klikáte na tlačítka, zadáváte text, vybíráte možnosti a další.

### Konzolové a UI aplikace jsou omezené

Porovnejte to s aplikací na příkazové bázi, kde zadáváte příkaz:

- **Je omezená**. Nemůžete jen tak zadat libovolný příkaz, pouze ty, které aplikace podporuje.
- **Specifická pro jazyk**. Některé aplikace podporují mnoho jazyků, ale aplikace je ve výchozím nastavení vytvořena pro konkrétní jazyk, i když můžete přidat podporu dalších jazyků.

### Výhody aplikací pro generování textu

Jak se tedy liší aplikace pro generování textu?

V aplikaci pro generování textu máte větší flexibilitu, nejste omezeni na sadu příkazů nebo konkrétní vstupní jazyk. Místo toho můžete používat přirozený jazyk pro interakci s aplikací. Další výhodou je, že již komunikujete se zdrojem dat, který byl vytrénován na rozsáhlém korpusu informací, zatímco tradiční aplikace může být omezená na data v databázi.

### Co mohu vytvořit s aplikací pro generování textu?

Existuje mnoho věcí, které můžete vytvořit. Například:

- **Chatbot**. Chatbot odpovídající na otázky o tématech, jako je vaše firma a její produkty, by mohl být vhodný.
- **Pomocník**. LLM jsou skvělé při sumarizaci textu, získávání poznatků z textu, tvorbě textů jako životopisy a další.
- **Asistent pro kód**. Podle použitého jazykového modelu můžete vytvořit asistenta pro psaní kódu. Například můžete použít produkt jako GitHub Copilot či ChatGPT pro pomoc s psaním kódu.

## Jak mohu začít?

Potřebujete najít způsob, jak integrovat LLM, což obvykle zahrnuje následující dvě metody:

- Použít API. Zde sestavujete webové požadavky s vaším promptem a dostáváte zpět generovaný text.
- Použít knihovnu. Knihovny pomáhají zapouzdřit volání API a usnadňují jejich použití.

## Knihovny/SDK

Existuje několik známých knihoven pro práci s LLM, jako jsou:

- **openai**, tato knihovna usnadňuje připojení k vašemu modelu a odesílání promptů.

Dále jsou tu knihovny, které operují na vyšší úrovni, například:

- **Langchain**. Langchain je dobře známý a podporuje Python.
- **Semantic Kernel**. Semantic Kernel je knihovna od Microsoftu podporující jazyky C#, Python a Java.

## První aplikace s openai

Podívejme se, jak můžeme vytvořit naši první aplikaci, jaké knihovny potřebujeme, kolik je toho zapotřebí, a tak dále.

### Instalace openai

Existuje mnoho knihoven pro interakci s OpenAI nebo Azure OpenAI. Je možné použít různé programovací jazyky jako C#, Python, JavaScript, Java a další. Zvolili jsme knihovnu `openai` pro Python, takže ji nainstalujeme pomocí `pip`.

```bash
pip install openai
```

### Vytvoření zdroje

Musíte provést následující kroky:

- Vytvořit účet na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)].
- Získat přístup k Azure OpenAI. Jděte na [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) a požádejte o přístup.

  > [!NOTE]
  > V době psaní je potřeba požádat o přístup k Azure OpenAI.

- Nainstalovat Python <https://www.python.org/>
- Vytvořit zdroj služby Azure OpenAI. Podívejte se na tento návod, jak [vytvořit zdroj](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Najít klíč API a koncový bod

V tuto chvíli musíte své knihovně `openai` sdělit, který klíč API použít. Chcete-li najít svůj klíč API, přejděte do sekce „Klíče a koncový bod“ vašeho Azure OpenAI zdroje a zkopírujte hodnotu „Klíč 1“.

![Klíče a koncový bod v Azure Portalu](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nyní, když máte tyto informace zkopírované, nastavme knihovnám, aby je používaly.

> [!NOTE]
> Je vhodné oddělit klíč API od vašeho kódu. Lze to provést pomocí proměnných prostředí.
>
> - Nastavte proměnnou prostředí `OPENAI_API_KEY` na svůj klíč API.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavení konfigurace Azure

Pokud používáte Azure OpenAI (nyní součást Microsoft Foundry), takto nastavíte konfiguraci. Používáme standardního klienta `OpenAI` směřujícího na koncový bod Azure OpenAI `/openai/v1/`, který pracuje s Responses API a nevyžaduje žádné `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Výše nastavujeme:

- `api_key`, což je váš klíč API nalezený v Azure Portalu nebo Microsoft Foundry portálu.
- `base_url`, což je váš Foundry resource endpoint s připojeným `/openai/v1/`. Stabilní v1 endpoint funguje napříč OpenAI a Azure OpenAI bez správy `api_version`.

> [!NOTE] > `os.environ` čte proměnné prostředí. Můžete ji použít pro čtení proměnných prostředí jako jsou `AZURE_OPENAI_API_KEY` a `AZURE_OPENAI_ENDPOINT`. Nastavte tyto proměnné prostředí ve vašem terminálu nebo pomocí knihovny jako je `dotenv`.

## Generování textu

Text generujete pomocí Responses API přes metodu `responses.create`. Zde je příklad:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Ve výše uvedeném kódu vytváříme odpověď a předáváme model, který chceme použít, a prompt. Poté vytiskneme generovaný text přes `response.output_text`.

### Vícekolové konverzace

Responses API je vhodné jak pro generování textu v jednom kole, tak pro vícekolové chatboty - poskytujete seznam zpráv ve `input` k vytvoření konverzace:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

O této funkci více v následující kapitole.

## Cvičení - vaše první aplikace pro generování textu

Teď, když jsme si ukázali, jak nastavit a konfigurovat openai, je čas vytvořit vaši první aplikaci pro generování textu. Postupujte podle těchto kroků:

1. Vytvořte virtuální prostředí a nainstalujte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Pokud používáte Windows, napište `venv\Scripts\activate` místo `source venv/bin/activate`.

   > [!NOTE]
   > Najděte si svůj Azure OpenAI klíč na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), vyhledejte `Open AI`, vyberte `Open AI resource`, poté klikněte na `Keys and Endpoint` a zkopírujte hodnotu `Key 1`.

2. Vytvořte soubor _app.py_ a vložte do něj následující kód:

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
   > Pokud používáte čisté OpenAI (ne Azure), použijte `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (bez `base_url`) a předávejte název modelu jako `gpt-5-mini` místo jména nasazení.

   Měli byste vidět výstup jako následující:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Různé typy promptů pro různé úkoly

Nyní jste viděli, jak generovat text pomocí promptu. Dokonce máte běžící program, který můžete upravovat a měnit pro generování různých typů textů.

Prompty lze použít pro různé úkoly. Například:

- **Generovat typ textu**. Například můžete generovat báseň, otázky pro kvíz atd.
- **Vyhledávat informace**. Můžete použít prompty k vyhledávání informací, například "Co znamená CORS ve vývoji webu?".
- **Generovat kód**. Pomocí promptů můžete generovat kód, například vyvíjet regulární výraz na validaci emailů, nebo proč ne vytvořit celý program, například webovou aplikaci?

## Praktický případ: generátor receptů

Představte si, že máte doma suroviny a chcete něco uvařit. K tomu potřebujete recept. Jak najít recepty? Můžete použít vyhledávač nebo LLM.

Můžete napsat prompt například takto:

> "Ukaž mi 5 receptů na jídlo s těmito ingrediencemi: kuře, brambory a mrkev. U každého receptu uveď všechny použité ingredience."

Na základě tohoto promptu můžete obdržet odpověď podobnou této:

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

Tento výsledek je skvělý, vím, co uvařit. V tomto bodě by byly užitečné následující vylepšení:

- Filtrování ingrediencí, které nemám rád nebo na které jsem alergický.
- Vytvoření nákupního seznamu, pokud některé ingredience doma nemám.

Pro uvedené případy přidáme další prompt:

> "Prosím odstraň recepty s česnekem, protože jsem na něj alergický, a nahraď je něčím jiným. Také prosím vytvoř nákupní seznam pro recepty, přičemž zohledni, že doma už mám kuře, brambory a mrkev."

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

To jsou vaše pět receptů, bez česneku a také máte nákupní seznam vzhledem k tomu, co už doma máte.

## Cvičení - vytvořte generátor receptů

Nyní, když máme scénář vysvětlený, pojďme napsat kód odpovídající uvedenému scénáři. Postupujte podle těchto kroků:

1. Použijte existující soubor _app.py_ jako výchozí bod
1. Najděte proměnnou `prompt` a změňte její kód na následující:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Pokud nyní spustíte kód, měli byste vidět výstup podobný:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > POZNÁMKA: váš LLM není deterministický, proto můžete po každém spuštění programu získat jiné výsledky.

   Skvěle, podíváme se, jak věci zlepšit. Abychom zlepšili věci, chceme, aby byl kód flexibilní, takže ingredience i počet receptů budou možné upravovat a měnit.

1. Změňme kód takto:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testovací spuštění kódu by mohlo vypadat takto:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Vylepšení přidáním filtru a nákupního seznamu

Nyní máme funkční aplikaci, která dokáže vytvářet recepty, a je flexibilní, protože závisí na vstupu uživatele, jak v počtu receptů, tak i v použitých ingrediencích.

Pro další zlepšení chceme přidat následující:

- **Filtrovat ingredience**. Chceme mít možnost filtrovat ingredience, které nemáme rádi nebo na které jsme alergičtí. K tomu upravíme náš stávající prompt a přidáme na jeho konec podmínku filtru, například takto:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Výše přidáváme `{filter}` na konec promptu a také zachytáváme hodnotu filtru od uživatele.

  Příklad vstupu při běhu programu může nyní vypadat takto:

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

  Jak vidíte, všechny recepty obsahující mléko byly odfiltrovány. Pokud jste však laktózově intolerantní, můžete chtít odfiltrovat i recepty se sýrem, takže je potřeba být jasný.

- **Vytvořit nákupní seznam**. Chceme vytvořit nákupní seznam s ohledem na to, co už doma máme.

  Pro tuto funkci můžeme zkusit vyřešit vše v jednom promptu, nebo to rozdělit do dvou promptů. Zkusme druhý přístup. Navrhujeme přidat další prompt, ale k tomu, aby to fungovalo, musíme přidat výsledek prvního promptu jako kontext do druhého promptu.

  Najděte místo v kódu, kde se tiskne výsledek z prvního promptu, a přidejte níže následující kód:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Všimněte si následujícího:

  1. Vytváříme nový prompt tak, že připojujeme výsledek z prvního promptu k novému promptu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  2. Požadujeme novou žádost, ale bereme v úvahu počet tokenů z prvního promptu, takže tentokrát nastavujeme `max_output_tokens` na 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Vyzkoušením tohoto kódu nyní dostáváme následující výstup:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Vylepšete své prostředí

Co zatím máme, je kód, který funguje, ale existují nějaké úpravy, které bychom měli udělat, aby to bylo ještě lepší. Některé věci, které bychom měli udělat, jsou:

- **Oddělit tajné údaje od kódu**, jako je API klíč. Tajné údaje nepatří do kódu a měly by být uloženy na bezpečném místě. Pro oddělení tajných údajů od kódu můžeme použít proměnné prostředí a knihovny jako `python-dotenv` pro jejich načtení ze souboru. Takto by to v kódu vypadalo:

  1. Vytvořte soubor `.env` s následujícím obsahem:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Poznámka, pro Azure OpenAI v Microsoft Foundry je třeba místo toho nastavit následující proměnné prostředí:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     V kódu byste proměnné prostředí načetli takto:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Slovo o délce tokenů**. Měli bychom zvážit, kolik tokenů potřebujeme k vygenerování požadovaného textu. Tokeny něco stojí, takže kde je to možné, měli bychom se snažit šetřit počtem použitých tokenů. Například, můžeme prompt formulovat tak, abychom použili méně tokenů?

  Pro změnu počtu použitých tokenů můžete použít parametr `max_output_tokens`. Například pokud chcete použít 100 tokenů, uděláte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentování s teplotou**. Teplota je něco, o čem jsme zatím nemluvili, ale je to důležitý parametr pro to, jak náš program funguje. Čím vyšší je hodnota teploty, tím náhodnější bude výstup. Naopak, čím nižší je hodnota teploty, tím předvídatelnější bude výstup. Zvažte, zda chcete mít ve výstupu variabilitu nebo ne.

  Pro změnu teploty můžete použít parametr `temperature`. Například pokud chcete použít teplotu 0,5, uděláte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Poznámka, čím blíže k 1,0, tím rozmanitější bude výstup.

- **Modely pro uvažování nepoužívají `temperature`**. Jedná se o důležitý posun v roce 2026. Současné, nepřestárlé modely v Microsoft Foundry jsou **modely pro uvažování** (rodina GPT-5, řada o) - a **nepodporují `temperature` ani `top_p`** (ani `max_tokens`; použijte `max_output_tokens`). Pokud pošlete `temperature` na `gpt-5-mini`, obdržíte chybu „parameter not supported“. Takže pro vyzkoušení výše uvedeného příkladu s teplotou zvolte model, který stále podporuje ovládání vzorkování – například otevřený model **Llama** jako `Llama-3.3-70B-Instruct` z [katalogu modelů Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), volaný přes endpoint Foundry Models / Azure AI Inference (stejně jako vzorky `githubmodels-*`). U modelů pro uvažování jako GPT-5 se výstup řídí jinak:
  - **Řízení promptem** - jasné instrukce, příklady a strukturovaný výstup (viz lekce [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) dělají práci, kterou dříve dělala ovládání vzorkování.
  - **Ovládání rozumování** - parametry jako úsilí o rozumování/verbóznost vyvažují hloubku rozumování proti latenci a nákladům.

  Stručně: `temperature`/`top_p` jsou stále platné u mnoha modelů (Llama, Mistral, Phi a rodina GPT-4.x - i když GPT-4.x je na ústupu), ale směr je prompt engineering + ovládání rozumování u rozumových modelů jako GPT-5.

## Zadání

Pro toto zadání si můžete vybrat, co chcete postavit.

Zde je několik návrhů:

- Vylepšete aplikaci generátoru receptů. Hrajte si s hodnotami teploty a s prompty, abyste zjistili, co vám může vygenerovat.
- Vytvořte "studijního kamaráda". Tato aplikace by měla být schopna odpovídat na otázky týkající se určitého tématu, například Pythonu, můžete mít prompty jako "Co je určitý koncept v Pythonu?" nebo třeba prompt, který říká, ukaž mi kód pro dané téma atd.
- Historický bot, oživte historii, nařiďte botovi, aby hrál určitou historickou postavu a ptejte se ho na otázky o jejím životě a době.

## Řešení

### Studijní kamarád

Níže je startovní prompt, podívejte se, jak jej můžete použít a upravit podle svého gusta.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historický bot

Zde je několik promptů, které můžete použít:

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

Při práci na zadání zkuste měnit teplotu, nastavte ji na 0, 0,5 a 1. Pamatujte, že 0 je nejméně variabilní a 1 nejvíce. Která hodnota funguje nejlépe pro vaši aplikaci?

## Skvělá práce! Pokračujte ve vzdělávání

Po dokončení této lekce se podívejte na naši [kolekci pro učení Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste dále rozšiřovali své znalosti o generativní AI!

Přejděte na lekci 7, kde se podíváme, jak [vytvářet chatovací aplikace](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->