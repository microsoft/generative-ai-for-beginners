# Bygga applikationer för textgenerering

[![Bygga applikationer för textgenerering](../../../translated_images/sv/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klicka på bilden ovan för att se videon till denna lektion)_

Hittills i detta kursmaterial har du sett att det finns kärnkoncept som prompts och till och med en hel disciplin som kallas "prompt engineering". Många verktyg du kan interagera med som ChatGPT, Office 365, Microsoft Power Platform med flera, stöder dig att använda prompts för att åstadkomma något.

För att du ska kunna lägga till en sådan upplevelse i en app behöver du förstå begrepp som prompts, completions och välja ett bibliotek att arbeta med. Det är precis vad du kommer lära dig i detta kapitel.

## Introduktion

I detta kapitel kommer du att:

- Lära dig om biblioteket openai och dess kärnkoncept.
- Bygga en app för textgenerering med openai.
- Förstå hur man använder begrepp som prompt, temperature och tokens för att bygga en app för textgenerering.

## Lärandemål

I slutet av denna lektion kommer du kunna:

- Förklara vad en app för textgenerering är.
- Bygga en app för textgenerering med openai.
- Konfigurera din app för att använda fler eller färre tokens och även ändra temperaturen för varierande utdata.

## Vad är en app för textgenerering?

Vanligtvis när du bygger en app har den någon form av gränssnitt som följande:

- Kommandobaserad. Konsolappar är typiska appar där du skriver ett kommando och den utför en uppgift. Ett exempel är `git` som är en kommandobaserad app.
- Användargränssnitt (UI). Vissa appar har grafiska användargränssnitt (GUI) där du klickar på knappar, matar in text, väljer alternativ med mera.

### Konsol- och UI-appar är begränsade

Jämför det med en kommandobaserad app där du skriver ett kommando:

- **Den är begränsad**. Du kan inte bara skriva vilket kommando som helst, utan bara de som appen stödjer.
- **Språkberoende**. Vissa appar stödjer flera språk, men som standard är appen byggd för ett specifikt språk, även om du kan lägga till fler språkstöd.

### Fördelar med appar för textgenerering

Så hur skiljer sig en app för textgenerering?

I en app för textgenerering har du mer flexibilitet; du är inte begränsad till en uppsättning kommandon eller ett specifikt inmatningsspråk. Istället kan du använda naturligt språk för att interagera med appen. En annan fördel är att du redan interagerar med en datakälla som har tränats på ett omfattande informationsmaterial, medan en traditionell app kanske är begränsad till vad som finns i en databas.

### Vad kan jag bygga med en app för textgenerering?

Det finns många saker du kan bygga. Till exempel:

- **En chatbot**. En chatbot som svarar på frågor om ämnen, som ditt företag och dess produkter, kan vara en bra match.
- **Hjälpare**. Stora språkmodeller (LLM) är bra på saker som att sammanfatta text, få insikter från text, producera text som CV:n med mera.
- **Kodassistent**. Beroende på vilken språkmodell du använder kan du bygga en kodassistent som hjälper dig att skriva kod. Du kan till exempel använda produkter som GitHub Copilot samt ChatGPT för att hjälpa dig skriva kod.

## Hur kan jag komma igång?

Först behöver du hitta ett sätt att integrera med en LLM vilket vanligtvis innebär följande två tillvägagångssätt:

- Använd en API. Här bygger du webbrequests med din prompt och får genererad text tillbaka.
- Använd ett bibliotek. Bibliotek hjälper till att kapsla in API-anrop och göra dem enklare att använda.

## Bibliotek/SDK:er

Det finns några välkända bibliotek för att arbeta med LLM:er som:

- **openai**, detta bibliotek gör det enkelt att koppla upp sig mot din modell och skicka in prompts.

Sedan finns det bibliotek som opererar på en högre nivå som:

- **Langchain**. Langchain är välkänt och stödjer Python.
- **Semantic Kernel**. Semantic Kernel är ett bibliotek från Microsoft som stöder språken C#, Python och Java.

## Första appen med openai

Låt oss se hur vi kan bygga vår första app, vilka bibliotek vi behöver, hur mycket som krävs med mera.

### Installera openai

Det finns många bibliotek för att interagera med OpenAI eller Azure OpenAI. Det går också att använda många programmeringsspråk som C#, Python, JavaScript, Java med flera. Vi har valt att använda Python-biblioteket `openai`, så vi använder `pip` för att installera det.

```bash
pip install openai
```

### Skapa en resurs

Du behöver utföra följande steg:

- Skapa ett konto på Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Få tillgång till Azure OpenAI. Gå till [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) och ansök om tillgång.

  > [!NOTE]
  > Vid skrivande stund måste du ansöka om tillgång till Azure OpenAI.

- Installera Python <https://www.python.org/>
- Har skapat en Azure OpenAI Service-resurs. Se denna guide för hur du [skapar en resurs](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Hitta API-nyckel och slutpunkt

Vid detta steg behöver du säga åt ditt `openai`-bibliotek vilken API-nyckel som ska användas. För att hitta din API-nyckel, gå till sektionen "Keys and Endpoint" i din Azure OpenAI-resurs och kopiera värdet "Key 1".

![Nycklar och slutpunktsresurs i Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nu när du har kopierat denna information, låt oss instruera biblioteken att använda den.

> [!NOTE]
> Det är värt att separera din API-nyckel från din kod. Det kan du göra genom att använda miljövariabler.
>
> - Sätt miljövariabeln `OPENAI_API_KEY` till din API-nyckel.
>   `export OPENAI_API_KEY='sk-...'`

### Konfigurera Azure

Om du använder Azure OpenAI (nu del av Microsoft Foundry) så här ställer du in konfigurationen. Vi använder standardklienten `OpenAI` riktad mot Azure OpenAI-slutpunkten `/openai/v1/` som fungerar med Responses API och kräver ingen `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Ovan ställer vi in följande:

- `api_key`, detta är din API-nyckel som hittas i Azure-portalen eller Microsoft Foundry-portalen.
- `base_url`, detta är din Foundry-resursslutpunkt med `/openai/v1/` tillagt. Den stabila v1-slutpunkten fungerar både för OpenAI och Azure OpenAI utan att hantera `api_version`.

> [!NOTE] > `os.environ` läser miljövariabler. Du kan använda det för att läsa miljövariabler som `AZURE_OPENAI_API_KEY` och `AZURE_OPENAI_ENDPOINT`. Sätt dessa i din terminal eller genom att använda ett bibliotek som `dotenv`.

## Generera text

Sättet att generera text är att använda Responses API via metoden `responses.create`. Här är ett exempel:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # detta är ditt modellutplaceringsnamn
    input=prompt,
    store=False,
)
print(response.output_text)
```

I koden ovan skapar vi ett svar och skickar in modellen vi vill använda samt prompten. Sedan skriver vi ut den genererade texten via `response.output_text`.

### Flerstegssamtal

Responses API passar väl för både enkel textgenerering och flerstegschattbotar – du anger en lista med meddelanden i `input` för att bygga upp en konversation:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Mer om denna funktion i ett kommande kapitel.

## Övning – din första app för textgenerering

Nu när vi lärt oss hur man ställer in och konfigurerar openai är det dags att bygga din första app för textgenerering. Följ dessa steg för att bygga din app:

1. Skapa en virtuell miljö och installera openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Om du använder Windows, skriv `venv\Scripts\activate` istället för `source venv/bin/activate`.

   > [!NOTE]
   > Hitta din Azure OpenAI-nyckel genom att gå till [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) och sök på `Open AI`, välj sedan `Open AI-resurs` och sen `Keys and Endpoint` och kopiera värdet `Key 1`.

1. Skapa en fil _app.py_ och ge den följande kod:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # lägg till din fullföljandekod
   prompt = "Complete the following: Once upon a time there was a"

   # gör en förfrågan med Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # skriv ut svaret
   print(response.output_text)
   ```

   > [!NOTE]
   > Om du använder vanlig OpenAI (inte Azure), använd `client = OpenAI(api_key="<ersätt detta värde med din OpenAI-nyckel>")` (ingen `base_url`) och ange ett modellnamn som `gpt-5-mini` istället för ett distributionsnamn.

   Du bör se en utdata som liknar följande:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Olika typer av prompts för olika ändamål

Nu har du sett hur man genererar text med en prompt. Du har till och med ett program som körs som du kan ändra och modifiera för att generera olika typer av text.

Prompts kan användas för alla möjliga uppgifter. Till exempel:

- **Generera en typ av text**. Till exempel kan du generera en dikt, frågor till en quiz med mera.
- **Söka information**. Du kan använda prompts för att söka information som i följande exempel: 'Vad betyder CORS i webbutveckling?'.
- **Generera kod**. Du kan använda prompts för att generera kod, till exempel skapa ett reguljärt uttryck för att validera e-postadresser eller varför inte generera ett helt program, som en webbapp?

## Ett mer praktiskt exempel: en receptgenerator

Föreställ dig att du har ingredienser hemma och vill laga något. Då behöver du ett recept. Ett sätt att hitta recept är att använda en sökmotor eller så kan du använda en LLM för detta.

Du kan skriva en prompt så här:

> "Visa mig 5 recept för en rätt med följande ingredienser: kyckling, potatis och morötter. Lista alla ingredienser som används per recept."

Med ovanstående prompt kan du få ett svar liknande:

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

Detta resultat är utmärkt, jag vet vad jag kan laga. Vid detta tillfälle kan följande förbättringar vara användbara:

- Filtrera bort ingredienser jag inte gillar eller är allergisk mot.
- Skapa en inköpslista ifall jag inte har alla ingredienser hemma.

För ovanstående fall, låt oss lägga till en extra prompt:

> "Var snäll och ta bort recept med vitlök eftersom jag är allergisk och ersätt det med något annat. Skapa även en inköpslista för recepten med tanke på att jag redan har kyckling, potatis och morötter hemma."

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

Det är dina fem recept, utan vitlök nämnt och du har även en inköpslista med tanke på vad du redan har hemma.

## Övning - bygg en receptgenerator

Nu när vi spelat upp ett scenario, låt oss skriva kod som matchar det visade scenariot. Följ dessa steg:

1. Använd den befintliga filen _app.py_ som utgångspunkt
1. Hitta variabeln `prompt` och ändra dess kod till följande:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Om du nu kör koden bör du se en utdata liknande denna:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > OBS, din LLM är icke-deterministisk, så du kan få olika resultat varje gång du kör programmet.

   Utmärkt, låt oss se hur vi kan förbättra saker. För att förbättra vill vi göra koden flexibel så att ingredienser och antal recept kan ändras och förbättras.

1. Låt oss ändra koden på följande sätt:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolera antalet recept i prompten och ingredienserna
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Att använda koden för ett testkör kan se ut så här:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Förbättra med att lägga till filter och inköpslista

Vi har nu en fungerande app som kan producera recept och den är flexibel eftersom den bygger på användarens input, både på antal recept och ingredienser som används.

För att förbättra vidare vill vi lägga till följande:

- **Filtrera bort ingredienser**. Vi vill kunna filtrera bort ingredienser vi inte gillar eller är allergiska mot. För att åstadkomma detta kan vi ändra vår befintliga prompt och lägga till ett filtervillkor i slutet som så:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ovan lägger vi till `{filter}` i slutet av prompten och vi fångar även filtret från användaren.

  Ett exempel på input för att köra programmet kan nu se ut så här:

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

  Som du kan se har recept med mjölk filtrerats bort. Men om du är laktosintolerant kanske du även vill filtrera bort recept med ost, så det finns ett behov av att vara tydlig.


- **Skapa en inköpslista**. Vi vill skapa en inköpslista med hänsyn till vad vi redan har hemma.

  För denna funktionalitet kan vi antingen försöka lösa allt i en prompt eller dela upp det i två promptar. Låt oss prova det senare tillvägagångssättet. Här föreslår vi att lägga till en ytterligare prompt, men för att det ska fungera behöver vi lägga till resultatet från den första prompten som kontext till den senare prompten.

  Lokalisera delen i koden som skriver ut resultatet från den första prompten och lägg till följande kod nedan:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # skriv ut svar
  print("Shopping list:")
  print(response.output_text)
  ```

  Observera följande:

  1. Vi konstruerar en ny prompt genom att lägga till resultatet från den första prompten till den nya prompten:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Vi gör en ny förfrågan, men med hänsyn till antalet tokens vi bad om i den första prompten, så den här gången säger vi `max_output_tokens` är 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     När vi testar denna kod får vi nu följande utskrift:

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

Vad vi har hittills är kod som fungerar, men det finns några justeringar vi bör göra för att förbättra saker ytterligare. Några saker vi bör göra är:

- **Separera hemligheter från kod**, som API-nyckeln. Hemligheter hör inte hemma i koden och bör lagras på en säker plats. För att separera hemligheter från kod kan vi använda miljövariabler och bibliotek som `python-dotenv` för att läsa in dem från en fil. Så här skulle det se ut i koden:

  1. Skapa en `.env`-fil med följande innehåll:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Observera, för Azure OpenAI i Microsoft Foundry behöver du istället sätta följande miljövariabler:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     I koden skulle du ladda miljövariablerna så här:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Ett ord om tokenlängd**. Vi bör överväga hur många tokens vi behöver för att generera den text vi vill ha. Tokens kostar pengar, så där det är möjligt bör vi försöka vara sparsamma med antalet tokens vi använder. Kan vi till exempel formulera prompten så att vi kan använda färre tokens?

  För att ändra tokens som används kan du använda parametern `max_output_tokens`. Om du till exempel vill använda 100 tokens, gör du så här:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentera med temperatur**. Temperatur är något vi inte nämnt hittills men är en viktig parameter för hur vårt program presterar. Ju högre temperatursvärde desto mer slumpmässig blir outputen. Omvänt, ju lägre temperatursvärde desto mer förutsägbar blir outputen. Fundera på om du vill ha variation i ditt svar eller inte.

  För att ändra temperaturen kan du använda parametern `temperature`. Om du till exempel vill använda en temperatur på 0,5, gör du så här:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Observera, ju närmare 1,0 desto mer varierad output.

- **Resonerande modeller använder inte `temperature`**. Detta är en viktig förändring 2026. De nuvarande, icke-föråldrade modellerna i Microsoft Foundry är **resonerande modeller** (GPT-5-familjen, o-serien) - och de **stöder inte `temperature` eller `top_p`** (inte heller `max_tokens`; använd `max_output_tokens`). Om du skickar `temperature` till `gpt-5-mini` får du ett felmeddelande om att parametern inte stöds. För att prova temperaturoexemplet ovan, rikta det istället mot en modell som fortfarande stöder samplingkontroller – till exempel en öppen **Llama**-modell som `Llama-3.3-70B-Instruct` från [Microsoft Foundry modellkatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), anropad via Foundry Models / Azure AI Inference endpoint (på samma sätt som `githubmodels-*` exemplen). För resonerande modeller som GPT-5 styr du output på annat sätt:
  - **Prompt engineering** - tydliga instruktioner, exempel och strukturerad output (se lektion [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) gör jobbet som samplingkontroller brukade göra.
  - **Reasoning controls** - parametrar som resonemangets insats/utförlighet balanserar djupet i resonemanget mot fördröjning och kostnad.

  Kort sagt: `temperature`/`top_p` är fortfarande giltiga på många modeller (Llama, Mistral, Phi och GPT-4.x-familjen – även om GPT-4.x håller på att föråldras), men utvecklingen går mot prompt engineering + reasoning controls på resonerande modeller som GPT-5.

## Uppgift

För denna uppgift kan du välja vad du vill bygga.

Här är några förslag:

- Justera receptgeneratorappen för att förbättra den ytterligare. Lek runt med temperaturvärden och promptarna för att se vad du kan komma fram till.
- Bygg en "studiekamrat". Denna app ska kunna svara på frågor om ett ämne, till exempel Python, du kan ha promptar som "Vad är ett visst ämne i Python?", eller en prompt som säger, visa mig kod för ett visst ämne osv.
- Historiebot, låt historien bli levande, instruera boten att spela en viss historisk person och ställ frågor om dess liv och tid.

## Lösning

### Studiekamrat

Nedan är en startprompt, se hur du kan använda den och justera den efter ditt tycke.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historiebot

Här är några promptar du kan använda:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Kunskapskontroll

Vad gör begreppet temperatur?

1. Det styr hur slumpmässigt resultatet är.
1. Det styr hur stort svaret är.
1. Det styr hur många tokens som används.

## 🚀 Utmaning

När du arbetar med uppgiften, försök variera temperaturen och sätt den till 0, 0,5 och 1. Kom ihåg att 0 är minst varierad och 1 är mest. Vilket värde fungerar bäst för din app?

## Bra jobbat! Fortsätt lära dig

Efter att ha avslutat denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta utveckla din Generative AI-kunskap!

Gå vidare till Lektion 7 där vi tittar på hur man [bygger chattapplikationer](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->