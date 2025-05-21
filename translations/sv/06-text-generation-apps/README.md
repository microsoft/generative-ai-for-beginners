<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T16:59:51+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "sv"
}
-->
# Bygga textgenereringsapplikationer

[![Bygga textgenereringsapplikationer](../../../translated_images/06-lesson-banner.90d8a665630e46b2990412d7c7d3d43c30f2441c95c0ee93e0763fb252734e83.sv.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

Hittills har du sett genom denna läroplan att det finns kärnkoncept som uppmaningar och till och med en hel disciplin som kallas "prompt engineering". Många verktyg som du kan interagera med, som ChatGPT, Office 365, Microsoft Power Platform och fler, stödjer dig i att använda uppmaningar för att åstadkomma något.

För att du ska kunna lägga till en sådan upplevelse i en app behöver du förstå koncept som uppmaningar, slutföranden och välja ett bibliotek att arbeta med. Det är precis vad du kommer att lära dig i detta kapitel.

## Introduktion

I detta kapitel kommer du att:

- Lära dig om openai-biblioteket och dess kärnkoncept.
- Bygga en textgenereringsapp med openai.
- Förstå hur man använder koncept som uppmaning, temperatur och tokens för att bygga en textgenereringsapp.

## Inlärningsmål

I slutet av denna lektion kommer du att kunna:

- Förklara vad en textgenereringsapp är.
- Bygga en textgenereringsapp med openai.
- Konfigurera din app för att använda fler eller färre tokens och även ändra temperaturen för ett varierat resultat.

## Vad är en textgenereringsapp?

Normalt när du bygger en app har den någon form av gränssnitt som följande:

- Kommando-baserad. Konsolappar är typiska appar där du skriver ett kommando och den utför en uppgift. Till exempel är `git` en kommando-baserad app.
- Användargränssnitt (UI). Vissa appar har grafiska användargränssnitt (GUIs) där du klickar på knappar, matar in text, väljer alternativ och mer.

### Konsol- och UI-appar är begränsade

Jämför det med en kommando-baserad app där du skriver ett kommando:

- **Det är begränsat**. Du kan inte bara skriva vilket kommando som helst, bara de som appen stödjer.
- **Språkspecifik**. Vissa appar stödjer många språk, men som standard är appen byggd för ett specifikt språk, även om du kan lägga till fler språkstöd.

### Fördelar med textgenereringsappar

Så hur är en textgenereringsapp annorlunda?

I en textgenereringsapp har du mer flexibilitet, du är inte begränsad till en uppsättning kommandon eller ett specifikt inmatningsspråk. Istället kan du använda naturligt språk för att interagera med appen. En annan fördel är att eftersom du redan interagerar med en datakälla som har tränats på en stor mängd information, medan en traditionell app kan vara begränsad till vad som finns i en databas.

### Vad kan jag bygga med en textgenereringsapp?

Det finns många saker du kan bygga. Till exempel:

- **En chatbot**. En chatbot som svarar på frågor om ämnen, som ditt företag och dess produkter, kan vara en bra matchning.
- **Hjälpare**. LLMs är bra på saker som att sammanfatta text, få insikter från text, producera text som CV:n och mer.
- **Kodassistent**. Beroende på språket du använder kan du bygga en kodassistent som hjälper dig att skriva kod. Till exempel kan du använda en produkt som GitHub Copilot samt ChatGPT för att hjälpa dig skriva kod.

## Hur kan jag komma igång?

Tja, du behöver hitta ett sätt att integrera med en LLM vilket vanligtvis innebär följande två tillvägagångssätt:

- Använda ett API. Här konstruerar du webbförfrågningar med din uppmaning och får genererad text tillbaka.
- Använda ett bibliotek. Bibliotek hjälper till att kapsla in API-anropen och göra dem lättare att använda.

## Bibliotek/SDK:er

Det finns några välkända bibliotek för att arbeta med LLMs som:

- **openai**, detta bibliotek gör det enkelt att ansluta till din modell och skicka in uppmaningar.

Sedan finns det bibliotek som fungerar på en högre nivå som:

- **Langchain**. Langchain är välkänt och stödjer Python.
- **Semantic Kernel**. Semantic Kernel är ett bibliotek av Microsoft som stödjer språken C#, Python och Java.

## Första appen med openai

Låt oss se hur vi kan bygga vår första app, vilka bibliotek vi behöver, hur mycket som krävs och så vidare.

### Installera openai

Det finns många bibliotek där ute för att interagera med OpenAI eller Azure OpenAI. Det är möjligt att använda flera programmeringsspråk som C#, Python, JavaScript, Java och mer. Vi har valt att använda `openai` Python-biblioteket, så vi kommer att använda `pip` för att installera det.

```bash
pip install openai
```

### Skapa en resurs

Du behöver utföra följande steg:

- Skapa ett konto på Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Få tillgång till Azure OpenAI. Gå till [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) och begär åtkomst.

  > [!NOTE]
  > Vid skrivande stund behöver du ansöka om åtkomst till Azure OpenAI.

- Installera Python <https://www.python.org/>
- Ha skapat en Azure OpenAI Service-resurs. Se denna guide för hur man [skapar en resurs](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Hitta API-nyckel och slutpunkt

Vid denna punkt behöver du tala om för ditt `openai`-bibliotek vilken API-nyckel som ska användas. För att hitta din API-nyckel, gå till avsnittet "Keys and Endpoint" i din Azure OpenAI-resurs och kopiera värdet för "Key 1".

![Keys and Endpoint-resursblad i Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nu när du har kopierat denna information, låt oss instruera biblioteken att använda den.

> [!NOTE]
> Det är värt att separera din API-nyckel från din kod. Du kan göra det genom att använda miljövariabler.
>
> - Ställ in miljövariabeln `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Konfigurera Azure

Om du använder Azure OpenAI, här är hur du konfigurerar det:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Ovan ställer vi in följande:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` klass. Här är ett exempel:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

I koden ovan skapar vi ett slutförandeobjekt och skickar in modellen vi vill använda och uppmaningen. Sedan skriver vi ut den genererade texten.

### Chat-slutföranden

Hittills har du sett hur vi har använt `Completion` to generate text. But there's another class called `ChatCompletion` som är mer lämpad för chatbots. Här är ett exempel på att använda det:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Mer om denna funktionalitet i ett kommande kapitel.

## Övning - din första textgenereringsapp

Nu när vi har lärt oss hur man sätter upp och konfigurerar openai är det dags att bygga din första textgenereringsapp. För att bygga din app, följ dessa steg:

1. Skapa en virtuell miljö och installera openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Om du använder Windows skriv `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` värde.

1. Skapa en _app.py_-fil och ge den följande kod:

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
   > Om du använder Azure OpenAI behöver du ställa in `api_type` to `azure` and set the `api_key` till din Azure OpenAI-nyckel.

   Du bör se ett resultat som ser ut så här:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Olika typer av uppmaningar, för olika saker

Nu har du sett hur man genererar text med en uppmaning. Du har till och med ett program igång som du kan modifiera och ändra för att generera olika typer av text.

Uppmaningar kan användas för alla möjliga uppgifter. Till exempel:

- **Generera en typ av text**. Till exempel kan du generera en dikt, frågor till ett quiz etc.
- **Slå upp information**. Du kan använda uppmaningar för att leta efter information som följande exempel 'Vad betyder CORS i webbutveckling?'.
- **Generera kod**. Du kan använda uppmaningar för att generera kod, till exempel utveckla ett reguljärt uttryck som används för att validera e-post eller varför inte generera ett helt program, som en webbapp?

## Ett mer praktiskt användningsfall: en receptgenerator

Tänk dig att du har ingredienser hemma och vill laga något. För det behöver du ett recept. Ett sätt att hitta recept är att använda en sökmotor eller så kan du använda en LLM för att göra det.

Du kan skriva en uppmaning som så:

> "Visa mig 5 recept för en maträtt med följande ingredienser: kyckling, potatis och morötter. För varje recept, lista alla ingredienser som används"

Med den ovanstående uppmaningen kan du få ett svar som liknar:

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

Detta resultat är fantastiskt, jag vet vad jag ska laga. Vid denna punkt, vad som skulle kunna vara användbara förbättringar är:

- Filtrera bort ingredienser jag inte gillar eller är allergisk mot.
- Producera en inköpslista, ifall jag inte har alla ingredienser hemma.

För de ovanstående fallen, låt oss lägga till en ytterligare uppmaning:

> "Vänligen ta bort recept med vitlök eftersom jag är allergisk och ersätt det med något annat. Producera också en inköpslista för recepten, med tanke på att jag redan har kyckling, potatis och morötter hemma."

Nu har du ett nytt resultat, nämligen:

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

Det är dina fem recept, utan vitlök nämnd och du har också en inköpslista med tanke på vad du redan har hemma.

## Övning - bygg en receptgenerator

Nu när vi har spelat ut ett scenario, låt oss skriva kod för att matcha det demonstrerade scenariot. För att göra det, följ dessa steg:

1. Använd den befintliga _app.py_-filen som en startpunkt
1. Hitta variabeln `prompt` och ändra dess kod till följande:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Om du nu kör koden bör du se ett resultat som liknar:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > OBS, din LLM är icke-deterministisk, så du kan få olika resultat varje gång du kör programmet.

   Bra, låt oss se hur vi kan förbättra saker. För att förbättra saker vill vi se till att koden är flexibel, så ingredienser och antal recept kan förbättras och ändras.

1. Låt oss ändra koden på följande sätt:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Att ta koden för en testrunda, kan se ut så här:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Förbättra genom att lägga till filter och inköpslista

Vi har nu en fungerande app som kan producera recept och den är flexibel eftersom den förlitar sig på inmatningar från användaren, både på antalet recept men också de ingredienser som används.

För att ytterligare förbättra den vill vi lägga till följande:

- **Filtrera bort ingredienser**. Vi vill kunna filtrera bort ingredienser vi inte gillar eller är allergiska mot. För att åstadkomma denna förändring kan vi redigera vår befintliga uppmaning och lägga till ett filtervillkor i slutet av den som så här:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ovan lägger vi till `{filter}` i slutet av uppmaningen och vi fångar också filtervärdet från användaren.

  Ett exempel på inmatning vid körning av programmet kan nu se ut så här:

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

  Som du kan se har alla recept med mjölk i det filtrerats bort. Men om du är laktosintolerant kanske du också vill filtrera bort recept med ost i dem, så det finns ett behov av att vara tydlig.

- **Producera en inköpslista**. Vi vill producera en inköpslista, med tanke på vad vi redan har hemma.

  För denna funktionalitet kan vi antingen försöka lösa allt i en uppmaning eller så kan vi dela upp det i två uppmaningar. Låt oss försöka med det senare tillvägagångssättet. Här föreslår vi att lägga till en ytterligare uppmaning, men för att det ska fungera måste vi lägga till resultatet av den första uppmaningen som kontext till den senare uppmaningen.

  Hitta den del i koden som skriver ut resultatet från den första uppmaningen och lägg till följande kod nedanför:

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

  Notera följande:

  1. Vi konstruerar en ny uppmaning genom att lägga till resultatet från den första uppmaningen till den nya uppmaningen:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Vi gör en ny förfrågan, men också med hänsyn till antalet tokens vi bad om i den första uppmaningen, så denna gång säger vi att `max_tokens` är 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     När vi tar denna kod för en testrunda, kommer vi nu fram till följande resultat:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Förbättra din setup

Det vi har hittills är kod som fungerar, men det finns några justeringar vi bör göra för att förbättra saker ytterligare. Några saker vi bör göra är:

- **Separera hemligheter från kod**, som API-nyckeln. Hemligheter hör inte hemma i kod och bör lagras på en säker plats. För att separera hemligheter från kod kan vi använda miljövariabler och bibliotek som `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env`-fil med följande innehåll:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Notera, för Azure, behöver du ställa in följande miljövariabler:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     I kod skulle du ladda miljövariablerna så här:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Ett ord om token-längd**. Vi bör överväga hur många tokens vi behöver för att generera den text vi vill ha. Tokens kostar pengar, så där det är möjligt bör vi försöka vara ekonomiska med antalet tokens vi använder. Till exempel, kan vi formulera uppmaningen så att vi kan använda färre tokens?

  För att ändra de tokens som används kan du använda parametern `max_tokens`. Till exempel, om du vill använda 100 tokens, skulle du göra:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Experimentera med temperatur**. Temperatur är något vi inte har nämnt hittills men är en viktig kontext för hur vårt program presterar. Ju högre temperaturvärde desto mer slumpmässigt blir resultatet. Omvänt, ju lägre temperaturvärde desto mer förutsägbart blir resultatet. Överväg om du vill ha variation i ditt resultat eller inte.

  För att ändra temperaturen kan du använda parametern `temperature`. Till exempel, om du vill använda en temperatur på 0.5, skulle du göra:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Notera, ju närmare 1.0, desto mer varierat blir resultatet.

## Uppgift

För denna uppgift kan du välja vad du vill bygga.

Här är några förslag:

- Justera receptgenerator-appen för att förbättra den ytterligare. Lek med temperaturvärden och uppmaningarna för att se vad du kan komma på.
- Bygg en "studiekamrat". Denna app bör kunna svara på frågor om ett ämne, till exempel Python, du kan ha uppmaningar som "Vad är ett visst ämne i Python?", eller du kan ha en uppmaning som säger, visa mig kod för ett visst ämne etc.
- Historiebot, få historien att komma till liv, instruera boten att spela en viss historisk karaktär och ställ frågor om dess liv och tider.

## Lösning

### Studiekamrat

Nedan är en startuppmaning, se hur du kan använda den och justera den efter dina önskemål.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historiebot

Här är några uppmaningar du kan använda:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Kunskapskontroll

Vad gör konceptet temperatur?

1. Det kontrollerar hur slumpmässigt resultatet är.
1. Det kontroller

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller misstolkningar som uppstår vid användningen av denna översättning.