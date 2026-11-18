# Izgradnja aplikacija za generiranje teksta

[![Izgradnja aplikacija za generiranje teksta](../../../translated_images/hr/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite na gornju sliku kako biste pogledali video ovog poglavlja)_

Do sada ste kroz ovaj kurikulum vidjeli osnovne koncepte poput promptova pa čak i cijelu disciplinu nazvanu "prompt inženjering". Mnogi alati s kojima možete komunicirati poput ChatGPT-a, Office 365, Microsoft Power Platforme i drugih, podržavaju korištenje promptova za postizanje nečega.

Da biste takvo iskustvo dodali u aplikaciju, morate razumjeti koncepte poput promptova, dovršenja i odabrati biblioteku za rad. Upravo to ćete naučiti u ovom poglavlju.

## Uvod

U ovom poglavlju ćete:

- Naučiti o openai biblioteci i njezinim osnovnim konceptima.
- Izgraditi aplikaciju za generiranje teksta koristeći openai.
- Razumjeti kako koristiti koncepte poput prompta, temperature i tokena za izradu aplikacije za generiranje teksta.

## Ciljevi učenja

Na kraju ovog poglavlja moći ćete:

- Objasniti što je aplikacija za generiranje teksta.
- Izgraditi aplikaciju za generiranje teksta koristeći openai.
- Konfigurirati svoju aplikaciju da koristi više ili manje tokena i također promijeniti temperaturu za raznoliki izlaz.

## Što je aplikacija za generiranje teksta?

Obično kada izrađujete aplikaciju, ona ima neku vrstu sučelja kao što je sljedeće:

- Na temelju naredbi. Konzolne aplikacije su tipične aplikacije gdje upisujete naredbu i ona izvršava zadatak. Na primjer, `git` je aplikacija zasnovana na naredbama.
- Korisničko sučelje (UI). Neke aplikacije imaju grafička korisnička sučelja (GUI) gdje klikate gumbe, unosite tekst, birate opcije i slično.

### Konzolne i UI aplikacije su ograničene

Usporedite to s konzolnom aplikacijom gdje upisujete naredbu:

- **Ograničeno je**. Ne možete jednostavno upisati bilo koju naredbu, samo one koje aplikacija podržava.
- **Specifično za jezik**. Neke aplikacije podržavaju više jezika, ali po zadanim postavkama aplikacija je izrađena za određeni jezik, čak i ako možete dodati podršku za više jezika.

### Prednosti aplikacija za generiranje teksta

Pa kako se aplikacija za generiranje teksta razlikuje?

U aplikaciji za generiranje teksta imate veću fleksibilnost, niste ograničeni na skup naredbi ili određeni jezik unosa. Umjesto toga, možete komunicirati s aplikacijom koristeći prirodni jezik. Još jedna prednost je da već komunicirate s izvorom podataka koji je treniran na opsežnom korpusu informacija, dok bi tradicionalna aplikacija mogla biti ograničena onim što je u bazi podataka.

### Što mogu izgraditi pomoću aplikacije za generiranje teksta?

Postoje mnoge stvari koje možete izgraditi. Na primjer:

- **Chatbot**. Chatbot koji odgovara na pitanja o temama poput vaše tvrtke i njezinih proizvoda mogao bi biti dobar izbor.
- **Pomoćnik**. LLM-ovi su izvrsni u stvarima poput sažimanja teksta, dobivanja uvida iz teksta, proizvodnje teksta poput životopisa i slično.
- **Pomoćnik za kod**. Ovisno o jezičnom modelu koji koristite, možete izgraditi pomoćnika za kod koji pomaže kod pisanju koda. Na primjer, možete koristiti proizvod poput GitHub Copilot kao i ChatGPT za pomoć u pisanju koda.

## Kako mogu započeti?

Pa, trebate pronaći način integracije s LLM-om što obično podrazumijeva sljedeća dva pristupa:

- Koristiti API. Ovdje sastavljate web zahtjeve s vašim promptom i dobivate generirani tekst nazad.
- Koristiti biblioteku. Biblioteke pomažu enkapsulirati API pozive i olakšavaju njihovu uporabu.

## Biblioteke/SDK-ovi

Postoji nekoliko poznatih biblioteka za rad s LLM-ovima kao:

- **openai**, ova biblioteka olakšava povezivanje s vašim modelom i slanje promptova.

Zatim postoje biblioteke koje rade na višoj razini, kao:

- **Langchain**. Langchain je dobro poznat i podržava Python.
- **Semantic Kernel**. Semantic Kernel je biblioteka tvrtke Microsoft koja podržava jezike C#, Python i Java.

## Prva aplikacija koristeći openai

Pogledajmo kako možemo izgraditi našu prvu aplikaciju, koje biblioteke trebamo, koliko je potrebno i slično.

### Instalirajte openai

Postoje mnoge biblioteke za interakciju s OpenAI ili Azure OpenAI. Moguće je koristiti i razne programske jezike poput C#, Python, JavaScript, Java i druge. Odabrali smo koristiti Python biblioteku `openai`, pa ćemo koristiti `pip` za njezinu instalaciju.

```bash
pip install openai
```

### Kreirajte resurs

Potrebno je napraviti sljedeće korake:

- Kreirajte račun na Azureu [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Dobijte pristup Azure OpenAI. Idite na [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) i zatražite pristup.

  > [!NOTE]
  > U vrijeme pisanja potrebno je aplicirati za pristup Azure OpenAI.

- Instalirajte Python <https://www.python.org/>
- Kreirali ste Azure OpenAI Service resurs. Pogledajte ovaj vodič kako [kreirati resurs](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Pronađite API ključ i krajnju točku

U ovom trenutku trebate svom `openai` library reći koji API ključ koristiti. Da biste pronašli svoj API ključ, idite u odjeljak "Keys and Endpoint" vašeg Azure OpenAI resursa i kopirajte vrijednost "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sada kada imate ove podatke kopirane, uputimo biblioteke da ih koriste.

> [!NOTE]
> Vrijedi odvojiti svoj API ključ iz koda. To možete učiniti korištenjem varijabli okoline.
>
> - Postavite varijablu okoline `OPENAI_API_KEY` na svoj API ključ.
>   `export OPENAI_API_KEY='sk-...'`

### Postavite konfiguraciju za Azure

Ako koristite Azure OpenAI (sada dio Microsoft Foundry), evo kako postaviti konfiguraciju. Koristimo standardni klijent `OpenAI` usmjeren na Azure OpenAI `/openai/v1/` endpoint, koji radi s Responses API-em i ne treba `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Gore postavljamo sljedeće:

- `api_key`, to je vaš API ključ pronađen u Azure Portalu ili Microsoft Foundry portalu.
- `base_url`, to je vaš Foundry resurs endpoint s `/openai/v1/` dodanim na kraj. Stabilna v1 krajnja točka radi u OpenAI-u i Azure OpenAI-u bez upravljanja `api_version`.

> [!NOTE] > `os.environ` čita varijable okoline. Možete ga koristiti za čitanje varijabli okoline poput `AZURE_OPENAI_API_KEY` i `AZURE_OPENAI_ENDPOINT`. Postavite te varijable okoline u svojem terminalu ili koristeći biblioteku poput `dotenv`.

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

### Višekratni razgovori

Responses API je dobro prilagođen za jednokratno generiranje teksta kao i višekratne chatbotove - pružate popis poruka u `input` kako biste izgradili razgovor:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Više o ovoj funkcionalnosti u jednom od nadolazećih poglavlja.

## Vježba - vaša prva aplikacija za generiranje teksta

Sada kada smo naučili kako postaviti i konfigurirati openai, vrijeme je za izgradnju vaše prve aplikacije za generiranje teksta. Za izradu aplikacije slijedite ove korake:

1. Kreirajte virtualno okruženje i instalirajte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ako koristite Windows, upišite `venv\Scripts\activate` umjesto `source venv/bin/activate`.

   > [!NOTE]
   > Pronađite svoj Azure OpenAI ključ tako da odete na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), potražite `Open AI` i odaberete `Open AI resource`, zatim odaberete `Keys and Endpoint` te kopirajte vrijednost `Key 1`.

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
   > Ako koristite obični OpenAI (ne Azure), koristite `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (bez `base_url`) i proslijedite ime modela poput `gpt-5-mini` umjesto imena deploymenta.

   Trebali biste vidjeti izlaz poput sljedećeg:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Različite vrste promptova za različite stvari

Sada ste vidjeli kako generirati tekst koristeći prompt. Čak imate program koji radi i koji možete modificirati i mijenjati da generira različite vrste teksta.

Promptovi se mogu koristiti za različite zadatke. Na primjer:

- **Generirati tip teksta**. Na primjer, možete generirati pjesmu, pitanja za kviz itd.
- **Pretraživati informacije**. Možete koristiti promptove za traženje informacija poput primjera 'Što znači CORS u web razvoju?'.
- **Generirati kod**. Možete koristiti promptove za generiranje koda, primjerice za razvoj regularnog izraza za validaciju emailova ili za generiranje cijelog programa, poput web aplikacije?

## Praktičniji primjer: generator recepata

Zamislite da imate sastojke kod kuće i želite nešto skuhati. Za to vam treba recept. Jedan način pronalaska recepata je korištenje tražilice, a možete upotrijebiti i LLM za tu svrhu.

Mogli biste napisati prompt ovako:

> "Pokaži mi 5 recepata za jelo s sljedećim sastojcima: piletina, krumpir i mrkva. Za svaki recept navedite sve korištene sastojke"

S obzirom na navedeni prompt, mogli biste dobiti odgovor sličan:

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

Ovaj rezultat je izvrstan, znam što ću skuhati. U ovom trenutku korisna poboljšanja bi bila:

- Filtrirati sastojke koje ne volim ili na koje sam alergičan.
- Napraviti popis za kupovinu, u slučaju da nemam sve sastojke kod kuće.

Za ove slučajeve dodajmo dodatni prompt:

> "Molim ukloni recepte s češnjakom jer sam alergičan i zamijeni ga nečim drugim. Također, molim napravi popis za kupovinu za recepte, uzimajući u obzir da imam piletinu, krumpir i mrkvu kod kuće."

Sada imate novi rezultat, a to je:

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

To su vaši pet recepata bez spomena češnjaka, a imate i popis za kupovinu uzimajući u obzir što već imate kod kuće.

## Vježba - izgradite generator recepata

Sada kada smo prikazali scenarij, napisimo kod koji odgovara ovom scenariju. Za to slijedite ove korake:

1. Koristite postojeću datoteku _app.py_ kao početnu točku
1. Pronađite varijablu `prompt` i promijenite njezin kod u sljedeće:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ako sada pokrenete kod, trebali biste vidjeti izlaz sličan:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NAPOMENA, vaš LLM nije determinističan, pa možete dobiti različite rezultate svaki put kada pokrenete program.

   Odlično, pogledajmo kako možemo stvari poboljšati. Za poboljšanje želimo osigurati da je kod fleksibilan, tako da se sastojci i broj recepata mogu lako mijenjati.

1. Promijenimo kod na sljedeći način:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testni primjer korištenja koda mogao bi izgledati ovako:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Poboljšaj dodavanjem filtera i popisa za kupovinu

Sada imamo radnu aplikaciju koja može proizvesti recepte, a fleksibilna je jer se oslanja na unos korisnika, i za broj recepata i za sastojke koji se koriste.

Da bismo je dodatno poboljšali, želimo dodati sljedeće:

- **Filtrirati sastojke**. Želimo moći filtrirati sastojke koje ne volimo ili na koje smo alergični. Da bismo napravili ovu izmjenu, možemo editirati postojeći prompt i na njegov kraj dodati uvjet za filtriranje ovako:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Gore smo na kraj prompta dodali `{filter}` i također hvatajmo vrijednost filtera od korisnika.

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

  Kao što vidite, svi recepti koji sadrže mlijeko su filtrirani. Ali ako ste netolerantni na laktozu, možda ćete htjeti filtrirati i recepte sa sirom, pa je potrebno biti precizan.

- **Proizvesti popis za kupovinu**. Želimo napraviti popis za kupovinu, uzimajući u obzir što već imamo kod kuće.

  Za ovu funkcionalnost mogli bismo pokušati riješiti sve u jednom promptu ili bismo to mogli podijeliti u dva prompta. Pokušajmo s ovim drugim pristupom. Ovdje predlažemo dodati dodatni prompt, ali da bi to funkcioniralo, trebamo dodati rezultat prvog prompta kao kontekst drugom promptu.

  Pronađite dio u kodu koji ispisuje rezultat iz prvog prompta i ispod njega dodajte sljedeći kod:

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

  1. Konstruiramo novi prompt dodavanjem rezultata iz prvog prompta novom promptu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Izvršavamo novi zahtjev, ali također uzimajući u obzir broj tokena kojeg smo tražili u prvom promptu, pa ovoga puta kažemo da je `max_output_tokens` 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Kad isprobamo ovaj kod, dobit ćemo sljedeći ispis:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Poboljšajte vašu postavku

Ono što do sada imamo je kod koji radi, ali postoje neke prilagodbe koje bismo trebali napraviti da dalje poboljšamo stvari. Neke stvari koje bismo trebali učiniti su:

- **Odvojite tajne od koda**, poput API ključa. Tajne ne pripadaju u kod i trebale bi se pohraniti na sigurno mjesto. Za odvajanje tajni od koda možemo koristiti varijable okoline i biblioteke poput `python-dotenv` za učitavanje iz datoteke. Evo kako bi to izgledalo u kodu:

  1. Kreirajte `.env` datoteku sa sljedećim sadržajem:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Napomena, za Azure OpenAI u Microsoft Foundry trebate umjesto toga postaviti sljedeće varijable okoline:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     U kodu biste varijable okoline učitali na sljedeći način:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Riječ o duljini tokena**. Trebali bismo razmotriti koliko tokena treba za generiranje teksta koji želimo. Tokeni koštaju novac, stoga bismo, gdje je moguće, trebali nastojati biti ekonomični s brojem tokena koje koristimo. Na primjer, možemo li formulirati prompt tako da koristimo manje tokena?

  Za promjenu broja korištenih tokena možete koristiti parametar `max_output_tokens`. Na primjer, ako želite koristiti 100 tokena, učinili biste:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimentiranje s temperaturom**. Temperatura je nešto o čemu do sada nismo govorili, ali je važan kontekst za to kako naš program radi. Što je temperatura veća, ishod je nasumičniji. Suprotno tome, što je temperatura niža, ishod je predvidljiviji. Razmotrite želite li varijaciju u svom rezultatu ili ne.

  Za promjenu temperature možete koristiti parametar `temperature`. Na primjer, ako želite koristiti temperaturu 0,5, učinili biste:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Napomena, što bliže 1,0, to je ishod raznovrsniji.

- **Modeli za rezoniranje ne koriste `temperature`**. Ovo je važna promjena za 2026. Trenutni, ne-zastarjeli modeli na Microsoft Foundry su **modeli za rezoniranje** (obitelj GPT-5, o-serija) - i oni **ne podržavaju `temperature` ili `top_p`** (niti `max_tokens`; koristite `max_output_tokens`). Ako pošaljete `temperature` na `gpt-5-mini` dobit ćete grešku "parametar nije podržan". Dakle, da biste isprobali primjer temperature gore, usmjerite to na model koji još uvijek podržava kontrole uzorkovanja - na primjer otvoreni **Llama** model poput `Llama-3.3-70B-Instruct` iz [kataloga modela Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), pozvan putem Foundry Models / Azure AI Inference API-ja (na isti način kao i `githubmodels-*` primjeri). Za modele za rezoniranje poput GPT-5, rezultat se vodi drugačije:
  - **Prompt inženjerstvo** - jasne upute, primjeri i strukturirani ishod (pogledajte lekciju [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) rade posao koji su nekada radili kontroleri uzorkovanja.
  - **Kontrole rezoniranja** - parametri poput truda/verbalnosti rezoniranja balansiraju dubinu rezoniranja s latencijom i troškovima.

  Ukratko: `temperature`/`top_p` su i dalje valjani na mnogim modelima (Llama, Mistral, Phi i obitelj GPT-4.x - iako GPT-4.x ide prema zastarjevanju), ali smjer kretanja je prompt inženjerstvo + kontrole rezoniranja na modelima za rezoniranje poput GPT-5.

## Zadatak

Za ovaj zadatak možete odabrati što ćete izraditi.

Evo nekoliko prijedloga:

- Doradite aplikaciju za generiranje recepata da je dodatno poboljšate. Igrajte se s vrijednostima temperature i promptovima kako biste vidjeli što možete osmisliti.
- Izradite "studijskog prijatelja". Ova aplikacija bi trebala moći odgovarati na pitanja o nekoj temi, na primjer Python, mogli biste imati promptove poput "Što je određena tema u Pythonu?", ili prompt koji kaže, pokaži mi kod za određenu temu itd.
- Povijesni bot, učinite povijest živom, zadajte botu da glumi određenog povijesnog lika i postavite mu pitanja o njegovom životu i vremenu.

## Rješenje

### Studijski prijatelj

Ispod je početni prompt, pogledajte kako ga možete koristiti i prilagoditi svojim željama.

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

Čemu služi pojam temperatura?

1. Kontrolira koliko je ishod nasumičan.
1. Kontrolira koliko je odgovor velik.
1. Kontrolira koliko se tokena koristi.

## 🚀 Izazov

Tijekom rada na zadatku, pokušajte varirati temperaturu, postavite je na 0, 0.5 i 1. Sjetite se da je 0 najmanje varijabilno, a 1 najviše. Koja vrijednost najbolje radi za vašu aplikaciju?

## Odličan posao! Nastavite s učenjem

Nakon što završite ovu lekciju, pogledajte našu [kolekciju za učenje o generativnoj umjetnoj inteligenciji](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili podizati razinu svog znanja o generativnoj AI!

Pređite na Lekciju 7 gdje ćemo proučiti kako [izraditi chat aplikacije](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->