# Het bouwen van tekstgeneratie-applicaties

[![Het bouwen van tekstgeneratie-applicaties](../../../translated_images/nl/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

Je hebt tot nu toe in deze leerroute gezien dat er kernconcepten zijn zoals prompts en zelfs een hele discipline genaamd "prompt engineering". Veel tools waarmee je kunt interacteren, zoals ChatGPT, Office 365, Microsoft Power Platform en meer, ondersteunen het gebruik van prompts om iets te bereiken.

Als je zo'n ervaring aan een app wilt toevoegen, moet je concepten zoals prompts en completions begrijpen en een bibliotheek kiezen om mee te werken. Dat is precies wat je in dit hoofdstuk zult leren.

## Introductie

In dit hoofdstuk ga je:

- Leren over de openai-bibliotheek en de kernconcepten ervan.
- Een tekstgeneratie-app bouwen met openai.
- Begrijpen hoe je concepten als prompt, temperatuur en tokens gebruikt om een tekstgeneratie-app te bouwen.

## Leerdoelen

Aan het einde van deze les kun je:

- Uitleggen wat een tekstgeneratie-app is.
- Een tekstgeneratie-app bouwen met openai.
- Je app configureren om meer of minder tokens te gebruiken en ook de temperatuur te wijzigen voor een gevarieerde output.

## Wat is een tekstgeneratie-app?

Normaal gesproken heeft een app die je bouwt een soort interface zoals de volgende:

- Op commando gebaseerd. Console-apps zijn typische apps waarbij je een commando typt en die een taak uitvoert. Bijvoorbeeld, `git` is een op commando gebaseerde app.
- Gebruikersinterface (UI). Sommige apps hebben grafische gebruikersinterfaces (GUIs) waar je op knoppen klikt, tekst invoert, opties selecteert en meer.

### Console- en UI-apps zijn beperkt

Vergelijk het met een op commando gebaseerde app waarbij je een commando typt:

- **Het is beperkt**. Je kunt niet zomaar elk commando typen, alleen de commando's die de app ondersteunt.
- **Taalgebonden**. Sommige apps ondersteunen veel talen, maar standaard is de app gebouwd voor een specifieke taal, ook al kun je vaak extra taalondersteuning toevoegen.

### Voordelen van tekstgeneratie-apps

Hoe verschilt een tekstgeneratie-app dan?

In een tekstgeneratie-app heb je meer flexibiliteit; je bent niet beperkt tot een set commando's of een specifieke invoertaal. In plaats daarvan kun je natuurlijke taal gebruiken om met de app te communiceren. Een ander voordeel is dat je al interactie hebt met een databron die getraind is op een enorme hoeveelheid informatie, terwijl een traditionele app vaak beperkt is tot wat er in een database staat.

### Wat kan ik bouwen met een tekstgeneratie-app?

Er zijn veel dingen die je kunt bouwen. Bijvoorbeeld:

- **Een chatbot**. Een chatbot die vragen beantwoordt over onderwerpen zoals je bedrijf en diens producten zou een goede match kunnen zijn.
- **Helper**. LLM's zijn uitstekend in zaken zoals het samenvatten van tekst, het verkrijgen van inzichten uit tekst, het produceren van tekst zoals cv's en meer.
- **Code-assistent**. Afhankelijk van het taalmodel dat je gebruikt, kun je een code-assistent bouwen die je helpt code te schrijven. Bijvoorbeeld kun je producten gebruiken zoals GitHub Copilot en ChatGPT om je code te helpen schrijven.

## Hoe kan ik beginnen?

Je moet een manier vinden om te integreren met een LLM, wat meestal neerkomt op de volgende twee benaderingen:

- Gebruik een API. Hierbij stel je webverzoeken samen met je prompt en krijg je de gegenereerde tekst terug.
- Gebruik een bibliotheek. Bibliotheken helpen de API-aanroepen te kapselen en maken ze makkelijker te gebruiken.

## Bibliotheken/SDK's

Er zijn een paar bekende bibliotheken om met LLM's te werken zoals:

- **openai**, deze bibliotheek maakt het makkelijk om je model te verbinden en prompts te versturen.

Vervolgens zijn er bibliotheken die op een hoger niveau opereren zoals:

- **Langchain**. Langchain is bekend en ondersteunt Python.
- **Semantic Kernel**. Semantic Kernel is een bibliotheek van Microsoft die de talen C#, Python en Java ondersteunt.

## Eerste app met openai

Laten we bekijken hoe we onze eerste app kunnen bouwen, welke bibliotheken we nodig hebben, hoeveel er vereist is enzovoort.

### Installeer openai

Er zijn veel bibliotheken om te communiceren met OpenAI of Azure OpenAI. Het is mogelijk om ook verschillende programmeertalen te gebruiken zoals C#, Python, JavaScript, Java en meer. Wij hebben gekozen om de `openai` Python-bibliotheek te gebruiken, dus we installeren die met `pip`.

```bash
pip install openai
```

### Maak een resource aan

Je moet de volgende stappen uitvoeren:

- Maak een account aan op Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Krijg toegang tot Azure OpenAI. Ga naar [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) en vraag toegang aan.

  > [!NOTE]
  > Ten tijde van schrijven moet je toegang aanvragen voor Azure OpenAI.

- Installeer Python <https://www.python.org/>
- Heb een Azure OpenAI Service resource aangemaakt. Zie deze gids voor het [aanmaken van een resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Zoek API-sleutel en endpoint

Op dit moment moet je aan je `openai` bibliotheek doorgeven welke API-sleutel te gebruiken. Om je API-sleutel te vinden, ga je naar het gedeelte "Keys and Endpoint" van je Azure OpenAI-resource en kopieer je de waarde van "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nu je deze informatie hebt gekopieerd, laten we de bibliotheken instrueren deze te gebruiken.

> [!NOTE]
> Het is verstandig je API-sleutel van je code te scheiden. Dat kun je doen door gebruik te maken van omgevingsvariabelen.
>
> - Stel de omgevingsvariabele `OPENAI_API_KEY` in op je API-sleutel.
>   `export OPENAI_API_KEY='sk-...'`

### Stel Azure-configuratie in

Als je Azure OpenAI (nu onderdeel van Microsoft Foundry) gebruikt, zo stel je de configuratie in. We gebruiken de standaard `OpenAI` client gericht op de Azure OpenAI `/openai/v1/` endpoint, die werkt met de Responses API en geen `api_version` nodig heeft:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Bovenstaande stelt het volgende in:

- `api_key`, dit is je API-sleutel gevonden in de Azure Portal of Microsoft Foundry portal.
- `base_url`, dit is je Foundry resource endpoint met `/openai/v1/` eraan toegevoegd. De stabiele v1 endpoint werkt over OpenAI en Azure OpenAI heen zonder `api_version`-beheer.

> [!NOTE] > `os.environ` leest omgevingsvariabelen. Je kunt het gebruiken om omgevingsvariabelen zoals `AZURE_OPENAI_API_KEY` en `AZURE_OPENAI_ENDPOINT` te lezen. Stel deze omgevingsvariabelen in je terminal in of gebruik een bibliotheek zoals `dotenv`.

## Tekst genereren

De manier om tekst te genereren is door de Responses API te gebruiken via de `responses.create` methode. Hier is een voorbeeld:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # dit is de naam van je modeluitrol
    input=prompt,
    store=False,
)
print(response.output_text)
```

In bovenstaande code maken we een response aan en geven het model door dat we willen gebruiken en de prompt. Daarna printen we de gegenereerde tekst via `response.output_text`.

### Conversaties met meerdere beurten

De Responses API is zeer geschikt voor zowel tekstgeneratie in één beurt als voor chatbots met meerdere beurten - je geeft een lijst met berichten in `input` mee om een gesprek op te bouwen:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Meer over deze functionaliteit in een aankomend hoofdstuk.

## Oefening - jouw eerste tekstgeneratie-app

Nu we hebben geleerd hoe we openai kunnen instellen en configureren, is het tijd om je eerste tekstgeneratie-app te bouwen. Volg deze stappen om je app te bouwen:

1. Maak een virtuele omgeving en installeer openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Als je Windows gebruikt, typ dan `venv\Scripts\activate` in plaats van `source venv/bin/activate`.

   > [!NOTE]
   > Vind je Azure OpenAI-sleutel door naar [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) te gaan, zoek naar `Open AI`, selecteer de `Open AI resource` en klik vervolgens op `Keys and Endpoint` en kopieer de waarde van `Key 1`.

1. Maak een _app.py_-bestand aan en geef deze de volgende code:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # voeg je voltooiingscode toe
   prompt = "Complete the following: Once upon a time there was a"

   # doe een verzoek met de Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print antwoord
   print(response.output_text)
   ```

   > [!NOTE]
   > Als je gewone OpenAI (niet Azure) gebruikt, gebruik `client = OpenAI(api_key="<vervang deze waarde door je OpenAI sleutel>")` (zonder `base_url`) en geef een modelnaam door zoals `gpt-5-mini` in plaats van een deploymentnaam.

   Je zou ongeveer de volgende output moeten zien:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Verschillende soorten prompts, voor verschillende dingen

Nu je hebt gezien hoe je tekst kunt genereren met een prompt, heb je zelfs een programma draaien dat je kunt aanpassen om verschillende soorten tekst te genereren.

Prompts kunnen worden gebruikt voor allerlei taken. Bijvoorbeeld:

- **Genereer een type tekst**. Bijvoorbeeld, je kunt een gedicht genereren, vragen voor een quiz, enzovoort.
- **Zoek informatie op**. Je kunt prompts gebruiken om informatie op te zoeken zoals in het volgende voorbeeld: 'Wat betekent CORS in webontwikkeling?'.
- **Genereer code**. Je kunt prompts gebruiken om code te genereren, bijvoorbeeld een reguliere expressie die e-mailadressen controleert of waarom niet een heel programma genereren, zoals een webapp?

## Een praktischer toepassingsvoorbeeld: een recepten-generator

Stel je voor dat je ingrediënten thuis hebt en iets wilt koken. Daarvoor heb je een recept nodig. Een manier om recepten te vinden is via een zoekmachine, of je kunt een LLM daarvoor gebruiken.

Je zou een prompt kunnen schrijven zoals:

> "Toon me 5 recepten voor een gerecht met de volgende ingrediënten: kip, aardappelen en wortels. Per recept, lijst alle gebruikte ingrediënten op."

Gegeven bovenstaande prompt zou je een vergelijkbare reactie kunnen krijgen:

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

Deze uitkomst is geweldig, ik weet wat ik kan koken. Op dit punt kunnen nuttige verbeteringen zijn:

- Ingrediënten filteren die ik niet lekker vind of waar ik allergisch voor ben.
- Een boodschappenlijst maken, voor het geval ik niet alle ingrediënten in huis heb.

Voor bovenstaande gevallen voegen we een extra prompt toe:

> "Verwijder alsjeblieft recepten met knoflook omdat ik daar allergisch voor ben en vervang het door iets anders. Maak ook een boodschappenlijst voor de recepten, rekening houdend met dat ik al kip, aardappelen en wortels in huis heb."

Nu heb je een nieuw resultaat, namelijk:

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

Dat zijn je vijf recepten zonder knoflook en je hebt ook een boodschappenlijst, rekening houdend met wat je al in huis hebt.

## Oefening - bouw een recepten-generator

Nu we een scenario hebben uitgewerkt, laten we code schrijven die bij het gedemonstreerde scenario past. Volg deze stappen:

1. Gebruik het bestaande _app.py_-bestand als startpunt
1. Zoek de variabele `prompt` en verander de code ervan naar het volgende:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Als je nu de code uitvoert, zou je een vergelijkbare output moeten zien als:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > LET OP, je LLM is niet deterministisch, dus je kunt elke keer dat je het programma uitvoert verschillende resultaten krijgen.

   Geweldig, laten we eens kijken hoe we dingen kunnen verbeteren. Om dingen te verbeteren willen we dat de code flexibel is, zodat ingrediënten en aantal recepten aangepast en veranderd kunnen worden.

1. Laten we de code op de volgende manier wijzigen:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpoleer het aantal recepten in de prompt en ingrediënten
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Het uitvoeren van de code voor een test kan er zo uitzien:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Verbeteren door filter en boodschappenlijst toe te voegen

We hebben nu een werkende app die recepten kan produceren en het is flexibel omdat het afhankelijk is van invoer van de gebruiker, zowel qua aantal recepten als de gebruikte ingrediënten.

Om het verder te verbeteren willen we het volgende toevoegen:

- **Ingrediënten filteren**. We willen in staat zijn om ingrediënten te filteren die we niet lekker vinden of waarvoor we allergisch zijn. Om deze wijziging door te voeren, kunnen we onze bestaande prompt aanpassen en een filtervoorwaarde aan het einde toevoegen zoals:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Boven voegen we `{filter}` toe aan het einde van de prompt en we leggen ook de filterwaarde vast van de gebruiker.

  Een voorbeeldinvoer bij het uitvoeren van het programma kan nu zo eruitzien:

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

  Zoals je ziet zijn recepten met melk eruit gefilterd. Maar als je lactose-intolerant bent, wil je misschien ook recepten met kaas eruit filteren, dus het is belangrijk duidelijk te zijn.


- **Maak een boodschappenlijst**. We willen een boodschappenlijst maken, rekening houdend met wat we al thuis hebben.

  Voor deze functionaliteit kunnen we proberen alles in één prompt op te lossen, of we kunnen het opsplitsen in twee prompts. Laten we de laatste benadering proberen. Hier suggereert men een extra prompt toe te voegen, maar daarvoor moeten we het resultaat van de eerste prompt als context toevoegen aan de tweede prompt.

  Zoek het deel in de code waar het resultaat van de eerste prompt wordt afgedrukt en voeg hieronder de volgende code toe:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print antwoord
  print("Shopping list:")
  print(response.output_text)
  ```

  Let op het volgende:

  1. We construeren een nieuwe prompt door het resultaat van de eerste prompt toe te voegen aan de nieuwe prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. We doen een nieuw verzoek, maar houden ook rekening met het aantal tokens dat we in de eerste prompt hebben gevraagd, dus zeggen we deze keer dat `max_output_tokens` 1200 is.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Als we deze code uitvoeren, komen we uit op het volgende resultaat:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Verbeter je opzet

Wat we tot nu toe hebben is code die werkt, maar er zijn enkele aanpassingen die we moeten doen om de zaken verder te verbeteren. Enkele dingen die we moeten doen zijn:

- **Scheiding van geheimen en code**, zoals de API-sleutel. Geheimen horen niet in de code thuis en moeten op een veilige plek worden opgeslagen. Om geheimen te scheiden van code kunnen we omgevingsvariabelen gebruiken en bibliotheken zoals `python-dotenv` om deze uit een bestand te laden. Zo zou dat er in code uitzien:

  1. Maak een `.env`-bestand aan met de volgende inhoud:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Let op, voor Azure OpenAI in Microsoft Foundry moet je in plaats daarvan de volgende omgevingsvariabelen instellen:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     In de code laad je de omgevingsvariabelen als volgt:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Een woord over tokenlengte**. We moeten nadenken over hoeveel tokens we nodig hebben om de gewenste tekst te genereren. Tokens kosten geld, dus waar mogelijk moeten we proberen spaarzaam te zijn met het aantal tokens dat we gebruiken. Bijvoorbeeld, kunnen we de prompt zo formuleren dat we minder tokens nodig hebben?

  Om het aantal gebruikte tokens te wijzigen, kun je de parameter `max_output_tokens` gebruiken. Als je bijvoorbeeld 100 tokens wilt gebruiken, doe je het volgende:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimenteren met temperatuur**. Temperatuur hebben we tot nu toe niet besproken, maar het is een belangrijke context voor de werking van ons programma. Hoe hoger de temperatuurwaarde, hoe willekeuriger de output zal zijn. Hoe lager de temperatuurwaarde, hoe voorspelbaarder de output is. Bedenk of je variatie in je output wilt of niet.

  Om de temperatuur aan te passen, gebruik je de parameter `temperature`. Bijvoorbeeld, als je een temperatuur van 0,5 wilt gebruiken, doe je:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Let op, hoe dichter bij 1.0, hoe gevarieerder de output.

- **Redeneringsmodellen gebruiken geen `temperature`**. Dit is een belangrijke verandering in 2026. De huidige, niet-verouderde modellen op Microsoft Foundry zijn **redeneringsmodellen** (de GPT-5 familie, o-series) – en ze **ondersteunen geen `temperature` of `top_p`** (evenmin `max_tokens`; gebruik `max_output_tokens`). Als je `temperature` naar `gpt-5-mini` stuurt, krijg je een "parameter niet ondersteund" foutmelding. Dus om het temperatuurvoorbeeld hierboven uit te proberen, gebruik je een model dat nog wel sampling-controles ondersteunt – bijvoorbeeld een open **Llama** model zoals `Llama-3.3-70B-Instruct` uit de [Microsoft Foundry model catalogus](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), aangeroepen via de Foundry Models / Azure AI Inference endpoint (net zoals de `githubmodels-*` voorbeelden). Voor redeneringsmodellen zoals GPT-5 stuur je output anders aan:
  - **Prompt engineering** - duidelijke instructies, voorbeelden en gestructureerde output (zie les [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) doen het werk dat sampling-knoppen vroeger deden.
  - **Redeneringscontroles** - parameters zoals redeneringsinspanning/woordrijkheid ruilen diepte van redenering in tegen latency en kosten.

  Kort gezegd: `temperature`/`top_p` zijn nog steeds geldig voor veel modellen (Llama, Mistral, Phi en de GPT-4.x familie – hoewel GPT-4.x wordt uitgefaseerd), maar de trend is prompt engineering + redeneringscontroles bij redeneringsmodellen zoals GPT-5.

## Opdracht

Voor deze opdracht kun je zelf kiezen wat je bouwt.

Hier zijn enkele suggesties:

- Pas de receptengenerator-app aan om deze verder te verbeteren. Experimenteer met temperatuurwaarden en de prompts om te zien wat je kunt bedenken.
- Bouw een "studiegenoot". Deze app moet in staat zijn vragen te beantwoorden over een onderwerp, bijvoorbeeld Python. Je kunt prompts gebruiken zoals "Wat is een bepaald onderwerp in Python?" of prompts die vragen om code te laten zien voor een bepaald onderwerp, enzovoorts.
- Geschiedenisbott, laat geschiedenis tot leven komen, stuur de bot aan om een bepaalde historische figuur te spelen en stel hem vragen over zijn leven en tijd.

## Oplossing

### Studienoot

Hieronder staat een startprompt, kijk hoe je die kunt gebruiken en aanpassen naar wens.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Geschiedenisbott

Hier zijn enkele prompts die je kunt gebruiken:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Kenniscontrole

Wat doet het concept temperatuur?

1. Het bepaalt hoe willekeurig de output is.
1. Het bepaalt hoe groot de respons is.
1. Het bepaalt hoeveel tokens er worden gebruikt.

## 🚀 Uitdaging

Wanneer je aan de opdracht werkt, probeer dan de temperatuur te variëren, zet deze op 0, 0.5 en 1. Onthoud dat 0 het minst gevarieerd is en 1 het meest. Welke waarde werkt het beste voor jouw app?

## Goed gedaan! Ga door met leren

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je kennis van Generative AI verder uit te breiden!

Ga verder naar Les 7 waar we bekijken hoe je [chatapplicaties bouwt](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->