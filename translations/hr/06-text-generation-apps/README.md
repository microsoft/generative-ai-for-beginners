# Izrada aplikacija za generiranje teksta

[![Izrada aplikacija za generiranje teksta](../../../translated_images/hr/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite na sliku iznad za prikaz video lekcije)_

Do sada ste kroz ovaj nastavni program vidjeli da postoje osnovni koncepti poput upita (prompts) i čak cijela disciplina zvana „inženjering upita“. Mnogi alati s kojima možete komunicirati poput ChatGPT-a, Office 365, Microsoft Power Platform i drugih, podržavaju korištenje upita za postizanje nečega.

Da biste takvo iskustvo dodali svojoj aplikaciji, morate razumjeti koncepte poput upita, dovršenja (completions) i odabrati biblioteku za rad. Točno to ćete naučiti u ovom poglavlju.

## Uvod

U ovom poglavlju naučit ćete:

- Naučiti o biblioteci openai i njezinim osnovnim konceptima.
- Izraditi aplikaciju za generiranje teksta koristeći openai.
- Razumjeti kako koristiti koncepte poput upita, temperature i tokena za izgradnju aplikacije za generiranje teksta.

## Ciljevi učenja

Na kraju ove lekcije moći ćete:

- Objasniti što je aplikacija za generiranje teksta.
- Izraditi aplikaciju za generiranje teksta koristeći openai.
- Konfigurirati svoju aplikaciju za korištenje više ili manje tokena, te promijeniti temperaturu za raznolik rezultat.

## Što je aplikacija za generiranje teksta?

Obično, kada izrađujete aplikaciju, ona ima neku vrstu sučelja poput sljedećeg:

- Temeljeno na komandama. Konzolne aplikacije su tipične aplikacije u kojima upisujete naredbu i ona izvršava zadatak. Primjerice, `git` je aplikacija temeljena na komandama.
- Korisničko sučelje (UI). Neke aplikacije imaju grafička korisnička sučelja (GUI) gdje klikate gumbe, unosite tekst, birate opcije i slično.

### Konzolne i UI aplikacije su ograničene

Usporedite to s aplikacijom temeljnom na komandama gdje upisujete naredbu:

- **Ograničeno je**. Ne možete upisati bilo koju naredbu, samo one koje aplikacija podržava.
- **Specifično za jezik**. Neke aplikacije podržavaju više jezika, ali po defaultu su izrađene za određeni jezik, iako možete dodati podršku za više jezika.

### Prednosti aplikacija za generiranje teksta

Pa kako je aplikacija za generiranje teksta drugačija?

U aplikaciji za generiranje teksta imate veću fleksibilnost, niste ograničeni na skup naredbi ili specifični ulazni jezik. Umjesto toga koristite prirodni jezik za interakciju s aplikacijom. Još jedna prednost je što u većini slučajeva već komunicirate s podatkovnim izvorom koji je treniran na ogromnom korpusu informacija, dok bi tradicionalna aplikacija mogla biti ograničena na ono što se nalazi u bazi podataka.

### Što mogu izraditi s aplikacijom za generiranje teksta?

Mnogo toga se može izraditi. Na primjer:

- **Chatbot**. Chatbot koji odgovara na pitanja o temama, poput vaše tvrtke i njenih proizvoda, može biti dobar izbor.
- **Pomoćnik**. Veliki jezični modeli (LLM) su izvrsni za stvari poput sažimanja teksta, izvlačenja uvida iz teksta, proizvodnju teksta poput životopisa i slično.
- **Asistent za kodiranje**. Ovisno o jezičnom modelu koji koristite, možete izraditi asistenta za kodiranje koji vam pomaže pisati kod. Na primjer, možete koristiti proizvode poput GitHub Copilot-a kao i ChatGPT za pomoć pri pisanju koda.

## Kako mogu početi?

Pa, trebate pronaći način kako se integrirati s velikim jezičnim modelom (LLM), što obično uključuje sljedeća dva pristupa:

- Koristiti API. Ovdje sastavljate web zahtjeve sa svojim upitom i dobivate generirani tekst natrag.
- Koristiti biblioteku. Biblioteke pomažu enkapsulirati API pozive i čine ih lakšim za korištenje.

## Biblioteke/SDK-ovi

Postoje neke dobro poznate biblioteke za rad s LLM-ovima poput:

- **openai**, ova biblioteka olakšava povezivanje s vašim modelom i slanje upita.

Zatim postoje biblioteke koje rade na višoj razini poput:

- **Langchain**. Langchain je dobro poznat i podržava Python.
- **Semantic Kernel**. Semantic Kernel je Microsoftova biblioteka koja podržava jezike C#, Python i Java.

## Prva aplikacija koristeći openai

Pogledajmo kako možemo izraditi našu prvu aplikaciju, koje biblioteke trebamo, koliko je potrebno i tako dalje.

### Instalacija openai

Postoji mnogo biblioteka za interakciju s OpenAI ili Azure OpenAI. Moguće je koristiti različite programske jezike kao što su C#, Python, JavaScript, Java i drugi. Mi smo odabrali koristiti Python biblioteku `openai`, pa ćemo koristiti `pip` za instalaciju.

```bash
pip install openai
```

### Kreiranje resursa

Trebate izvršiti sljedeće korake:

- Kreirajte račun na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Dobijte pristup Azure OpenAI. Posjetite [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) i zatražite pristup.

  > [!NOTE]
  > U trenutku pisanja ovog materijala, morate podnijeti zahtjev za pristup Azure OpenAI.

- Instalirajte Python <https://www.python.org/>
- Kreirajte Azure OpenAI Service resurs. Pogledajte ovaj vodič za [kako kreirati resurs](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Pronađite API ključ i krajnju točku

U ovom trenutku trebate svojoj biblioteci `openai` reći koji API ključ koristi. Da biste pronašli svoj API ključ, idite u odjeljak "Keys and Endpoint" vašeg Azure OpenAI resursa i kopirajte vrijednost "Key 1".

![Ključevi i resurs "endpoint" na Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sad kad imate ove podatke kopirane, uputimo biblioteke da ih koriste.

> [!NOTE]
> Vrijedi razdvojiti svoj API ključ od koda. To možete učiniti korištenjem varijabli okruženja.
>
> - Postavite varijablu okruženja `OPENAI_API_KEY` na svoj API ključ.
>   `export OPENAI_API_KEY='sk-...'`

### Postavljanje konfiguracije za Azure

Ako koristite Azure OpenAI (sada dio Microsoft Foundry), evo kako postaviti konfiguraciju. Koristimo standardni `OpenAI` klijent usmjeren na Azure OpenAI `/openai/v1/` endpoint, koji radi s Responses API-jem i ne zahtijeva `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Gore postavljamo sljedeće:

- `api_key`, to je vaš API ključ koji se nalazi u Azure Portalu ili Microsoft Foundry portalu.
- `base_url`, to je vaša Foundry adresa resursa s dodatkom `/openai/v1/`. Stabilni v1 endpoint radi na OpenAI i Azure OpenAI bez potrebe za upravljanjem `api_version`.

> [!NOTE] > `os.environ` čita varijable okruženja. Možete ga koristiti za čitanje varijabli okruženja poput `AZURE_OPENAI_API_KEY` i `AZURE_OPENAI_ENDPOINT`. Postavite te varijable u vašem terminalu ili koristite biblioteku poput `dotenv`.

## Generiranje teksta

Način generiranja teksta je korištenjem Responses API-a putem metode `responses.create`. Evo primjera:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

U gornjem kodu kreiramo odgovor i prosljeđujemo model koji želimo koristiti i upit (prompt). Zatim ispisujemo generirani tekst putem `response.output_text`.

### Višekratni razgovori

Responses API je dobro prilagođen za generiranje teksta u jednom koraku kao i za višekratne razgovore s chatbotom - prosljeđujete listu poruka u `input` da izgradite konverzaciju:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Više o ovoj funkcionalnosti u nadolazećem poglavlju.

## Vježba - vaša prva aplikacija za generiranje teksta

Sad kad smo naučili kako postaviti i konfigurirati openai, vrijeme je da izradite svoju prvu aplikaciju za generiranje teksta. Da biste izradili svoju aplikaciju, slijedite ove korake:

1. Kreirajte virtualno okruženje i instalirajte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ako koristite Windows, upišite `venv\Scripts\activate` umjesto `source venv/bin/activate`.

   > [!NOTE]
   > Pronađite svoj Azure OpenAI ključ tako da odete na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) i potražite `Open AI`, zatim odaberite `Open AI resource` i potom odaberite `Keys and Endpoint` i kopirajte vrijednost `Key 1`.

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
   > Ako koristite obični OpenAI (ne Azure), koristite `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (bez `base_url`) i navedite ime modela poput `gpt-5-mini` umjesto imena deploymenta.

   Trebali biste dobiti izlaz poput sljedećeg:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Različite vrste upita za različite stvari

Sad ste vidjeli kako generirati tekst koristeći upit. Zapravo imate program koji radi i koji možete mijenjati da generira različite vrste teksta.

Upiti se mogu koristiti za razne zadatke. Na primjer:

- **Generiranje vrste teksta**. Na primjer, možete generirati pjesmu, pitanja za kviz itd.
- **Traženje informacija**. Možete koristiti upite za pretraživanje informacija poput primjera 'Što znači CORS u web razvoju?'.
- **Generiranje koda**. Možete koristiti upite za generiranje koda, primjerice razvijanje regularnog izraza za provjeru emailova ili zašto ne generirati cijelu aplikaciju, poput web aplikacije?

## Praktičniji primjer: generator recepata

Zamislite da imate sastojke kod kuće i želite nešto skuhati. Za to vam treba recept. Jedan od načina pronalaska recepata je korištenje tražilice ili možete koristiti LLM.

Mogli biste napisati upit ovako:

> "Prikaži mi 5 recepata za jelo s sljedećim sastojcima: piletina, krumpir i mrkva. Za svaki recept navedite sve korištene sastojke"

Na temelju gore navedenog upita mogli biste dobiti odgovor sličan ovome:

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

Ovaj rezultat je odličan, sada znam što skuhati. U ovom trenutku, korisna poboljšanja bi mogla biti:

- Filtriranje sastojaka koje ne volim ili na koje sam alergičan.
- Proizvesti popis za kupovinu, u slučaju da nemam sve sastojke kod kuće.

Za ove slučajeve dodajmo dodatni upit:

> "Molim ukloni recepte s češnjakom jer sam alergičan i zamijeni ga nečim drugim. Također, molim napravi popis za kupovinu za recepte s obzirom da već imam piletinu, krumpir i mrkvu kod kuće."

Sada imate novi rezultat, naime:

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

To je vaših pet recepata, bez spominjanja češnjaka, i imate i popis za kupovinu s obzirom na to što već imate kod kuće.

## Vježba - izradite generator recepata

Sad kad smo odglumili scenario, napišimo kod koji odgovara demonstriranom scenariju. Da biste to učinili, slijedite ove korake:

1. Koristite postojeću datoteku _app.py_ kao polazište
1. Pronađite varijablu `prompt` i promijenite njezin kod u sljedeći:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ako sada pokrenete kod, trebali biste vidjeti izlaz sličan ovom:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NAPOMENA, vaš LLM je nedeterminističan, pa možete dobiti različite rezultate svaki put kada pokrenete program.

   Odlično, pogledajmo kako poboljšati stvari. Za poboljšanje želimo napraviti kod fleksibilnim, tako da se sastojci i broj recepata mogu mijenjati i prilagođavati.

1. Promijenimo kod na sljedeći način:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testiranje koda može izgledati ovako:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Poboljšanje dodavanjem filtra i popisa za kupovinu

Sad imamo funkcionalnu aplikaciju koja može proizvoditi recepte i fleksibilna je jer se oslanja na unos korisnika, i za broj recepata i za sastojke.

Za daljnje poboljšanje želimo dodati sljedeće:

- **Filtriranje sastojaka**. Želimo moći filtrirati sastojke koje ne volimo ili na koje smo alergični. Da bismo to postigli, možemo urediti postojeći upit i na kraj dodati uvjet filtra ovako:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Gore dodajemo `{filter}` na kraj upita i također dohvaćamo vrijednost filtra od korisnika.

  Primjer unosa prilikom pokretanja programa sada može izgledati ovako:

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

  Kao što vidite, svi su recepti koji sadrže mlijeko filtrirani. Ali, ako ste netolerantni na laktozu, možda ćete željeti filtrirati i recepte sa sirom, pa treba biti jasan.

- **Proizvodnja popisa za kupovinu**. Želimo napraviti popis za kupovinu uzimajući u obzir ono što već imamo kod kuće.

  Za ovu funkcionalnost mogli bismo pokušati riješiti sve u jednom upitu ili bismo mogli podijeliti na dva upita. Pokušajmo s drugim pristupom. Ovdje predlažemo dodati dodatni upit, ali da to funkcionira, potrebno je dodati rezultat prvog upita kao kontekst za drugi upit.

  Pronađite dio koda koji ispisuje rezultat iz prvog upita i dodajte sljedeći kod ispod:

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

  1. Kreiramo novi upit tako da dodajemo rezultat iz prvog upita u novi upit:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Radimo novi zahtjev, ali uzimajući u obzir broj tokena koje smo tražili u prvom upitu, pa sada kažemo da je `max_output_tokens` 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Pokretanjem ovog koda dolazimo do sljedećeg izlaza:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Poboljšajte svoju postavku

Ono što do sada imamo je kod koji radi, ali postoje neke dorade koje bismo trebali napraviti kako bismo dodatno poboljšali stvari. Neke stvari koje bismo trebali napraviti su:

- **Odvojite tajne od koda**, poput API ključa. Tajne ne pripadaju u kod i trebaju se čuvati na sigurnom mjestu. Da bismo tajne odvojili od koda, možemo koristiti varijable okoline i biblioteke poput `python-dotenv` za učitavanje iz datoteke. Evo kako bi to izgledalo u kodu:

  1. Kreirajte datoteku `.env` sa sljedećim sadržajem:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Napomena, za Azure OpenAI u Microsoft Foundry, trebate postaviti sljedeće varijable okoline umjesto toga:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     U kodu biste učitali varijable okoline ovako:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Riječ o duljini tokena**. Trebali bismo razmotriti koliko tokena trebamo za generiranje željenog teksta. Tokeni koštaju, pa bismo gdje je moguće trebali biti ekonomični s brojem korištenih tokena. Na primjer, možemo li formulirati prompt tako da upotrijebimo manje tokena?

  Za promjenu korištenih tokena možete koristiti parametar `max_output_tokens`. Na primjer, ako želite koristiti 100 tokena, napravili biste ovako:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimentiranje s temperaturom**. Temperatura je nešto o čemu dosad nismo govorili, ali je važan kontekst za performanse našeg programa. Što je vrijednost temperature viša, to će rezultat biti nasumičniji. Suprotno, što je temperatura niža, to je izlaz predvidljiviji. Razmislite želite li varijaciju u vašem izlazu ili ne.

  Za promjenu temperature, možete koristiti parametar `temperature`. Na primjer, ako želite koristiti temperaturu 0,5, učinili biste ovako:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Napomena, što je bliže 1.0, to je izlaz raznovrsniji.

- **Modeli zaključivanja ne koriste `temperature`**. Ovo je važan pomak u 2026. Trenutni, ne-deprekirani modeli u Microsoft Foundry su **modeli zaključivanja** (GPT-5 obitelj, o-serija) - i oni **ne podržavaju `temperature` ni `top_p`** (niti `max_tokens`; koristite `max_output_tokens`). Ako pošaljete `temperature` na `gpt-5-mini` dobit ćete grešku "parameter not supported". Dakle, da isprobate primjer s temperaturom gore, usmjerite ga na model koji još podržava kontrole uzorkovanja - na primjer otvoreni **Llama** model poput `Llama-3.3-70B-Instruct` iz [Microsoft Foundry kataloga modela](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), pozvan putem Foundry Models / Azure AI Inference endpointa (na isti način kao i `githubmodels-*` primjeri). Za modele zaključivanja poput GPT-5, upravljate izlazom drugačije:
  - **Prompt inženjering** - jasne upute, primjeri i strukturirani izlaz (pogledajte lekciju [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) rade posao koji su nekad radili kontroleri uzorkovanja.
  - **Kontrole zaključivanja** - parametri poput napora/riječitosti zaključivanja balansiraju dubinu zaključivanja protiv latencije i troška.

  Ukratko: `temperature`/`top_p` su i dalje važeći na mnogim modelima (Llama, Mistral, Phi i GPT-4.x obitelj - iako GPT-4.x biva deprikirana), ali smjer kretanja je prompt inženjering + kontrole zaključivanja na modelima zaključivanja kao što je GPT-5.

## Zadatak

Za ovaj zadatak možete odabrati što ćete napraviti.

Evo nekoliko prijedloga:

- Doradite aplikaciju za generiranje recepata kako biste je dodatno poboljšali. Igrajte se s vrijednostima temperature i promptovima da vidite što možete smisliti.
- Izradite "studijskog prijatelja". Ta aplikacija treba moći odgovarati na pitanja o nekoj temi, na primjer Python; mogli biste imati promptove kao "Što je određena tema u Pythonu?", ili prompt koji kaže, pokaži mi kod za određenu temu itd.
- Povijesni bot, učinite povijest živom, naredite botu da glumi određenu povijesnu osobu i postavljajte mu pitanja o njegovom životu i vremenu.

## Rješenje

### Studijski prijatelj

Ispod je početni prompt, pogledajte kako ga možete koristiti i prilagoditi po želji.

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

1. Kontrolira koliko je izlaz nasumičan.
1. Kontrolira koliko je odgovor opsežan.
1. Kontrolira koliko se tokena koristi.

## 🚀 Izazov

Dok radite na zadatku, pokušajte mijenjati temperaturu, postavite ju na 0, 0.5 i 1. Sjetite se da je 0 najmanje varijabilno, a 1 najviše. Koja vrijednost najbolje funkcionira za vašu aplikaciju?

## Sjajan rad! Nastavite svoje učenje

Nakon što završite ovu lekciju, pogledajte našu [kolekciju učenja o Generativnoj AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da nastavite usavršavati svoje znanje o Generativnoj AI!

Idite na Lekciju 7 gdje ćemo pogledati kako [izgraditi chat aplikacije](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->