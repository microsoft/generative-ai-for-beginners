# Bygge tekstgenereringsapplikationer

[![Bygge tekstgenereringsapplikationer](../../../translated_images/da/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

Du har indtil nu set gennem dette pensum, at der er kernebegreber som prompts og endda en hel disciplin kaldet "prompt engineering". Mange værktøjer, som du kan interagere med som ChatGPT, Office 365, Microsoft Power Platform og mere, understøtter brugen af prompts for at opnå noget.

For at tilføje sådan en oplevelse til en app, skal du forstå begreber som prompts, færdiggørelser og vælge et bibliotek at arbejde med. Det er præcis, hvad du vil lære i dette kapitel.

## Introduktion

I dette kapitel vil du:

- Lære om openai biblioteket og dets kernebegreber.
- Bygge en tekstgenereringsapp med openai.
- Forstå hvordan man bruger begreber som prompt, temperatur og tokens til at bygge en tekstgenereringsapp.

## Læringsmål

I slutningen af denne lektion vil du kunne:

- Forklare hvad en tekstgenereringsapp er.
- Bygge en tekstgenereringsapp med openai.
- Konfigurere din app til at bruge flere eller færre tokens og også ændre temperaturen for en varieret output.

## Hvad er en tekstgenereringsapp?

Normalt, når du bygger en app, har den en slags interface som følgende:

- Kommando-baseret. Konsolapps er typiske apps, hvor du skriver en kommando, og den udfører en opgave. For eksempel er `git` en kommando-baseret app.
- Brugergrænseflade (UI). Nogle apps har grafiske brugergrænseflader (GUI'er), hvor du klikker på knapper, indtaster tekst, vælger muligheder og mere.

### Konsol- og UI-apps er begrænsede

Sammenlign det med en kommando-baseret app, hvor du skriver en kommando:

- **Det er begrænset**. Du kan ikke bare skrive enhver kommando, kun dem appen understøtter.
- **Sprog-specifik**. Nogle apps understøtter mange sprog, men som standard er appen bygget til et bestemt sprog, selvom du kan tilføje mere sprogsupport.

### Fordele ved tekstgenereringsapps

Hvordan er en tekstgenereringsapp så anderledes?

I en tekstgenereringsapp har du mere fleksibilitet, du er ikke begrænset til et sæt af kommandoer eller et bestemt input-sprog. I stedet kan du bruge naturligt sprog til at interagere med appen. En anden fordel er, at du allerede interagerer med en datakilde, der er trænet på et stort korpus af information, hvorimod en traditionel app måske er begrænset til, hvad der er i en database.

### Hvad kan jeg bygge med en tekstgenereringsapp?

Der er mange ting, du kan bygge. For eksempel:

- **En chatbot**. En chatbot, der besvarer spørgsmål om emner som dit firma og dets produkter, kunne være et godt match.
- **Hjælpere**. LLM'er er gode til ting som at opsummere tekst, få indsigt fra tekst, producere tekst som CV'er og mere.
- **Kodeassistent**. Afhængig af det sprogmodel, du bruger, kan du bygge en kodeassistent, der hjælper dig med at skrive kode. For eksempel kan du bruge et produkt som GitHub Copilot samt ChatGPT til at hjælpe dig med at skrive kode.

## Hvordan kommer jeg i gang?

Nå, du skal finde en måde at integrere med en LLM, hvilket normalt indebærer følgende to tilgange:

- Brug en API. Her konstruerer du webanmodninger med din prompt og får genereret tekst tilbage.
- Brug et bibliotek. Biblioteker hjælper med at indkapsle API-kald og gøre dem nemmere at bruge.

## Biblioteker/SDK'er

Der er nogle få velkendte biblioteker til at arbejde med LLM'er som:

- **openai**, dette bibliotek gør det nemt at forbinde til din model og sende prompts ind.

Derudover er der biblioteker, der arbejder på et højere niveau som:

- **Langchain**. Langchain er velkendt og understøtter Python.
- **Semantic Kernel**. Semantic Kernel er et bibliotek fra Microsoft, der understøtter sprogene C#, Python og Java.

## Første app med openai

Lad os se, hvordan vi kan bygge vores første app, hvilke biblioteker vi har brug for, hvor meget der kræves og så videre.

### Installer openai

Der findes mange biblioteker til interaktion med OpenAI eller Azure OpenAI. Det er muligt at bruge mange programmeringssprog også som C#, Python, JavaScript, Java og mere. Vi har valgt at bruge `openai` Python-biblioteket, så vi vil bruge `pip` til at installere det.

```bash
pip install openai
```

### Opret en ressource

Du skal udføre følgende trin:

- Opret en konto på Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Få adgang til Azure OpenAI. Gå til [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) og anmod om adgang.

  > [!NOTE]
  > På tidspunktet for skrivningen skal du søge om adgang til Azure OpenAI.

- Installer Python <https://www.python.org/>
- Har oprettet en Azure OpenAI Service-ressource. Se denne vejledning for hvordan man [opretter en ressource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Find API-nøgle og endepunkt

På dette tidspunkt skal du fortælle dit `openai` bibliotek, hvilken API-nøgle det skal bruge. For at finde din API-nøgle, gå til "Keys and Endpoint" sektionen på din Azure OpenAI-ressource og kopier "Nøgle 1" værdien.

![Nøgler og Endepunkt ressourceblade i Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nu hvor du har denne information kopieret, lad os instruere bibliotekerne til at bruge den.

> [!NOTE]
> Det er værd at holde din API-nøgle adskilt fra din kode. Det kan du gøre ved at bruge miljøvariabler.
>
> - Sæt miljøvariablen `OPENAI_API_KEY` til din API-nøgle.
>   `export OPENAI_API_KEY='sk-...'`

### Konfigurer Azure

Hvis du bruger Azure OpenAI (nu en del af Microsoft Foundry), her er hvordan du sætter konfiguration op. Vi bruger standard `OpenAI` klienten rettet mod Azure OpenAI `/openai/v1/` endepunktet, som virker med Responses API og kræver ingen `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Ovenfor sætter vi følgende:

- `api_key`, dette er din API-nøgle fundet i Azure-portalen eller Microsoft Foundry-portalen.
- `base_url`, dette er dit Foundry-ressourceendepunkt med `/openai/v1/` tilføjet. Det stabile v1-endepunkt fungerer på tværs af OpenAI og Azure OpenAI uden nogen `api_version` styring.

> [!NOTE] > `os.environ` læser miljøvariabler. Du kan bruge det til at læse miljøvariabler som `AZURE_OPENAI_API_KEY` og `AZURE_OPENAI_ENDPOINT`. Sæt disse miljøvariabler i din terminal eller ved at bruge et bibliotek som `dotenv`.

## Generer tekst

Måden at generere tekst på er ved at bruge Responses API via `responses.create` metoden. Her er et eksempel:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

I koden ovenfor opretter vi et svar og sender modellen, vi vil bruge, og prompten ind. Så printer vi den genererede tekst via `response.output_text`.

### Multi-turn samtaler

Responses API er velegnet til både enkelt-generering og multi-turn chatbots - du leverer en liste af beskeder i `input` for at opbygge en samtale:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Mere om denne funktionalitet i et kommende kapitel.

## Øvelse - din første tekstgenereringsapp

Nu hvor vi har lært, hvordan man sætter openai op og konfigurerer det, er det tid til at bygge din første tekstgenereringsapp. For at bygge din app, følg disse trin:

1. Opret et virtuelt miljø og installer openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Hvis du bruger Windows, skriv `venv\Scripts\activate` i stedet for `source venv/bin/activate`.

   > [!NOTE]
   > Find din Azure OpenAI nøgle ved at gå til [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), søg efter `Open AI`, vælg `Open AI resource`, og derefter vælg `Keys and Endpoint` og kopier `Key 1` værdien.

1. Opret en _app.py_-fil og giv den følgende kode:

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
   > Hvis du bruger almindelig OpenAI (ikke Azure), brug `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (uden `base_url`) og angiv et modelnavn som `gpt-5-mini` i stedet for et deploymentsnavn.

   Du skulle se en output som følgende:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Forskellige typer af prompts til forskellige ting

Nu har du set, hvordan man genererer tekst ved hjælp af en prompt. Du har endda et program kørende, som du kan modificere og ændre for at generere forskellige typer tekst.

Prompts kan bruges til alle slags opgaver. For eksempel:

- **Generer en type tekst**. For eksempel kan du generere et digt, spørgsmål til en quiz osv.
- **Opslag af information**. Du kan bruge prompts til at søge information som for eksempel 'Hvad betyder CORS i webudvikling?'.
- **Generer kode**. Du kan bruge prompts til at generere kode, for eksempel udvikle et regulært udtryk til validering af e-mails eller hvorfor ikke generere et helt program, som en webapp?

## Et mere praktisk eksempel: en opskriftgenerator

Forestil dig, at du har ingredienser hjemme og vil lave mad. Til det har du brug for en opskrift. En måde at finde opskrifter på er at bruge en søgemaskine, eller du kunne bruge en LLM til det.

Du kunne skrive en prompt som denne:

> "Vis mig 5 opskrifter på en ret med følgende ingredienser: kylling, kartofler og gulerødder. For hver opskrift, list alle ingredienserne, der bruges"

Givet ovenstående prompt, kan du få et svar ligesom:

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

Dette resultat er godt, jeg ved hvad jeg skal lave. På dette punkt kunne nyttige forbedringer være:

- Filtrering af ingredienser, jeg ikke kan lide eller er allergisk overfor.
- Lav en indkøbsliste, hvis jeg ikke har alle ingredienserne hjemme.

For ovenstående tilfælde, lad os tilføje en ekstra prompt:

> "Fjern venligst opskrifter med hvidløg, da jeg er allergisk og erstat det med noget andet. Lav også en indkøbsliste for opskrifterne, da jeg allerede har kylling, kartofler og gulerødder hjemme."

Nu har du et nyt resultat, nemlig:

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

Det er dine fem opskrifter, uden hvidløg nævnt, og du har også en indkøbsliste under hensyn til, hvad du allerede har derhjemme.

## Øvelse - byg en opskriftgenerator

Nu hvor vi har afprøvet et scenarie, lad os skrive kode, der matcher det viste scenarie. Følg disse trin:

1. Brug den eksisterende _app.py_-fil som udgangspunkt
1. Find `prompt` variablen og ændr dens kode til følgende:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Hvis du nu kører koden, bør du se en output som ligner:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > BEMÆRK, din LLM er ikke deterministisk, så du kan få forskellige resultater hver gang du kører programmet.

   Fint, lad os se, hvordan vi kan forbedre tingene. For at forbedre tingene ønsker vi at gøre koden fleksibel, så både ingredienser og antal opskrifter kan forbedres og ændres.

1. Lad os ændre koden på følgende måde:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   At tage koden til en testkørsel kunne se sådan ud:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Forbedr ved at tilføje filter og indkøbsliste

Vi har nu en fungerende app der kan producere opskrifter, og den er fleksibel, da den baseres på input fra brugeren, både på antal opskrifter men også ingredienserne der bruges.

For at forbedre den yderligere, ønsker vi at tilføje følgende:

- **Filtrer ingredienser ud**. Vi vil kunne filtrere ingredienser, vi ikke kan lide eller er allergiske overfor. For at opnå denne ændring, kan vi redigere vores eksisterende prompt og tilføje en filterbetingelse til slutningen af den som følger:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ovenfor tilføjer vi `{filter}` til slutningen af prompten, og vi fanger også filterværdien fra brugeren.

  Et eksempelinput ved kørsel af programmet kunne nu se sådan ud:

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

  Som du kan se, er opskrifter med mælk i blevet filtreret ud. Men hvis du er laktoseintolerant, vil du måske også filtrere opskrifter med ost ud, så det er nødvendigt at være specifik.

- **Lav en indkøbsliste**. Vi vil lave en indkøbsliste, taget i betragtning hvad vi allerede har hjemme.

  Til denne funktionalitet kunne vi enten prøve at løse alt i én prompt eller vi kunne opdele det i to prompts. Lad os prøve den sidstnævnte tilgang. Her foreslår vi at tilføje en ekstra prompt, men for at det kan fungere, skal vi tilføje resultatet af den første prompt som kontekst til den anden prompt.

  Find delen i koden, der printer resultatet fra den første prompt, og tilføj følgende kode nedenunder:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Bemærk følgende:

  1. Vi konstruerer en ny prompt ved at tilføje resultatet fra den første prompt til den nye prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  2. Vi laver en ny anmodning, men tager også hensyn til antal tokens, vi bad om i den første prompt, så denne gang siger vi `max_output_tokens` er 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Når vi prøver denne kode, får vi nu følgende output:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Forbedr din opsætning

Hvad vi har indtil videre, er kode, der fungerer, men der er nogle justeringer, vi bør lave for at forbedre tingene yderligere. Nogle ting, vi bør gøre, er:

- **Adskil hemmeligheder fra kode**, som for eksempel API-nøglen. Hemmeligheder hører ikke hjemme i koden og bør gemmes et sikkert sted. For at adskille hemmeligheder fra koden kan vi bruge miljøvariabler og biblioteker som `python-dotenv` til at indlæse dem fra en fil. Sådan ville det se ud i koden:

  1. Opret en `.env` fil med følgende indhold:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Bemærk, for Azure OpenAI i Microsoft Foundry skal du i stedet sætte følgende miljøvariabler:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     I koden vil du indlæse miljøvariablerne sådan her:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Et ord om token-længde**. Vi bør overveje, hvor mange tokens vi har brug for til at generere den tekst, vi ønsker. Tokens koster penge, så hvor muligt bør vi prøve at være økonomiske med antallet af tokens, vi bruger. Kan vi for eksempel formulere prompten, så vi kan bruge færre tokens?

  For at ændre de tokens der bruges, kan du bruge parameteren `max_output_tokens`. Hvis du for eksempel vil bruge 100 tokens, ville du gøre:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimentér med temperatur**. Temperatur er noget, vi ikke har nævnt indtil nu, men det er en vigtig sammenhæng til, hvordan vores program opfører sig. Jo højere temperaturværdi, jo mere tilfældig bliver outputtet. Omvendt: jo lavere temperaturværdi, jo mere forudsigeligt bliver outputtet. Overvej om du ønsker variation i dit output eller ej.

  For at ændre temperaturen kan du bruge parameteren `temperature`. Hvis du for eksempel vil bruge en temperatur på 0,5, ville du gøre:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Bemærk, jo tættere på 1.0, jo mere varieret bliver outputtet.

- **Årsagsmodeller bruger ikke `temperature`**. Dette er et vigtigt skift i 2026. De nuværende, ikke-deprecierede modeller på Microsoft Foundry er **årsagsmodeller** (GPT-5 familien, o-serien) - og de **understøtter ikke `temperature` eller `top_p`** (eller `max_tokens`; brug `max_output_tokens`). Hvis du sender `temperature` til `gpt-5-mini` får du en "parameter ikke understøttet" fejl. Så for at prøve temperatur-eksemplet ovenfor, skal du pege på en model, der stadig understøtter samplingkontroller - for eksempel en åben **Llama**-model som `Llama-3.3-70B-Instruct` fra [Microsoft Foundry modelkataloget](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), kaldt via Foundry Models / Azure AI Inference endpoint (på samme måde som `githubmodels-*` eksemplerne). For årsagsmodeller som GPT-5 styrer du output anderledes:
  - **Prompt engineering** - klare instruktioner, eksempler og struktureret output (se lektion [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) udfører det arbejde, som samplingknapperne plejede at gøre.
  - **Årsagskontroller** - parametre som reasoning effort/verbosity bytter dybde af ræsonnering mod latenstid og omkostninger.

  Kort sagt: `temperature`/`top_p` er stadig gyldige på mange modeller (Llama, Mistral, Phi og GPT-4.x familien - selvom GPT-4.x er ved at udfases), men retningen går mod prompt engineering + årsagskontroller på årsagsmodeller som GPT-5.

## Opgave

Til denne opgave kan du vælge, hvad du vil bygge.

Her er nogle forslag:

- Juster opskriftgenerator-appen for at forbedre den yderligere. Leg med temperaturværdier og prompts for at se, hvad du kan finde på.
- Byg en "studiebuddy". Denne app skal kunne besvare spørgsmål om et emne, for eksempel Python. Du kan have prompts som "Hvad er et bestemt emne i Python?" eller en prompt der siger, vis mig kode for et bestemt emne osv.
- Historie-bot, få historien til at leve, instruer botten om at spille en bestemt historisk karakter og spørg den om dens liv og tid.

## Løsning

### Studiebuddy

Nedenfor er en startprompt, se hvordan du kan bruge den og tilpasse den, som du vil.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historie-bot

Her er nogle prompts, du kan bruge:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Videnstest

Hvad gør begrebet temperatur?

1. Det styrer, hvor tilfældigt outputtet er.
1. Det styrer, hvor stor responsen er.
1. Det styrer, hvor mange tokens der bruges.

## 🚀 Udfordring

Når du arbejder på opgaven, prøv at variere temperaturen, prøv at sætte den til 0, 0,5 og 1. Husk at 0 er mindst varieret og 1 er mest. Hvilken værdi fungerer bedst for din app?

## Godt arbejde! Fortsæt din læring

Efter at have gennemført denne lektion, tjek vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at forbedre din viden om Generative AI!

Gå videre til Lektion 7, hvor vi vil se på, hvordan man [bygger chatapplikationer](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->