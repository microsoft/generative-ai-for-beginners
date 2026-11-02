# Izgradnja aplikacija za generiranje teksta

[![Izgradnja aplikacija za generiranje teksta](../../../translated_images/hr/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite sliku iznad da biste pogledali video ovog sata)_

Do sada ste kroz ovaj kurikulum vidjeli da postoje osnovni koncepti poput promptova i čak cjelokupna disciplina zvana "prompt inženjering". Mnogi alati s kojima možete komunicirati poput ChatGPT-a, Office 365, Microsoft Power Platforme i drugih podržavaju korištenje promptova za izvođenje nečega.

Da biste dodali takvo iskustvo u aplikaciju, morate razumjeti koncepte kao što su promptovi, dovršenja i odabrati biblioteku za rad. Upravo to ćete naučiti u ovom poglavlju.

## Uvod

U ovom poglavlju ćete:

- Naučiti o biblioteci openai i njenim osnovnim konceptima.
- Izgraditi aplikaciju za generiranje teksta koristeći openai.
- Razumjeti kako koristiti koncepte poput prompta, temperature i tokena za izgradnju aplikacije za generiranje teksta.

## Ciljevi učenja

Na kraju ovog sata, moći ćete:

- Objasniti što je aplikacija za generiranje teksta.
- Izgraditi aplikaciju za generiranje teksta koristeći openai.
- Konfigurirati svoju aplikaciju za korištenje više ili manje tokena i također mijenjati temperaturu, za raznoliki ishod.

## Što je aplikacija za generiranje teksta?

Obično kad gradite aplikaciju, ona ima neku vrstu sučelja poput sljedećeg:

- Bazirano na naredbama. Konzolne aplikacije su tipične aplikacije gdje unosite naredbu i ona izvršava zadatak. Na primjer, `git` je aplikacija bazirana na naredbama.
- Korisničko sučelje (UI). Neke aplikacije imaju grafička korisnička sučelja (GUI) gdje kliknete gumbe, unosite tekst, birate opcije i slično.

### Konzolne i UI aplikacije su ograničene

Usporedite to s aplikacijom baziranom na naredbi gdje unosite naredbu:

- **Ograničeno je**. Ne možete jednostavno unijeti bilo koju naredbu, samo one koje aplikacija podržava.
- **Specifično za jezik**. Neke aplikacije podržavaju mnogo jezika, ali po zadanim postavkama aplikacija je izrađena za određeni jezik, čak i ako možete dodati podršku za druge jezike.

### Prednosti aplikacija za generiranje teksta

Kako se onda aplikacija za generiranje teksta razlikuje?

U aplikaciji za generiranje teksta imate veću fleksibilnost, niste ograničeni na skup naredbi ili određeni ulazni jezik. Umjesto toga, možete koristiti prirodni jezik za interakciju s aplikacijom. Još jedna prednost je da već komunicirate s izvorom podataka koji je treniran na ogromnom korpusu informacija, dok tradicionalna aplikacija može biti ograničena na ono što je u bazi podataka.

### Što mogu izgraditi s aplikacijom za generiranje teksta?

Mnogo je stvari koje možete izgraditi. Na primjer:

- **Chatbot**. Chatbot koji odgovara na pitanja o temama poput vaše tvrtke i njezinih proizvoda mogao bi biti dobra opcija.
- **Pomoćnik**. LLM-ovi su odlični za stvari poput sažimanja teksta, izvlačenja uvida iz teksta, proizvodnje teksta poput životopisa i slično.
- **Pomoćnik za kod**. Ovisno o jezičnom modelu koji koristite, možete izgraditi pomoćnika za pisanje koda. Na primjer, možete koristiti proizvod poput GitHub Copilot kao i ChatGPT za pomoć u pisanju koda.

## Kako mogu početi?

Pa, morate pronaći način za integraciju s LLM-om što obično podrazumijeva sljedeća dva pristupa:

- Koristiti API. Ovdje sastavljate web zahtjeve sa svojim promptom i dobijete generirani tekst natrag.
- Koristiti biblioteku. Biblioteke pomažu sakriti API pozive i olakšavaju njihovu upotrebu.

## Biblioteke/SDK-ovi

Postoji nekoliko poznatih biblioteka za rad s LLM-ovima poput:

- **openai**, ova biblioteka olakšava povezivanje s vašim modelom i slanje promptova.

Zatim postoje biblioteke koje rade na višoj razini poput:

- **Langchain**. Langchain je poznat i podržava Python.
- **Semantic Kernel**. Semantic Kernel je biblioteka tvrtke Microsoft koja podržava jezike C#, Python i Java.

## Prva aplikacija koristeći openai

Pogledajmo kako možemo izgraditi našu prvu aplikaciju, koje biblioteke trebamo, koliko je potrebno i slično.

### Instalirajte openai

Postoji mnogo biblioteka za interakciju s OpenAI ili Azure OpenAI. Moguće je koristiti mnoge programske jezike kao što su C#, Python, JavaScript, Java i drugi. Odabrali smo korištenje biblioteke `openai` za Python, pa ćemo koristiti `pip` za instalaciju.

```bash
pip install openai
```

### Kreirajte resurs

Morate izvršiti sljedeće korake:

- Kreirajte račun na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Dobijte pristup Azure OpenAI. Idite na [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) i zatražite pristup.

  > [!NOTE]
  > U vrijeme pisanja, morate se prijaviti za pristup Azure OpenAI.

- Instalirajte Python <https://www.python.org/>
- Kreirali ste Azure OpenAI Service resurs. Pogledajte ovaj vodič kako [kreirati resurs](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Pronađite API ključ i krajnju točku

Sada trebate reći svojoj `openai` biblioteci koji API ključ koristiti. Da biste pronašli svoj API ključ, idite na odjeljak "Keys and Endpoint" vašeg Azure OpenAI resursa i kopirajte vrijednost "Key 1".

![Ključevi i krajnja točka resursa u Azure Portalu](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sad kad imate ove informacije kopirane, uputimo biblioteke da ih koriste.

> [!NOTE]
> Vrijedno je odvojiti vaš API ključ od koda. To možete napraviti korištenjem varijabli okoline.
>
> - Postavite varijablu okoline `OPENAI_API_KEY` na svoj API ključ.
>   `export OPENAI_API_KEY='sk-...'`

### Postavljanje konfiguracije za Azure

Ako koristite Azure OpenAI (sada dio Microsoft Foundry), evo kako postaviti konfiguraciju. Koristimo standardnog `OpenAI` klijenta usmjerenog na Azure OpenAI `/openai/v1/` krajnju točku, koja radi s Responses API-jem i ne treba `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Gornjim kodom postavljamo sljedeće:

- `api_key`, to je vaš API ključ pronađen u Azure Portalu ili Microsoft Foundry portalu.
- `base_url`, to je krajnja točka vašeg Foundry resursa s `/openai/v1/` dodatkom. Stabilna v1 krajnja točka radi preko OpenAI i Azure OpenAI bez upravljanja `api_version`.

> [!NOTE] > `os.environ` čita varijable okoline. Možete ga koristiti za čitanje varijabli okoline poput `AZURE_OPENAI_API_KEY` i `AZURE_OPENAI_ENDPOINT`. Postavite ove varijable okoline u svojem terminalu ili koristeći biblioteku poput `dotenv`.

## Generiranje teksta

Način generiranja teksta je korištenje Responses API-ja putem metode `responses.create`. Evo primjera:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

U gornjem kodu stvaramo odgovor i prosljeđujemo model koji želimo koristiti i prompt. Zatim ispisujemo generirani tekst putem `response.output_text`.

### Razgovori s više tura

Responses API je prikladan kako za generiranje teksta u jednoj turi, tako i za višeturajne chatbotove - pružite popis poruka u `input` za izgradnju razgovora:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Više o ovoj funkcionalnosti u nadolazećem poglavlju.

## Vježba - vaša prva aplikacija za generiranje teksta

Sad kad smo naučili kako postaviti i konfigurirati openai, vrijeme je za izradu vaše prve aplikacije za generiranje teksta. Slijedite ove korake da biste izgradili svoju aplikaciju:

1. Napravite virtualno okruženje i instalirajte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ako koristite Windows, upišite `venv\Scripts\activate` umjesto `source venv/bin/activate`.

   > [!NOTE]
   > Pronađite svoj Azure OpenAI ključ odlaskom na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) i potražite `Open AI`, zatim odaberite `Open AI resource` i potom `Keys and Endpoint` i kopirajte vrijednost `Key 1`.

1. Kreirajte datoteku _app.py_ i upišite sljedeći kod:

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
   > Ako koristite običan OpenAI (ne Azure), koristite `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (bez `base_url`) i proslijedite ime modela poput `gpt-5-mini` umjesto ime deploymenta.

   Trebali biste vidjeti izlaz poput sljedećeg:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Različite vrste promptova, za različite stvari

Sad ste vidjeli kako generirati tekst pomoću prompta. Čak imate i program koji radi i možete ga mijenjati i prilagođavati za generiranje različitih vrsta teksta.

Promptovi se mogu koristiti za sve vrste zadataka. Na primjer:

- **Generiranje vrste teksta**. Na primjer, možete generirati pjesmu, pitanja za kviz itd.
- **Pretraživanje informacija**. Možete koristiti promptove za traženje informacija kao u primjeru "Što znači CORS u web razvoju?".
- **Generiranje koda**. Možete koristiti promptove za generiranje koda, na primjer razvoj regularnog izraza za provjeru e-mailova ili zašto ne generirati cijeli program, poput web aplikacije?

## Praktičnija primjena: generator recepata

Zamislite da imate sastojke kod kuće i želite nešto skuhati. Za to vam treba recept. Jedan način da pronađete recepte je korištenje tražilice ili možete koristiti LLM za to.

Mogli biste napisati prompt poput ovog:

> "Pokaži mi 5 recepata za jelo s sljedećim sastojcima: piletina, krumpir i mrkva. Za svaki recept navedi sve korištene sastojke"

Na temelju gornjeg prompta mogli biste dobiti odgovor sličan ovome:

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

Ovaj ishod je sjajan, znam što kuhati. U ovom trenutku korisna poboljšanja mogla bi biti:

- Filtriranje sastojaka koje ne volim ili na koje sam alergičan.
- Izrada popisa za kupovinu, u slučaju da ne posjedujem sve sastojke kod kuće.

Za gore navedene slučajeve, dodajmo dodatni prompt:

> "Molim ukloni recepte s češnjakom jer sam alergičan i zamijeni ga nečim drugim. Također, molim napravi popis za kupovinu za recepte, uzimajući u obzir da već imam piletinu, krumpir i mrkvu kod kuće."

Sad imate novi rezultat, naime:

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

To su vaši pet recepata, bez češnjaka, i imate popis za kupovinu s obzirom na ono što već imate kod kuće.

## Vježba - izgradite generator recepata

Sad kad smo prikazali scenarij, napišimo kod koji odgovara prikazanom scenariju. Da biste to učinili, slijedite ove korake:

1. Koristite postojeću datoteku _app.py_ kao početnu točku
1. Pronađite varijablu `prompt` i promijenite njezin kod na sljedeći:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ako sad pokrenete kod, trebali biste vidjeti izlaz sličan ovome:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NAPOMENA, vaš LLM je nedomentistički, pa možete dobiti različite rezultate svaki put kad pokrenete program.

   Odlično, pogledajmo kako možemo stvari poboljšati. Za poboljšanje želimo osigurati fleksibilnost koda, tako da se sastojci i broj recepata mogu mijenjati i poboljšavati.

1. Promijenimo kod na sljedeći način:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testni pokus koda mogao bi izgledati ovako:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Poboljšanje dodavanjem filtera i popisa za kupovinu

Sad imamo radnu aplikaciju sposobnu za proizvodnju recepata, a fleksibilna je jer se oslanja na unos korisnika, kako na broj recepata tako i na korištene sastojke.

Za daljnje poboljšanje želimo dodati sljedeće:

- **Filtriranje sastojaka**. Želimo moći filtrirati sastojke koje ne volimo ili na koje smo alergični. Da bismo to postigli, možemo urediti naš postojeći prompt i dodati uvjet filtra na kraj prompta, ovako:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Gore dodajemo `{filter}` na kraj prompta i također dohvaćamo vrijednost za filter od korisnika.

  Primjer unosa pri pokretanju programa sada može izgledati ovako:

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

  Kao što vidite, svi recepti koji sadrže mlijeko su filtrirani. Ali, ako ste netolerantni na laktozu, možda biste željeli filtrirati i recepte sa sirom, pa je potrebno jasno definirati.

- **Proizvodnja popisa za kupovinu**. Želimo proizvesti popis za kupovinu uzimajući u obzir što već imamo kod kuće.

  Za ovu funkcionalnost mogli bismo pokušati riješiti sve u jednom promptu ili bismo mogli to podijeliti u dva prompta. Pokušajmo ovaj drugi pristup. Ovdje predlažemo dodavanje dodatnog prompta, ali da to funkcionira, moramo dodati rezultat prvog prompta kao kontekst drugom promptu.

  Pronađite dio u kodu koji ispisuje rezultat prvog prompta i dodajte sljedeći kod ispod:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Obratite pažnju na sljedeće:

  1. Konstrukcija novog prompta dodavanjem rezultata iz prvog prompta u novi prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Pravljenje novog zahtjeva, uzimajući u obzir broj tokena zatraženih u prvom promptu, pa ovaj put kažemo `max_output_tokens`  je 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Izvršavajući ovaj kod sada dobivamo sljedeći rezultat:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Poboljšajte svoju postavu

Ono što do sada imamo je kod koji funkcionira, ali postoje neke prilagodbe koje bismo trebali napraviti kako bismo stvari dodatno poboljšali. Neke stvari koje bismo trebali napraviti su:

- **Odvojite tajne od koda**, poput API ključa. Tajne ne pripadaju u kod i trebale bi se pohraniti na sigurno mjesto. Da bismo odvojili tajne od koda, možemo koristiti varijable okoline i biblioteke poput `python-dotenv` za učitavanje iz datoteke. Evo kako bi to izgledalo u kodu:

  1. Napravite datoteku `.env` s sljedećim sadržajem:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Napomena, za Azure OpenAI u Microsoft Foundry, trebate postaviti sljedeće varijable okoline:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     U kodu, varijable okoline biste učitali ovako:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Riječ o duljini tokena**. Trebali bismo razmotriti koliko tokena trebamo za generiranje željenog teksta. Tokeni koštaju novac, stoga bismo, gdje je moguće, trebali biti štedljivi s brojem tokena koje koristimo. Na primjer, možemo li formulirati prompt tako da koristimo manje tokena?

  Za promjenu broja tokena koje koristimo, možemo koristiti parametar `max_output_tokens`. Na primjer, ako želite koristiti 100 tokena, napravili biste:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimentiranje s temperaturom**. Temperatura je nešto što do sada nismo spomenuli, ali je važan kontekst za ponašanje našeg programa. Što je veća vrijednost temperature, to je izlaz nasumičniji. Obrnuto, što je manja temperatura, to je izlaz predvidljiviji. Razmislite želite li varijaciju u izlazu ili ne.

  Za promjenu temperature, možete koristiti parametar `temperature`. Na primjer, ako želite koristiti temperaturu 0.5, učinili biste:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Napomena, što je bliže 1.0, to je izlaz raznolikiji.

- **Razumski modeli ne koriste `temperature`**. Ovo je važan pomak u 2026. Trenutni, ne-deprecirani modeli na Microsoft Foundryu su **razumski modeli** (GPT-5 obitelj, o-serija) - i oni **ne podržavaju `temperature` niti `top_p`** (niti `max_tokens`; koristite `max_output_tokens`). Ako pošaljete `temperature` na `gpt-5-mini` dobit ćete grešku "parametar nije podržan". Dakle, da biste isprobali primjer temperature gore, usmjerite to na model koji još podržava upravljanje uzorkovanjem – na primjer otvoreni **Llama** model poput `Llama-3.3-70B-Instruct` iz [Microsoft Foundry kataloga modela](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), pozvan preko Foundry Models / Azure AI Inference krajnje točke (na isti način kao i `githubmodels-*` primjeri). Za razumske modele poput GPT-5, upravljanje izlazom ide drugačije:
  - **Inženjering prompta** - jasne upute, primjeri i strukturirani izlaz (vidi lekciju [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) zamjenjuju rad koje prije obavljali kontrolni brojila za uzorkovanje.
  - **Razumske kontrole** - parametri poput truda/opširnosti rezoniranja uravnotežuju dubinu rezoniranja s latencijom i troškovima.

  Ukratko: `temperature`/`top_p` još su valjani na mnogim modelima (Llama, Mistral, Phi i GPT-4.x obitelj - iako GPT-4.x odlazi u zastarjelost), ali smjer je inženjering prompta + razumske kontrole na razumskim modelima poput GPT-5.

## Zadatak

Za ovaj zadatak možete odabrati što ćete izgraditi.

Evo nekoliko prijedloga:

- Doradite aplikaciju za generiranje recepata kako biste je dodatno poboljšali. Eksperimentirajte s vrijednostima temperature i promptovima da vidite što možete smisliti.
- Izgradite "studijskog prijatelja". Ova aplikacija treba biti u stanju odgovarati na pitanja o nekoj temi, na primjer Python, možete imati upite poput "Što je određena tema u Pythonu?", ili prompt koji kaže, pokaži mi kod za određenu temu itd.
- Povijesni bot, oživite povijest, uputite bota da glumi određenu povijesnu osobu i postavite mu pitanja o njegovom životu i vremenu.

## Rješenje

### Studijski prijatelj

Ispod je početni prompt, pogledajte kako ga možete iskoristiti i prilagoditi po želji.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Povijesni bot

Evo nekoliko promptova koje biste mogli koristiti:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Provjera znanja

Što radi koncept temperature?

1. Kontrolira koliko nasumičan izlaz je.
1. Kontrolira koliko je velik odgovor.
1. Kontrolira koliko tokena se koristi.

## 🚀 Izazov

Dok radite na zadatku, pokušajte varirati temperaturu, postavite je na 0, 0.5 i 1. Zapamtite da je 0 najmanje raznoliko, a 1 najviše. Koja vrijednost najbolje radi za vašu aplikaciju?

## Odličan rad! Nastavite učiti

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da nastavite s usavršavanjem znanja o Generativnoj AI!

Idite na Lekciju 7 gdje ćemo pogledati kako [izgraditi chat aplikacije](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->