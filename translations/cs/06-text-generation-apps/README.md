<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-17T21:35:41+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "cs"
}
-->
# Vytváření aplikací pro generování textu

[![Vytváření aplikací pro generování textu](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.cs.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

V tomto kurzu jste se již seznámili se základními koncepty, jako jsou prompty, a dokonce s celou disciplínou nazvanou "prompt engineering". Mnoho nástrojů, se kterými můžete pracovat, jako ChatGPT, Office 365, Microsoft Power Platform a další, vám umožňuje používat prompty k dosažení určitého cíle.

Abyste mohli přidat takovou funkci do své aplikace, musíte pochopit koncepty jako prompty, dokončení a vybrat knihovnu, se kterou budete pracovat. Přesně to se naučíte v této kapitole.

## Úvod

V této kapitole se naučíte:

- Seznámit se s knihovnou openai a jejími základními koncepty.
- Vytvořit aplikaci pro generování textu pomocí openai.
- Pochopit, jak používat koncepty jako prompt, teplota a tokeny k vytvoření aplikace pro generování textu.

## Cíle učení

Na konci této lekce budete schopni:

- Vysvětlit, co je aplikace pro generování textu.
- Vytvořit aplikaci pro generování textu pomocí openai.
- Konfigurovat svou aplikaci tak, aby používala více nebo méně tokenů a také měnit teplotu pro různorodý výstup.

## Co je aplikace pro generování textu?

Obvykle, když vytváříte aplikaci, má nějaké rozhraní, například:

- Na základě příkazů. Typické konzolové aplikace, kde zadáte příkaz a aplikace provede úkol. Například `git` je aplikace založená na příkazech.
- Uživatelské rozhraní (UI). Některé aplikace mají grafické uživatelské rozhraní (GUI), kde klikáte na tlačítka, zadáváte text, vybíráte možnosti a další.

### Omezení konzolových a UI aplikací

Porovnejte to s aplikací založenou na příkazech, kde zadáváte příkaz:

- **Je omezená**. Nemůžete zadat libovolný příkaz, pouze ty, které aplikace podporuje.
- **Specifická pro jazyk**. Některé aplikace podporují mnoho jazyků, ale ve výchozím nastavení je aplikace vytvořena pro konkrétní jazyk, i když můžete přidat podporu dalších jazyků.

### Výhody aplikací pro generování textu

Jak se tedy aplikace pro generování textu liší?

V aplikaci pro generování textu máte větší flexibilitu, nejste omezeni na sadu příkazů nebo konkrétní vstupní jazyk. Místo toho můžete používat přirozený jazyk k interakci s aplikací. Další výhodou je, že již pracujete s datovým zdrojem, který byl vyškolen na rozsáhlém korpusu informací, zatímco tradiční aplikace může být omezená na to, co je v databázi.

### Co mohu vytvořit s aplikací pro generování textu?

Existuje mnoho věcí, které můžete vytvořit. Například:

- **Chatbot**. Chatbot odpovídající na otázky o tématech, jako je vaše společnost a její produkty, by mohl být dobrým řešením.
- **Pomocník**. LLM jsou skvělé na věci jako shrnutí textu, získávání poznatků z textu, vytváření textů jako životopisů a další.
- **Asistent pro kódování**. V závislosti na modelu jazyka, který používáte, můžete vytvořit asistenta pro kódování, který vám pomůže psát kód. Například můžete použít produkt jako GitHub Copilot nebo ChatGPT k pomoci při psaní kódu.

## Jak začít?

Musíte najít způsob, jak se integrovat s LLM, což obvykle zahrnuje následující dva přístupy:

- Použít API. Zde sestavujete webové požadavky s vaším promptem a získáváte vygenerovaný text zpět.
- Použít knihovnu. Knihovny pomáhají zapouzdřit volání API a usnadňují jejich použití.

## Knihovny/SDK

Existuje několik známých knihoven pro práci s LLM, například:

- **openai**, tato knihovna usnadňuje připojení k vašemu modelu a odesílání promptů.

Pak jsou tu knihovny, které fungují na vyšší úrovni, například:

- **Langchain**. Langchain je dobře známý a podporuje Python.
- **Semantic Kernel**. Semantic Kernel je knihovna od Microsoftu podporující jazyky C#, Python a Java.

## První aplikace pomocí openai

Podívejme se, jak můžeme vytvořit naši první aplikaci, jaké knihovny potřebujeme, co je nutné a tak dále.

### Instalace openai

Existuje mnoho knihoven pro interakci s OpenAI nebo Azure OpenAI. Je možné použít různé programovací jazyky, jako C#, Python, JavaScript, Java a další. Vybrali jsme knihovnu `openai` pro Python, takže ji nainstalujeme pomocí `pip`.

```bash
pip install openai
```

### Vytvoření zdroje

Musíte provést následující kroky:

- Vytvořte si účet na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Získejte přístup k Azure OpenAI. Přejděte na [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) a požádejte o přístup.

  > [!NOTE]
  > V době psaní je nutné požádat o přístup k Azure OpenAI.

- Nainstalujte Python <https://www.python.org/>
- Vytvořte zdroj služby Azure OpenAI. Podívejte se na tento průvodce, jak [vytvořit zdroj](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Vyhledání API klíče a koncového bodu

V tomto bodě musíte sdělit knihovně `openai`, jaký API klíč má použít. Chcete-li najít svůj API klíč, přejděte do sekce "Keys and Endpoint" ve vašem zdroji Azure OpenAI a zkopírujte hodnotu "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nyní, když máte tyto informace zkopírované, pojďme knihovny instruovat, aby je použily.

> [!NOTE]
> Stojí za to oddělit váš API klíč od vašeho kódu. Můžete to udělat pomocí proměnných prostředí.
>
> - Nastavte proměnnou prostředí `OPENAI_API_KEY` na váš API klíč.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavení konfigurace Azure

Pokud používáte Azure OpenAI, zde je postup nastavení konfigurace:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Výše nastavujeme následující:

- `api_type` na `azure`. To říká knihovně, aby používala Azure OpenAI a ne OpenAI.
- `api_key`, to je váš API klíč nalezený v Azure Portálu.
- `api_version`, to je verze API, kterou chcete použít. V době psaní je nejnovější verze `2023-05-15`.
- `api_base`, to je koncový bod API. Najdete ho v Azure Portálu vedle vašeho API klíče.

> [!NOTE] > `os.getenv` je funkce, která čte proměnné prostředí. Můžete ji použít k čtení proměnných prostředí, jako `OPENAI_API_KEY` a `API_BASE`. Nastavte tyto proměnné prostředí ve vašem terminálu nebo pomocí knihovny jako `dotenv`.

## Generování textu

Způsob, jak generovat text, je použití třídy `Completion`. Zde je příklad:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

V uvedeném kódu vytvoříme objekt completion a předáme model, který chceme použít, a prompt. Poté vytiskneme vygenerovaný text.

### Chat completions

Doposud jste viděli, jak jsme používali `Completion` k generování textu. Ale existuje další třída nazvaná `ChatCompletion`, která je více vhodná pro chatboty. Zde je příklad jejího použití:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Více o této funkci v nadcházející kapitole.

## Cvičení - vaše první aplikace pro generování textu

Nyní, když jsme se naučili, jak nastavit a konfigurovat openai, je čas vytvořit vaši první aplikaci pro generování textu. Postupujte podle těchto kroků:

1. Vytvořte virtuální prostředí a nainstalujte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Pokud používáte Windows, napište `venv\Scripts\activate` místo `source venv/bin/activate`.

   > [!NOTE]
   > Najděte svůj Azure OpenAI klíč tak, že přejdete na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), vyhledáte `Open AI`, vyberete `Open AI resource` a poté vyberete `Keys and Endpoint` a zkopírujete hodnotu `Key 1`.

1. Vytvořte soubor _app.py_ a vložte do něj následující kód:

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
   > Pokud používáte Azure OpenAI, musíte nastavit `api_type` na `azure` a nastavit `api_key` na váš Azure OpenAI klíč.

   Měli byste vidět výstup podobný následujícímu:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Různé typy promptů pro různé účely

Nyní jste viděli, jak generovat text pomocí promptu. Dokonce máte program, který můžete upravit a změnit tak, aby generoval různé typy textu.

Prompty mohou být použity pro různé úkoly. Například:

- **Generování typu textu**. Například můžete generovat báseň, otázky pro kvíz atd.
- **Vyhledávání informací**. Můžete použít prompty k vyhledávání informací, například 'Co znamená CORS ve webovém vývoji?'.
- **Generování kódu**. Můžete použít prompty k generování kódu, například k vytvoření regulárního výrazu pro validaci e-mailů nebo proč ne vytvořit celý program, jako je webová aplikace?

## Praktický příklad: generátor receptů

Představte si, že máte doma ingredience a chcete něco uvařit. K tomu potřebujete recept. Jedním ze způsobů, jak najít recepty, je použít vyhledávač, nebo můžete použít LLM.

Můžete napsat prompt například takto:

> "Ukaž mi 5 receptů na jídlo s následujícími ingrediencemi: kuře, brambory a mrkev. U každého receptu uveď všechny použité ingredience."

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

Tento výsledek je skvělý, vím, co vařit. V tomto bodě by mohly být užitečné následující vylepšení:

- Filtrování ingrediencí, které nemám rád nebo na které jsem alergický.
- Vytvoření nákupního seznamu, pokud nemám všechny ingredience doma.

Pro výše uvedené případy přidáme další prompt:

> "Prosím, odstraň recepty s česnekem, protože jsem na něj alergický, a nahraď ho něčím jiným. Také vytvoř nákupní seznam pro recepty, s ohledem na to, že už mám doma kuře, brambory a mrkev."

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

To je vašich pět receptů, bez zmínky o česneku, a také máte nákupní seznam s ohledem na to, co už máte doma.

## Cvičení - vytvořte generátor receptů

Nyní, když jsme si prošli scénář, napišme kód, který odpovídá demonstrovanému scénáři. Postupujte podle těchto kroků:

1. Použijte existující soubor _app.py_ jako výchozí bod.
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

   > POZNÁMKA, váš LLM je nedeterministický, takže můžete získat různé výsledky pokaždé, když program spustíte.

   Skvělé, podívejme se, jak můžeme věci vylepšit. Abychom věci vylepšili, chceme zajistit, že kód bude flexibilní, takže ingredience a počet receptů mohou být upraveny a změněny.

1. Změňme kód následujícím způsobem:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testovací běh kódu by mohl vypadat takto:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Vylepšení přidáním filtru a nákupního seznamu

Nyní máme funkční aplikaci schopnou vytvářet recepty a je flexibilní, protože se spoléhá na vstupy od uživatele, jak na počet receptů, tak na použité ingredience.

Abychom ji dále vylepšili, chceme přidat následující:

- **Filtrování ingrediencí**. Chceme být schopni filtrovat ingredience, které nemáme rádi nebo na které jsme alergičtí. K dosažení této změny můžeme upravit náš existující prompt a přidat podmínku filtru na jeho konec, například takto:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Výše přidáváme `{filter}` na konec promptu a také zachytáváme hodnotu filtru od uživatele.

  Příklad vstupu při spuštění programu může nyní vypadat takto:

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

  Jak vidíte, jakékoli recepty s mlékem byly odfiltrovány. Ale pokud jste intolerantní na laktózu, možná budete chtít odfiltrovat i recepty se sýrem, takže je potřeba být jasný.

- **Vytvoření nákupního seznamu**. Chceme vytvořit nákupní seznam s ohledem na to, co už máme doma.

  Pro tuto funkci bychom mohli buď zkusit vyřešit vše v jednom promptu, nebo bychom to mohli rozdělit na dva prompty. Zkusme druhý přístup. Zde navrhujeme přidat další prompt, ale aby to fungovalo, musíme přidat výsledek prvního promptu jako kontext k druhému promptu.

  Najděte část v kódu, která tiskne výsledek z prvního promptu, a přidejte následující kód níže:
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

  Všimněte si následujícího:

  1. Vytváříme nový prompt přidáním výsledku z prvního promptu k novému promptu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Vytváříme nový požadavek, ale zároveň bereme v úvahu počet tokenů, které jsme použili v prvním promptu, takže tentokrát nastavíme `max_tokens` na 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
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

To, co máme zatím, je funkční kód, ale existují některé úpravy, které bychom měli provést, abychom věci dále zlepšili. Některé věci, které bychom měli udělat, jsou:

- **Oddělení tajných klíčů od kódu**, jako je API klíč. Tajné klíče nepatří do kódu a měly by být uloženy na bezpečném místě. Pro oddělení tajných klíčů od kódu můžeme použít proměnné prostředí a knihovny jako `python-dotenv`, které je načtou ze souboru. Takto by to vypadalo v kódu:

  1. Vytvořte soubor `.env` s následujícím obsahem:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Poznámka: Pro Azure je třeba nastavit následující proměnné prostředí:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     V kódu byste načetli proměnné prostředí takto:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Poznámka k délce tokenů**. Měli bychom zvážit, kolik tokenů potřebujeme k vygenerování textu, který chceme. Tokeny stojí peníze, takže kde je to možné, měli bychom se snažit být ekonomičtí s počtem použitých tokenů. Například, můžeme formulovat prompt tak, abychom použili méně tokenů?

  Pro změnu počtu použitých tokenů můžete použít parametr `max_tokens`. Například, pokud chcete použít 100 tokenů, udělali byste:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Experimentování s teplotou**. Teplota je něco, co jsme dosud nezmínili, ale je důležitým faktorem pro výkon našeho programu. Čím vyšší je hodnota teploty, tím náhodnější bude výstup. Naopak, čím nižší je hodnota teploty, tím předvídatelnější bude výstup. Zvažte, zda chcete variabilitu ve výstupu nebo ne.

  Pro změnu teploty můžete použít parametr `temperature`. Například, pokud chcete použít teplotu 0.5, udělali byste:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Poznámka: Čím blíže k 1.0, tím rozmanitější bude výstup.

## Úkol

Pro tento úkol si můžete vybrat, co vytvoříte.

Zde jsou některé návrhy:

- Vylepšete aplikaci pro generování receptů. Experimentujte s hodnotami teploty a prompty, abyste zjistili, co dokážete vytvořit.
- Vytvořte "studijního parťáka". Tato aplikace by měla být schopna odpovídat na otázky o určitém tématu, například Pythonu. Můžete mít prompty jako "Co je určitý koncept v Pythonu?" nebo můžete mít prompt, který říká "Ukaž mi kód pro určité téma" atd.
- Historický bot, oživte historii, instruujte bota, aby hrál určitou historickou postavu, a ptejte se ho na jeho život a dobu.

## Řešení

### Studijní parťák

Níže je úvodní prompt, podívejte se, jak ho můžete použít a upravit podle svých potřeb.

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
1. Řídí, kolik tokenů se použije.

## 🚀 Výzva

Při práci na úkolu zkuste měnit teplotu, zkuste ji nastavit na 0, 0.5 a 1. Pamatujte, že 0 je nejméně variabilní a 1 je nejvíce. Jaká hodnota funguje nejlépe pro vaši aplikaci?

## Skvělá práce! Pokračujte ve svém učení

Po dokončení této lekce se podívejte na naši [sbírku učení o generativní AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), abyste dále rozvíjeli své znalosti o generativní AI!

Přejděte na Lekci 7, kde se podíváme na to, jak [vytvářet chatovací aplikace](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.