# Bygge tekstgenereringsapplikasjoner

[![Bygge tekstgenereringsapplikasjoner](../../../translated_images/no/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klikk på bildet over for å se video av denne leksjonen)_

Du har så langt sett gjennom dette pensumet at det finnes kjernenbegreper som prompt og til og med en hel disiplin kalt "prompt engineering". Mange verktøy du kan interagere med som ChatGPT, Office 365, Microsoft Power Platform og flere, støtter deg i å bruke prompts for å få til noe.

For at du skal kunne legge til en slik opplevelse i en app, må du forstå begreper som prompt, fullføringer og velge et bibliotek å jobbe med. Det er akkurat det du vil lære i dette kapittelet.

## Introduksjon

I dette kapitlet vil du:

- Lære om openai-biblioteket og dets kjernebegreper.
- Bygge en tekstgenereringsapp med openai.
- Forstå hvordan du bruker begreper som prompt, temperatur og tokens for å bygge en tekstgenereringsapp.

## Læringsmål

På slutten av denne leksjonen vil du kunne:

- Forklare hva en tekstgenereringsapp er.
- Bygge en tekstgenereringsapp ved hjelp av openai.
- Konfigurere appen din til å bruke flere eller færre tokens og også endre temperaturen for et variert resultat.

## Hva er en tekstgenereringsapp?

Normalt når du bygger en app har den en slags grensesnitt som følgende:

- Kommandobasert. Konsollapper er typiske apper hvor du skriver en kommando og den utfører en oppgave. For eksempel, `git` er en kommandobasert app.
- Brukergrensesnitt (UI). Noen apper har grafiske brukergrensesnitt (GUI) hvor du klikker på knapper, skriver inn tekst, velger alternativer og mer.

### Konsoll- og UI-apper er begrensede

Sammenlign det med en kommandobasert app der du skriver en kommando:

- **Den er begrenset**. Du kan ikke bare skrive hvilken som helst kommando, kun de som appen støtter.
- **Språkspesifikk**. Noen apper støtter mange språk, men som standard er appen bygget for et spesifikt språk, selv om du kan legge til mer språksupport.

### Fordeler med tekstgenereringsapper

Så hvordan er en tekstgenereringsapp annerledes?

I en tekstgenereringsapp har du mer fleksibilitet, du er ikke begrenset til et sett med kommandoer eller et spesifikt inndataspråk. I stedet kan du bruke naturlig språk til å interagere med appen. En annen fordel er at du allerede interagerer med en datakilde som er trent på et stort korpus av informasjon, mens en tradisjonell app kan være begrenset til det som er i en database.

### Hva kan jeg bygge med en tekstgenereringsapp?

Det er mange ting du kan bygge. For eksempel:

- **En chatbot**. En chatbot som svarer på spørsmål om temaer, som ditt selskap og dets produkter, kan være en god match.
- **Hjelper**. LLM-er er gode på ting som å oppsummere tekst, hente innsikt fra tekst, produsere tekst som CV-er og mer.
- **Kodeassistent**. Avhengig av språkmodellen du bruker, kan du bygge en kodeassistent som hjelper deg å skrive kode. For eksempel kan du bruke et produkt som GitHub Copilot så vel som ChatGPT for å hjelpe deg å skrive kode.

## Hvordan kan jeg komme i gang?

Vel, du må finne en måte å integrere med en LLM som vanligvis innebærer følgende to tilnærminger:

- Bruke en API. Her konstruerer du webforespørsler med din prompt og får generert tekst tilbake.
- Bruke et bibliotek. Biblioteker hjelper med å kapsle inn API-kall og gjøre dem lettere å bruke.

## Biblioteker/SDK-er

Det finnes noen få godt kjente biblioteker for å jobbe med LLM-er som:

- **openai**, dette biblioteket gjør det enkelt å koble til modellen din og sende inn prompts.

Så finnes det biblioteker som opererer på et høyere nivå som:

- **Langchain**. Langchain er godt kjent og støtter Python.
- **Semantic Kernel**. Semantic Kernel er et bibliotek fra Microsoft som støtter språkene C#, Python og Java.

## Første app med openai

La oss se hvordan vi kan bygge vår første app, hvilke biblioteker vi trenger, hvor mye som kreves og så videre.

### Installer openai

Det finnes mange biblioteker der ute for å interagere med OpenAI eller Azure OpenAI. Det er også mulig å bruke mange programmeringsspråk som C#, Python, JavaScript, Java og mer. Vi har valgt å bruke `openai` Python-biblioteket, så vi bruker `pip` for å installere det.

```bash
pip install openai
```

### Opprett en ressurs

Du må utføre følgende steg:

- Opprett en konto på Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Få tilgang til Azure OpenAI. Gå til [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) og søk om tilgang.

  > [!NOTE]
  > På tidspunktet for skriving må du søke om tilgang til Azure OpenAI.

- Installer Python <https://www.python.org/>
- Har opprettet en Azure OpenAI Service-ressurs. Se denne veiledningen for hvordan du [oppretter en ressurs](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Finn API-nøkkel og endepunkt

På dette tidspunktet må du fortelle `openai`-biblioteket hvilket API-nøkkel som skal brukes. For å finne API-nøkkelen din, gå til "Nøkler og endepunkt"-delen av Azure OpenAI-ressursen din og kopier "Nøkkel 1"-verdien.

![Nøkler og endepunkt ressursblad i Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nå som du har kopiert denne informasjonen, la oss instruere bibliotekene til å bruke den.

> [!NOTE]
> Det er verdt å skille API-nøkkelen fra koden din. Du kan gjøre det ved å bruke miljøvariabler.
>
> - Sett miljøvariabelen `OPENAI_API_KEY` til din API-nøkkel.
>   `export OPENAI_API_KEY='sk-...'`

### Sett opp konfigurering for Azure

Hvis du bruker Azure OpenAI (nå en del av Microsoft Foundry), her er hvordan du setter opp konfigurasjonen. Vi bruker standard `OpenAI` klient som peker på Azure OpenAI `/openai/v1/` endepunkt, som fungerer med Responses API og trenger ingen `api_version`:

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
- `base_url`, dette er ditt Foundry-ressursendepunkt med `/openai/v1/` lagt til. Det stabile v1-endepunktet fungerer på tvers av OpenAI og Azure OpenAI uten `api_version`-administrasjon.

> [!NOTE] > `os.environ` leser miljøvariabler. Du kan bruke den til å lese miljøvariabler som `AZURE_OPENAI_API_KEY` og `AZURE_OPENAI_ENDPOINT`. Sett disse miljøvariablene i terminalen din eller ved å bruke et bibliotek som `dotenv`.

## Generer tekst

Måten å generere tekst på er å bruke Responses API via `responses.create` metoden. Her er et eksempel:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

I koden over oppretter vi et svar og sender inn modellen vi vil bruke og prompten. Så skriver vi ut den genererte teksten via `response.output_text`.

### Flere-runde-samtaler

Responses API er godt egnet både for enkelt-runde tekstgenerering og flerrerunde-chatboter - du gir en liste av meldinger i `input` for å bygge opp en samtale:

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
   > Finn din Azure OpenAI-nøkkel ved å gå til [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) og søk etter `Open AI` og velg `Open AI resource` og deretter velg `Keys and Endpoint` og kopier `Key 1`-verdien.

1. Lag en _app.py_-fil og gi den følgende kode:

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
   > Hvis du bruker vanlig OpenAI (ikke Azure), bruk `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (ingen `base_url`) og oppgi et modellnavn som `gpt-5-mini` i stedet for et distribusjonsnavn.

   Du bør se et resultat som følgende:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Ulike typer prompts, for ulike ting

Nå har du sett hvordan man genererer tekst ved bruk av en prompt. Du har til og med et program som kjører som du kan endre og modifisere for å generere ulike typer tekst.

Prompts kan brukes til alle slags oppgaver. For eksempel:

- **Generere en type tekst**. Du kan for eksempel generere et dikt, spørsmål til en quiz osv.
- **Søke opp informasjon**. Du kan bruke prompts for å lete etter informasjon som i eksemplet 'Hva betyr CORS i webutvikling?'.
- **Generere kode**. Du kan bruke prompts for å generere kode, for eksempel utvikle et regulært uttrykk brukt til å validere e-poster eller hvorfor ikke generere et helt program, som en webapp?

## En mer praktisk brukstilfelle: en oppskriftsgenerator

Forestill deg at du har ingredienser hjemme og ønsker å lage noe. For det trenger du en oppskrift. En måte å finne oppskrifter på er å bruke en søkemotor eller du kan bruke en LLM for å gjøre det.

Du kunne skrevet en prompt slik:

> "Vis meg 5 oppskrifter for en rett med følgende ingredienser: kylling, poteter og gulrøtter. For hver oppskrift, list opp alle ingrediensene som brukes"

Med den ovennevnte prompten kan du få et svar som ligner på:

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

Dette utfallet er flott, jeg vet hva jeg skal lage. På dette punktet kan nyttige forbedringer være:

- Filtrere ut ingredienser jeg ikke liker eller er allergisk mot.
- Lage en handleliste, i tilfelle jeg ikke har alle ingrediensene hjemme.

For de ovennevnte tilfellene, la oss legge til en ekstra prompt:

> "Vennligst fjern oppskrifter med hvitløk da jeg er allergisk, og erstatt det med noe annet. Lag også en handleliste for oppskriftene, med tanke på at jeg allerede har kylling, poteter og gulrøtter hjemme."

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

Det er dine fem oppskrifter, uten hvitløk nevnt og du har også en handleliste som tar hensyn til hva du allerede har hjemme.

## Øvelse - bygg en oppskriftsgenerator

Nå som vi har spilt ut et scenario, la oss skrive kode som matcher det demonstrerte scenarioet. For å gjøre det, følg disse trinnene:

1. Bruk den eksisterende _app.py_-filen som utgangspunkt
1. Finn variabelen `prompt` og endre koden til følgende:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Hvis du nå kjører koden, bør du se et resultat som ligner:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > MERK: Din LLM er ikke-deterministisk, så du kan få forskjellige resultater hver gang du kjører programmet.

   Flott, la oss se hvordan vi kan forbedre ting. For å forbedre ting, ønsker vi å sikre at koden er fleksibel, slik at ingredienser og antall oppskrifter kan forbedres og endres.

1. La oss endre koden på følgende måte:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Å ta koden for en prøvetur kan se slik ut:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Forbedre ved å legge til filter og handleliste

Vi har nå en fungerende app som kan produsere oppskrifter og den er fleksibel siden den baserer seg på inndata fra brukeren, både på antall oppskrifter men også ingrediensene som brukes.

For ytterligere forbedring vil vi legge til følgende:

- **Filtrer ut ingredienser**. Vi ønsker å kunne filtrere ut ingredienser vi ikke liker eller er allergiske mot. For å oppnå denne endringen kan vi redigere vår eksisterende prompt og legge til en filterbetingelse på slutten av den slik:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ovenfor legger vi til `{filter}` på slutten av prompten og vi fanger også filterverdien fra brukeren.

  Et eksempel på inndata ved kjøring av programmet kan nå se slik ut:

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

  Som du ser er alle oppskrifter med melk filtrert ut. Men, hvis du er laktoseintolerant, vil du kanskje også filtrere ut oppskrifter med ost, så det er behov for å være tydelig.

- **Produsere en handleliste**. Vi ønsker å produsere en handleliste med tanke på hva vi allerede har hjemme.

  For denne funksjonaliteten kunne vi enten prøve å løse alt i én prompt eller splitte det opp i to prompts. La oss prøve det siste. Her foreslår vi å legge til en ekstra prompt, men for at det skal fungere må vi legge resultatet fra den første prompten som kontekst til den siste prompten.

  Finn delen i koden som skriver ut resultatet fra første prompt og legg til følgende kode nedenfor:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Merk følgende:

  1. Vi bygger en ny prompt ved å legge resultatet fra første prompt til den nye prompten:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Vi lager en ny forespørsel, men også med tanke på antall tokens vi ba om i første prompt, så denne gangen sier vi at `max_output_tokens` er 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Når vi prøver denne koden, får vi nå følgende utskrift:

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

Det vi har så langt er kode som fungerer, men det er noen justeringer vi bør gjøre for å forbedre ting videre. Noen ting vi bør gjøre er:

- **Skill hemmeligheter fra koden**, som API-nøkkelen. Hemmeligheter hører ikke hjemme i koden og bør lagres på et sikkert sted. For å skille hemmeligheter fra koden, kan vi bruke miljøvariabler og biblioteker som `python-dotenv` for å laste dem inn fra en fil. Slik vil det se ut i kode:

  1. Lag en `.env`-fil med følgende innhold:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Merk, for Azure OpenAI i Microsoft Foundry, må du sette følgende miljøvariabler i stedet:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     I koden vil du laste miljøvariablene slik:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Et ord om token-lengde**. Vi bør vurdere hvor mange tokens vi trenger for å generere teksten vi ønsker. Tokens koster penger, så der det er mulig bør vi prøve å være økonomiske med antall tokens vi bruker. Kan vi for eksempel formulere prompten slik at vi bruker færre tokens?

  For å endre antall tokens som brukes, kan du bruke parameteren `max_output_tokens`. For eksempel, hvis du vil bruke 100 tokens, gjør du:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimenter med temperatur**. Temperatur er noe vi ikke har nevnt så langt, men det er en viktig kontekst for hvordan programmet vårt fungerer. Jo høyere temperaturverdi, jo mer tilfeldig blir utdataene. Jo lavere temperaturverdi, jo mer forutsigbar blir utdataene. Vurder om du ønsker variasjon i utdataene eller ikke.

  For å endre temperaturen kan du bruke parameteren `temperature`. For eksempel, hvis du vil bruke en temperatur på 0,5, gjør du:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Merk, jo nærmere 1.0, jo mer varierte blir utdataene.

- **Reasoning-modeller bruker ikke `temperature`**. Dette er et viktig skifte i 2026. De nåværende, ikke-avskrevne modellene i Microsoft Foundry er **reasoning-modeller** (GPT-5-familien, o-serien) - og de **støtter ikke `temperature` eller `top_p`** (ikke heller `max_tokens`; bruk `max_output_tokens`). Hvis du sender `temperature` til `gpt-5-mini` vil du få en "parameter ikke støttet"-feil. Så for å prøve temperatur-eksemplet ovenfor, pek til en modell som fortsatt støtter sampling-kontroller - for eksempel en åpen **Llama**-modell som `Llama-3.3-70B-Instruct` fra [Microsoft Foundry modellkatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), kalt via Foundry Models / Azure AI Inference-endepunktet (samme måte som `githubmodels-*`-eksemplene). For reasoning-modeller som GPT-5, styrer du utdata på en annen måte:
  - **Prompt engineering** - klare instruksjoner, eksempler og strukturert output (se leksjon [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) gjør jobben som sampling-kontroller pleide å gjøre.
  - **Reasoning-kontroller** - parametere som reasoning effort/verbosity bytter dybde i resonnement mot ventetid og kostnad.

  Kort fortalt: `temperature`/`top_p` er fortsatt gyldige på mange modeller (Llama, Mistral, Phi, og GPT-4.x-familien - selv om GPT-4.x fases ut), men retningen går mot prompt engineering + reasoning-kontroller på reasoning-modeller som GPT-5.

## Oppgave

For denne oppgaven kan du velge hva du vil bygge.

Her er noen forslag:

- Juster oppskriftsgenerator-appen for å forbedre den ytterligere. Lek med temperaturverdier og promptene for å se hva du kan komme opp med.
- Bygg en "studievenn". Denne appen skal kunne svare på spørsmål om et emne, for eksempel Python. Du kan ha prompts som "Hva er et bestemt tema i Python?" eller en prompt som sier, vis meg kode for et bestemt tema osv.
- Historie-bot, få historien til å leve, instruer boten til å spille en bestemt historisk figur og still den spørsmål om livet og tiden til denne personen.

## Løsning

### Studievenn

Under er en startprompt, se hvordan du kan bruke den og justere den etter din smak.

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

1. Det kontrollerer hvor tilfeldig utdataene er.
1. Det kontrollerer hvor stort svaret er.
1. Det kontrollerer hvor mange tokens som brukes.

## 🚀 Utfordring

Når du jobber med oppgaven, prøv å variere temperaturen, prøv å sette den til 0, 0,5 og 1. Husk at 0 er minst variert og 1 er mest variert. Hvilken verdi fungerer best for appen din?

## Flott arbeid! Fortsett å lære

Etter å ha fullført denne leksjonen, sjekk ut vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for å fortsette å heve dine kunnskaper om Generativ AI!

Gå videre til Lekse 7 hvor vi skal se på hvordan du kan [bygge chatteapplikasjoner](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->