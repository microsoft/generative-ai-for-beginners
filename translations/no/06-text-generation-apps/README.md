# Bygge applikasjoner for tekstgenerering

[![Bygge applikasjoner for tekstgenerering](../../../translated_images/no/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klikk på bildet over for å se video av denne leksjonen)_

Du har så langt sett gjennom dette pensum at det finnes kjernebegreper som prompts og til og med en hel disiplin kalt «prompt engineering». Mange verktøy du kan interagere med som ChatGPT, Office 365, Microsoft Power Platform og mer, støtter deg i å bruke prompts for å oppnå noe.

For at du skal kunne legge til en slik opplevelse i en app, må du forstå konsepter som prompts, fullføringer og velge et bibliotek å jobbe med. Det er akkurat det du vil lære i dette kapittelet.

## Introduksjon

I dette kapittelet vil du:

- Lære om openai-biblioteket og dets kjernebegreper.
- Bygge en app for tekstgenerering ved bruk av openai.
- Forstå hvordan man bruker konsepter som prompt, temperatur og tokens for å bygge en app for tekstgenerering.

## Læringsmål

På slutten av denne leksjonen vil du kunne:

- Forklare hva en app for tekstgenerering er.
- Bygge en app for tekstgenerering ved bruk av openai.
- Konfigurere appen din til å bruke flere eller færre tokens og også endre temperaturen for variert output.

## Hva er en app for tekstgenerering?

Normalt når du bygger en app har den en form for grensesnitt som følgende:

- Kommando-basert. Konsollapper er typiske apper der du skriver inn en kommando og den utfører en oppgave. For eksempel er `git` en kommando-basert app.
- Brukergrensesnitt (UI). Noen apper har grafiske brukergrensesnitt (GUI) hvor du klikker på knapper, skriver inn tekst, velger alternativer og mer.

### Konsoll- og UI-apper har begrensninger

Sammenlign det med en kommando-basert app hvor du skriver en kommando:

- **Den er begrenset**. Du kan ikke bare skrive hvilken som helst kommando, bare de appen støtter.
- **Språkspesifikk**. Noen apper støtter mange språk, men som standard er appen bygget for et bestemt språk, selv om du kan legge til mer språksupport.

### Fordeler med apper for tekstgenerering

Så hvordan er en app for tekstgenerering annerledes?

I en tekstgenereringsapp har du mer fleksibilitet, du er ikke begrenset til et sett av kommandoer eller et spesifikt inndata-språk. I stedet kan du bruke naturlig språk for å samhandle med appen. En annen fordel er at du allerede samhandler med en datakilde som er trent på et enormt korpus av informasjon, mens en tradisjonell app kan være begrenset av hva som er i en database.

### Hva kan jeg bygge med en tekstgenereringsapp?

Det er mange ting du kan bygge. For eksempel:

- **En chatbot**. En chatbot som svarer på spørsmål om temaer, som firmaet ditt og produktene kan være en god match.
- **Hjelper**. LLM-er er flinke til ting som å oppsummere tekst, hente innsikt fra tekst, produsere tekst som CV-er og mer.
- **Kodeassistent**. Avhengig av språkmodellen du bruker, kan du bygge en kodeassistent som hjelper deg å skrive kode. For eksempel kan du bruke produkter som GitHub Copilot samt ChatGPT for å hjelpe deg skrive kode.

## Hvordan komme i gang?

Vel, du må finne en måte å integrere med en LLM som vanligvis innebærer de to følgende tilnærmingene:

- Bruke en API. Her konstruerer du webforespørsler med prompten din og får tilbake generert tekst.
- Bruke et bibliotek. Biblioteker hjelper med å innkapsle API-kallene og gjøre dem enklere å bruke.

## Biblioteker/SDK-er

Det finnes noen få kjente biblioteker for å jobbe med LLM-er som:

- **openai**, dette biblioteket gjør det enkelt å koble til modellen din og sende inn prompts.

Så finnes det biblioteker som opererer på et høyere nivå, som:

- **Langchain**. Langchain er velkjent og støtter Python.
- **Semantic Kernel**. Semantic Kernel er et bibliotek fra Microsoft som støtter språkene C#, Python og Java.

## Første app med openai

La oss se hvordan vi kan bygge vår første app, hvilke biblioteker vi trenger, hvor mye det kreves og så videre.

### Installer openai

Det finnes mange biblioteker for å samhandle med OpenAI eller Azure OpenAI. Det er mulig å bruke flere programmeringsspråk også som C#, Python, JavaScript, Java og mer. Vi har valgt å bruke `openai` Python-biblioteket, så vi vil bruke `pip` for å installere det.

```bash
pip install openai
```

### Opprett en ressurs

Du må utføre følgende trinn:

- Opprett en konto på Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Få tilgang til Azure OpenAI. Gå til [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) og be om tilgang.

  > [!NOTE]
  > På tidspunktet for skriving må du søke om tilgang til Azure OpenAI.

- Installer Python <https://www.python.org/>
- Har opprettet en Azure OpenAI Service-ressurs. Se denne veiledningen for hvordan du [oppretter en ressurs](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Finn API-nøkkel og endepunkt

På dette tidspunktet må du fortelle `openai`-biblioteket hvilket API-nøkkel som skal brukes. For å finne API-nøkkelen din, gå til delen "Keys and Endpoint" for din Azure OpenAI-ressurs og kopier verdien for "Key 1".

![Nøkler og Endepunkt ressursområde i Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nå som du har kopiert denne informasjonen, la oss instruere bibliotekene til å bruke den.

> [!NOTE]
> Det anbefales å holde API-nøkkelen adskilt fra koden din. Du kan gjøre dette ved å bruke miljøvariabler.
>
> - Sett miljøvariabelen `OPENAI_API_KEY` til API-nøkkelen din.
>   `export OPENAI_API_KEY='sk-...'`

### Konfigurer Azure

Hvis du bruker Azure OpenAI (nå en del av Microsoft Foundry), her er hvordan du setter opp konfigurasjonen. Vi bruker standard `OpenAI` klient med endepunktet `/openai/v1/` fra Azure OpenAI, som fungerer med Responses API og krever ingen `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Ovenfor setter vi følgende:

- `api_key`, dette er API-nøkkelen din funnet i Azure-portalen eller Microsoft Foundry-portalen.
- `base_url`, dette er Foundry-ressursens endepunkt med `/openai/v1/` lagt til. Stabil v1-endepunkt fungerer på tvers av OpenAI og Azure OpenAI uten `api_version`-håndtering.

> [!NOTE] > `os.environ` leser miljøvariabler. Du kan bruke det til å lese miljøvariabler som `AZURE_OPENAI_API_KEY` og `AZURE_OPENAI_ENDPOINT`. Sett disse miljøvariablene i terminalen din eller ved å bruke et bibliotek som `dotenv`.

## Generer tekst

Måten å generere tekst på er å bruke Responses API via metoden `responses.create`. Her er et eksempel:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # dette er navnet på modellutrullingen din
    input=prompt,
    store=False,
)
print(response.output_text)
```

I koden ovenfor lager vi et svar og sender inn modellen vi ønsker å bruke og prompten. Så skriver vi ut den genererte teksten via `response.output_text`.

### Samtaler med flere runder

Responses API er godt egnet for både enkelt-runds tekstgenerering og fler-runds chatboter – du gir en liste av meldinger i `input` for å bygge opp en samtale:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Mer om denne funksjonaliteten i et kommende kapittel.

## Øvelse - din første tekstgenereringsapp

Nå som vi har lært hvordan vi setter opp og konfigurerer openai, er det på tide å bygge din første tekstgenereringsapp. For å bygge appen din, følg disse trinnene:

1. Opprett et virtuelt miljø og installer openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Hvis du bruker Windows, skriv `venv\Scripts\activate` i stedet for `source venv/bin/activate`.

   > [!NOTE]
   > Finn din Azure OpenAI-nøkkel ved å gå til [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) og søk etter `Open AI`, velg `Open AI-ressursen` og deretter `Keys and Endpoint` og kopier verdien til `Key 1`.

1. Opprett en fil kalt _app.py_ og gi den følgende kode:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # legg til din fullføringskode
   prompt = "Complete the following: Once upon a time there was a"

   # gjør en forespørsel ved å bruke Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # skriv ut svar
   print(response.output_text)
   ```

   > [!NOTE]
   > Hvis du bruker ren OpenAI (ikke Azure), bruk `client = OpenAI(api_key="<erstatt denne verdien med din OpenAI-nøkkel>")` (ingen `base_url`) og send en modellnavn som `gpt-5-mini` i stedet for et distribusjonsnavn.

   Du bør se en output som følgende:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Ulike typer prompts, for forskjellige ting

Nå har du sett hvordan man kan generere tekst ved å bruke en prompt. Du har til og med et program som kjører som du kan modifisere og endre for å generere ulike typer tekst.

Prompts kan brukes for alle slags oppgaver. For eksempel:

- **Generere en type tekst**. For eksempel, du kan generere et dikt, spørsmål til en quiz osv.
- **Slå opp informasjon**. Du kan bruke prompts for å søke informasjon som i følgende eksempel 'Hva betyr CORS i webutvikling?'.
- **Generere kode**. Du kan bruke prompts for å generere kode, for eksempel utvikle et regulært uttrykk brukt til å validere e-postadresser eller hvorfor ikke generere et helt program, som en webapp?

## Et mer praktisk brukstilfelle: en oppskriftsgenerator

Forestill deg at du har ingredienser hjemme og vil lage noe å spise. For det trenger du en oppskrift. En måte å finne oppskrifter på er å bruke en søkemotor eller du kan bruke en LLM til det.

Du kan skrive en prompt slik:

> «Vis meg 5 oppskrifter for en rett med følgende ingredienser: kylling, poteter og gulrøtter. List opp alle ingrediensene brukt per oppskrift»

Med den overstående prompten kan du få et svar som ligner på:

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

Dette resultatet er flott, jeg vet hva jeg skal lage. På dette punktet kan nyttige forbedringer være:

- Filtrere ut ingredienser som jeg ikke liker eller er allergisk mot.
- Lage en handleliste, i tilfelle jeg ikke har alle ingrediensene hjemme.

For de overstående tilfellene, la oss legge til en ekstra prompt:

> «Vennligst fjern oppskrifter med hvitløk da jeg er allergisk, og erstatt det med noe annet. Lag også en handleliste for oppskriftene, med tanke på at jeg allerede har kylling, poteter og gulrøtter hjemme.»

Nå har du et nytt resultat, nemlig:

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

Det er dine fem oppskrifter, uten hvitløk nevnt og du har også en handleliste med tanke på det du allerede har hjemme.

## Øvelse - bygg en oppskriftsgenerator

Nå som vi har spilt ut et scenario, la oss skrive kode som matcher det viste scenarioet. Følg disse trinnene:

1. Bruk den eksisterende _app.py_-filen som utgangspunkt
1. Finn variabelen `prompt` og bytt ut koden til følgende:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Hvis du nå kjører koden, bør du se en output som ligner på:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > MERK, din LLM er ikke deterministisk, så du kan få forskjellige resultater hver gang du kjører programmet.

   Flott, la oss se hvordan vi kan forbedre ting. For å forbedre ting, vil vi sørge for at koden er fleksibel, slik at ingrediensene og antall oppskrifter kan forbedres og endres.

1. La oss endre koden på følgende måte:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpoler antall oppskrifter inn i beskjeden og ingrediensene
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Å kjøre koden for en test kan se slik ut:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Forbedre ved å legge til filter og handleliste

Vi har nå en fungerende app som kan produsere oppskrifter, og den er fleksibel siden den baserer seg på input fra brukeren, både på antall oppskrifter og ingrediensene som brukes.

For å forbedre den ytterligere vil vi legge til følgende:

- **Filtrere ut ingredienser**. Vi ønsker å kunne filtrere ut ingredienser vi ikke liker eller som vi er allergiske mot. For å oppnå denne endringen kan vi redigere eksisterende prompt og legge til en filterbetingelse på slutten, slik:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ovenfor legger vi til `{filter}` på slutten av prompten, og vi tar også inn filterverdien fra brukeren.

  Et eksempel på inndata når programmet kjøres kan nå se slik ut:

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

  Som du ser, er alle oppskrifter som inneholder melk filtrert ut. Men hvis du er laktoseintolerant, vil du kanskje filtrere ut oppskrifter med ost også, så det er behov for tydelighet.


- **Lag en handleliste**. Vi ønsker å lage en handleliste, med tanke på hva vi allerede har hjemme.

  For denne funksjonaliteten kunne vi enten prøvd å løse alt i ett prompt eller vi kunne delt det opp i to prompts. La oss prøve det siste. Her foreslår vi å legge til et ekstra prompt, men for at det skal fungere, må vi legge resultatet fra det første promptet som kontekst til det andre promptet.

  Finn delen i koden som skriver ut resultatet fra det første promptet og legg til følgende kode under:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # skriv ut svar
  print("Shopping list:")
  print(response.output_text)
  ```

  Merk følgende:

  1. Vi bygger et nytt prompt ved å legge til resultatet fra det første promptet på det nye promptet:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Vi lager en ny forespørsel, men tar også hensyn til antall tokens vi ba om i første prompt, så denne gangen sier vi at `max_output_tokens` er 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Når vi kjører denne koden, får vi nå følgende utskrift:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Forbedre oppsettet ditt

Det vi har så langt er kode som fungerer, men det er noen justeringer vi bør gjøre for å forbedre ting ytterligere. Noe av det vi bør gjøre er:

- **Skill hemmeligheter fra kode**, som API-nøkkelen. Hemmeligheter hører ikke hjemme i koden og bør lagres på et sikkert sted. For å skille hemmeligheter fra kode kan vi bruke miljøvariabler og biblioteker som `python-dotenv` for å laste dem fra en fil. Slik kan det se ut i kode:

  1. Lag en `.env`-fil med følgende innhold:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Merk, for Azure OpenAI i Microsoft Foundry må du sette følgende miljøvariabler i stedet:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     I kode kan du laste miljøvariablene slik:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Et ord om token-lengde**. Vi bør vurdere hvor mange tokens vi trenger for å generere teksten vi ønsker. Tokens koster penger, så der det er mulig bør vi være økonomiske med antall tokens vi bruker. Kan vi for eksempel formulere prompten slik at vi kan bruke færre tokens?

  For å endre antallet tokens som brukes, kan du bruke parameteren `max_output_tokens`. For eksempel, hvis du vil bruke 100 tokens, gjør du:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimentere med temperatur**. Temperatur er noe vi ikke har nevnt så langt, men det er en viktig faktor for hvordan programmet vårt oppfører seg. Jo høyere temperaturverdi, desto mer tilfeldig blir outputen. Omvendt, jo lavere temperaturverdi, desto mer forutsigbar blir outputen. Vurder om du ønsker variasjon i outputen din eller ikke.

  For å endre temperaturen kan du bruke parameteren `temperature`. For eksempel, hvis du vil bruke temperatur 0,5, gjør du:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Merk, jo nærmere 1,0, desto mer variert blir outputen.

- **Resonnerende modeller bruker ikke `temperature`**. Dette er en viktig endring i 2026. De nåværende, ikke-deprekerte modellene i Microsoft Foundry er **resonnerende modeller** (GPT-5-familien, o-serien) - og de **støtter ikke `temperature` eller `top_p`** (ikke heller `max_tokens`; bruk `max_output_tokens`). Hvis du sender `temperature` til `gpt-5-mini`, får du en "parameter ikke støttet"-feil. For å prøve temperatur-eksempelet ovenfor, pek på en modell som fortsatt støtter sampling-kontroller - for eksempel en åpen **Llama**-modell som `Llama-3.3-70B-Instruct` fra [Microsoft Foundry modellkatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), kalt via Foundry Models / Azure AI Inference-endepunktet (samme måte som `githubmodels-*`-eksemplene). For resonnementmodeller som GPT-5, styrer du output annerledes:
  - **Prompt engineering** - klare instruksjoner, eksempler og strukturert output (se leksjon [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) gjør jobben sampling-kontroller pleide å gjøre.
  - **Resonneringskontroller** - parametere som resonneringsinnsats/verbositet bytter dybde av resonnement mot forsinkelse og kostnad.

  Kort sagt: `temperature`/`top_p` er fortsatt gyldige på mange modeller (Llama, Mistral, Phi og GPT-4.x-familien - selv om GPT-4.x fases ut), men retningen går mot prompt engineering + resonneringskontroller på resonnementmodeller som GPT-5.

## Oppgave

For denne oppgaven kan du velge hva du vil bygge.

Her er noen forslag:

- Juster oppskriftgenerator-appen for å forbedre den ytterligere. Lek med temperaturverdier og promptene for å se hva du kommer opp med.
- Lag en "studiekompis". Denne appen bør kunne svare på spørsmål om et tema, for eksempel Python, du kan ha prompts som "Hva er et bestemt tema i Python?", eller du kan ha et prompt som sier, vis meg kode for et bestemt tema osv.
- Historie-bot, få historien til å leve, instruer boten til å spille en bestemt historisk person og still spørsmål om livet og tiden dens.

## Løsning

### Studiekompis

Nedenfor er et startprompt, se hvordan du kan bruke det og justere det etter eget ønske.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historie-bot

Her er noen prompts du kan bruke:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Kunnskapssjekk

Hva gjør konseptet temperatur?

1. Det kontrollerer hvor tilfeldig outputen er.
1. Det kontrollerer hvor stor responsen er.
1. Det kontrollerer hvor mange tokens som brukes.

## 🚀 Utfordring

Når du jobber med oppgaven, prøv å variere temperaturen, prøv å sette den til 0, 0,5 og 1. Husk at 0 er minst variert og 1 er mest. Hvilken verdi fungerer best for din app?

## Flott jobbet! Fortsett læringen din

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å utvikle din kunnskap om Generativ AI!

Gå til leksjon 7 hvor vi ser på hvordan man [bygger chat-applikasjoner](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->