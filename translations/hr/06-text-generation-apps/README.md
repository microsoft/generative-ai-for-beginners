# Izrada aplikacija za generiranje teksta

[![Izrada aplikacija za generiranje teksta](../../../translated_images/hr/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite na gornju sliku da pogledate video ovog poglavlja)_

Do sada ste kroz ovaj kurikulum vidjeli da postoje osnovni koncepti poput promptova i čak cijela disciplina nazvana "prompt inženjering". Mnogi alati s kojima možete komunicirati poput ChatGPT-a, Office 365, Microsoft Power Platforme i drugih, podržavaju korištenje promptova za ostvarivanje nečega.

Da biste takvo iskustvo dodali aplikaciji, morate razumjeti koncepte poput promptova, dovršetaka i odabrati biblioteku za rad. Upravo to ćete naučiti u ovom poglavlju.

## Uvod

U ovom poglavlju ćete:

- Naučiti o biblioteci openai i njezinim osnovnim konceptima.
- Izgraditi aplikaciju za generiranje teksta koristeći openai.
- Razumjeti kako koristiti koncepte poput prompta, temperature i tokena za izradu aplikacije za generiranje teksta.

## Ciljevi učenja

Na kraju ove lekcije, moći ćete:

- Objasniti što je aplikacija za generiranje teksta.
- Izgraditi aplikaciju za generiranje teksta koristeći openai.
- Konfigurirati svoju aplikaciju da koristi više ili manje tokena te također promijeniti temperaturu za raznolike izlaze.

## Što je aplikacija za generiranje teksta?

Obično, kad izrađujete aplikaciju, ona ima neki oblik sučelja poput sljedećeg:

- Bazirano na naredbama. Konzolne aplikacije su tipične aplikacije u koje upisujete naredbu i one izvršavaju zadatak. Na primjer, `git` je aplikacija bazirana na naredbama.
- Korisničko sučelje (UI). Neke aplikacije imaju grafička korisnička sučelja (GUI) gdje klikate tipke, unosite tekst, birate opcije i slično.

### Konzolne i UI aplikacije su ograničene

Usporedite to s aplikacijom baziranom na naredbama u koju upisujete naredbu:

- **Ograničeno je**. Ne možete upisivati bilo koju naredbu, samo one koje aplikacija podržava.
- **Specifično za jezik**. Neke aplikacije podržavaju mnoge jezike, no prema zadanim postavkama aplikacija je izrađena za određeni jezik, iako se može dodati podrška za dodatne jezike.

### Prednosti aplikacija za generiranje teksta

Pa kako je aplikacija za generiranje teksta drugačija?

U aplikaciji za generiranje teksta imate veću fleksibilnost, niste ograničeni na skup naredbi ili specifični ulazni jezik. Umjesto toga, koristite prirodni jezik za interakciju s aplikacijom. Druga prednost je što već radite s izvorom podataka koji je treniran na ogromnom korpusu informacija, dok tradicionalna aplikacija možda ima ograničenja u bazi podataka.

### Što mogu izraditi s aplikacijom za generiranje teksta?

Možete napraviti mnogo stvari. Primjerice:

- **Chatbot**. Chatbot koji odgovara na pitanja o temama poput vaše tvrtke i njezinih proizvoda mogao bi biti dobar izbor.
- **Pomoćnik**. LLM-ovi su odlični u stvarima poput sažimanja teksta, dobivanja uvida iz teksta, stvaranja tekstova poput životopisa i slično.
- **Pomoćnik za kod**. Ovisno o modelu jezika koji koristite, možete izraditi pomoćnika za kod koji pomaže pri pisanju koda. Na primjer, možete koristiti proizvode poput GitHub Copilot i ChatGPT za pomoć pri pisanju koda.

## Kako mogu započeti?

Pa, morate pronaći način da se povežete s LLM-om što obično podrazumijeva sljedeća dva pristupa:

- Koristiti API. Tu sastavljate web zahtjeve sa svojim promptom i dobivate generirani tekst nazad.
- Koristiti biblioteku. Biblioteke pomažu enkapsulirati API pozive i olakšavaju njihovo korištenje.

## Biblioteke/SDK-ovi

Postoji nekoliko poznatih biblioteka za rad s LLM-ovima poput:

- **openai**, ova biblioteka olakšava povezivanje s vašim modelom i slanje promptova.

Zatim postoje biblioteke koje rade na višoj razini poput:

- **Langchain**. Langchain je dobro poznat i podržava Python.
- **Semantic Kernel**. Semantic Kernel je Microsoftova biblioteka koja podržava jezike C#, Python i Java.

## Prva aplikacija koristeći openai

Pogledajmo kako možemo napraviti prvu aplikaciju, koje biblioteke trebamo, koliko je potrebno i slično.

### Instalirajte openai

Postoji mnogo biblioteka za interakciju s OpenAI ili Azure OpenAI. Moguće je koristiti različite programske jezike poput C#, Python, JavaScript, Java i druge. Odabrali smo koristiti Python biblioteku `openai`, pa ćemo instalirati pomoću `pip` alata.

```bash
pip install openai
```

### Kreirajte resurs

Morate napraviti sljedeće korake:

- Kreirajte račun na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Dobite pristup Azure OpenAI. Idite na [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) i zatražite pristup.

  > [!NOTE]
  > U trenutku pisanja, potrebno je podnijeti zahtjev za pristup Azure OpenAI.

- Instalirajte Python <https://www.python.org/>
- Napravite Azure OpenAI Service resurs. Pogledajte vodič kako [kreirati resurs](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Pronađite API ključ i endpoint

Sada trebate reći vašoj `openai` biblioteci koji API ključ koristiti. Da pronađete vaš API ključ, idite u odjeljak "Keys and Endpoint" vašeg Azure OpenAI resursa i kopirajte vrijednost "Key 1".

![Keys and Endpoint resource blade u Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sada kad imate ove podatke kopirane, uputimo biblioteke da ih koriste.

> [!NOTE]
> Vrijedi odvojiti vaš API ključ od vašeg koda. To možete učiniti koristeći varijable okruženja.
>
> - Postavite varijablu okruženja `OPENAI_API_KEY` na vaš API ključ.
>   `export OPENAI_API_KEY='sk-...'`

### Postavljanje konfiguracije za Azure

Ako koristite Azure OpenAI (sada dio Microsoft Foundry), evo kako postaviti konfiguraciju. Koristimo standardnog `OpenAI` klijenta usmjerenog na Azure OpenAI `/openai/v1/` endpoint, koji radi s Responses API-jem i ne treba `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Gore smo postavili sljedeće:

- `api_key`, to je vaš API ključ pronađen u Azure portalu ili Microsoft Foundry portalu.
- `base_url`, to je endpoint Foundry resursa uz dodatak `/openai/v1/`. Stabilni v1 endpoint radi za OpenAI i Azure OpenAI bez potrebe za upravljanjem `api_version`.

> [!NOTE] > `os.environ` čita varijable okruženja. Možete ga koristiti za dohvaćanje varijabli poput `AZURE_OPENAI_API_KEY` i `AZURE_OPENAI_ENDPOINT`. Postavite ove varijable u vašem terminalu ili koristeći biblioteku poput `dotenv`.

## Generiranje teksta

Način generiranja teksta je korištenje Responses API-ja putem metode `responses.create`. Evo primjera:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # ovo je ime vaše implementacije modela
    input=prompt,
    store=False,
)
print(response.output_text)
```

U gornjem kodu stvaramo odgovor i prosljeđujemo model koji želimo koristiti i prompt. Zatim ispisujemo generirani tekst preko `response.output_text`.

### Višerundni razgovori

Responses API je prikladan za generiranje teksta u jednoj rundi, kao i za višerundne chatbotove – pružate popis poruka u `input` da izgradite razgovor:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Više o ovoj funkcionalnosti u nadolazećem poglavlju.

## Vježba – vaša prva aplikacija za generiranje teksta

Sada kada smo naučili kako postaviti i konfigurirati openai, vrijeme je da napravite svoju prvu aplikaciju za generiranje teksta. Za izradu aplikacije slijedite ove korake:

1. Kreirajte virtualno okruženje i instalirajte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ako koristite Windows, upišite `venv\Scripts\activate` umjesto `source venv/bin/activate`.

   > [!NOTE]
   > Pronađite svoj Azure OpenAI ključ tako da odete na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), potražite `Open AI`, odaberete `Open AI resource`, zatim `Keys and Endpoint` i kopirate vrijednost `Key 1`.

1. Napravite datoteku _app.py_ i stavite sljedeći kod:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # dodajte svoj kod dovršetka
   prompt = "Complete the following: Once upon a time there was a"

   # napravite zahtjev koristeći Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # ispišite odgovor
   print(response.output_text)
   ```

   > [!NOTE]
   > Ako koristite obični OpenAI (ne Azure), upotrijebite `client = OpenAI(api_key="<zamijenite ovo vašim OpenAI ključem>")` (bez `base_url`) i proslijedite naziv modela poput `gpt-5-mini` umjesto imena deploymenta.

   Trebali biste vidjeti rezultat poput sljedećeg:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Različite vrste promptova, za različite zadatke

Sada ste vidjeli kako generirati tekst koristeći prompt. Čak imate program koji radi i koji možete mijenjati i prilagođavati za generiranje različitih tipova teksta.

Promptovi se mogu koristiti za sve vrste zadataka. Primjerice:

- **Generiranje vrste teksta**. Na primjer, možete generirati pjesmu, pitanja za kviz i slično.
- **Pretraživanje informacija**. Možete koristiti promptove za traženje informacija poput primjera "Što znači CORS u web razvoju?".
- **Generiranje koda**. Možete koristiti promptove za generiranje koda, na primjer za razvoj regularnog izraza koji provjerava e-mailove ili za generiranje cijelog programa, poput web aplikacije.

## Praktičniji primjer: generator recepata

Zamislite da imate sastojke kod kuće i želite nešto skuhati. Za to vam treba recept. Jedan način za pronalaženje recepata je korištenje tražilice, a drugi je korištenje LLM-a.

Možete napisati prompt ovako:

> "Pokaži mi 5 recepata za jelo sa sljedećim sastojcima: piletina, krumpir i mrkva. Za svaki recept navedite sve korištene sastojke"

S obzirom na ovaj prompt, mogli biste dobiti odgovor sličan ovom:

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

Ovaj rezultat je dobar, znam što kuhati. U ovom trenutku, korisna poboljšanja mogla bi biti:

- Filtriranje sastojaka koje ne volim ili na koje sam alergičan.
- Izrada popisa za kupovinu, u slučaju da nemam sve sastojke kod kuće.

Za ove slučajeve, dodajmo dodatni prompt:

> "Molim ukloni recepte koji sadrže češnjak jer sam alergičan i zamijeni ga nečim drugim. Također, molim napravi popis za kupovinu za recepte, uzimajući u obzir da već imam piletinu, krumpir i mrkvu kod kuće."

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

To su vaši pet recepata bez češnjaka, a uz to imate i popis za kupovinu uzimajući u obzir što već imate kod kuće.

## Vježba – izradite generator recepata

Sada kad smo prikazali scenarij, napišimo kod koji odgovara ovom scenariju. Za to slijedite ove korake:

1. Koristite postojeću datoteku _app.py_ kao polaznu točku
1. Pronađite varijablu `prompt` i promijenite njezin kod na sljedeći:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ako sada pokrenete kod, trebali biste vidjeti rezultat sličan ovome:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NAPOMENA, vaš LLM je nedeterministički, tako da možete dobiti različite rezultate svaki put kad pokrenete program.

   Super, pogledajmo kako možemo poboljšati stvari. Za poboljšanje želimo osigurati fleksibilnost koda, tako da se sastojci i broj recepata mogu jednostavno mijenjati.

1. Izmijenimo kod na sljedeći način:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolirajte broj recepata u upit i sastojke
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Ispitivanje koda moglo bi izgledati ovako:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Poboljšanje dodavanjem filtera i popisa za kupovinu

Sada imamo radnu aplikaciju koja može proizvodi recepte i fleksibilna je jer se oslanja na unos korisnika, kako na broj recepata tako i na korištene sastojke.

Da bismo je dodatno poboljšali, želimo dodati sljedeće:

- **Filtriranje sastojaka**. Želimo moći filtrirati sastojke koje ne volimo ili na koje smo alergični. Za tu promjenu možemo urediti postojeći prompt i na kraj dodati uvjet filtera ovako:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Gore dodajemo `{filter}` na kraj prompta i također dohvaćamo vrijednost filtera od korisnika.

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

  Kao što možete vidjeti, recepti s mlijekom su filtrirani. No, ako ste netolerantni na laktozu, možda ćete htjeti filtrirati i recepte s sirom, pa je važno biti precizan.


- **Napravi popis za kupovinu**. Želimo napraviti popis za kupovinu, uzimajući u obzir što već imamo kod kuće.

  Za ovu funkcionalnost, mogli bismo pokušati riješiti sve u jednom promptu ili to podijeliti u dva prompta. Pokušajmo drugi pristup. Ovdje predlažemo dodavanje dodatnog prompta, ali da bi to funkcioniralo, trebamo dodati rezultat prvog prompta kao kontekst drugom promptu.

  Pronađi dio u kodu koji ispisuje rezultat iz prvog prompta i dodaj sljedeći kod ispod:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # ispiši odgovor
  print("Shopping list:")
  print(response.output_text)
  ```

  Obrati pažnju na sljedeće:

  1. Kreiramo novi prompt dodavanjem rezultata iz prvog prompta u novi prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Napravimo novi zahtjev, pri čemu također razmatramo broj tokena koje smo tražili u prvom promptu, pa ovoga puta kažemo `max_output_tokens` je 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Izvršavajući ovaj kod, sada dobivamo sljedeći izlaz:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Poboljšaj svoju postavu

Dosad imamo kod koji radi, ali postoje neka poboljšanja koja bismo trebali napraviti da stvari dodatno unaprijedimo. Neke stvari koje trebamo učiniti su:

- **Odvoji tajne od koda**, poput API ključa. Tajne ne pripadaju u kod i trebale bi se čuvati na sigurnom mjestu. Da bismo odvojili tajne od koda, možemo koristiti varijable okoline i biblioteke poput `python-dotenv` za učitavanje iz datoteke. Evo kako bi to izgledalo u kodu:

  1. Kreiraj `.env` datoteku sa sljedećim sadržajem:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Napomena, za Azure OpenAI u Microsoft Foundry, morate umjesto toga postaviti sljedeće varijable okoline:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     U kodu, varijable okoline biste učitali na sljedeći način:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Riječ o duljini tokena**. Trebali bismo razmotriti koliko tokena trebamo za generiranje željenog teksta. Tokeni koštaju novac, pa bismo tamo gdje je moguće trebali biti štedljivi s brojem tokena koje koristimo. Na primjer, možemo li oblikovati prompt tako da koristimo manje tokena?

  Da promijeniš broj korištenih tokena, možeš koristiti parametar `max_output_tokens`. Na primjer, ako želiš koristiti 100 tokena, napravio bi to ovako:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimentiranje s temperaturom**. Temperatura je nešto što do sada nismo spominjali, ali je važan kontekst za performanse našeg programa. Što je vrijednost temperature viša, izlaz je nasumičniji. Obrnuto, što je temperatura niža, izlaz je predvidljiviji. Razmisli želiš li varijaciju u izlazu ili ne.

  Da promijeniš temperaturu, možeš koristiti parametar `temperature`. Na primjer, ako želiš koristiti temperaturu od 0.5, napravio bi to ovako:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Napomena, što je bliže 1.0, izlaz je raznovrsniji.

- **Razložni modeli ne koriste `temperature`**. Ovo je važan pomak za 2026. Trenutni modeli koji nisu zastarjeli na Microsoft Foundry su **razložni modeli** (obitelj GPT-5, o-serija) - i oni **ne podržavaju `temperature` ili `top_p`** (kao ni `max_tokens`; koristi `max_output_tokens`). Ako pošalješ `temperature` modelu `gpt-5-mini`, dobit ćeš grešku "parameter not supported". Dakle, za isprobati primjer temperature gore, usmjeri ga na model koji još podržava kontrole uzorkovanja - na primjer otvoreni **Llama** model poput `Llama-3.3-70B-Instruct` iz [Microsoft Foundry kataloga modela](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), pozvan preko Foundry Models / Azure AI Inference endpointa (na isti način kao uzorci `githubmodels-*`). Za razložne modele poput GPT-5, izlaz se usmjerava drugačije:
  - **Prompt inženjering** - jasne upute, primjeri i strukturirani izlaz (vidi lekciju [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) rade posao koji su ranije radile kontrole uzorkovanja.
  - **Kontrole razmišljanja** - parametri poput truda/verbositeta razmišljanja balansiraju dubinu razmišljanja s latencijom i cijenom.

  Ukratko: `temperature`/`top_p` su još uvijek važeći za mnoge modele (Llama, Mistral, Phi i obitelj GPT-4.x - iako se GPT-4.x ukida), ali smjer razvoja su prompt inženjering + kontrole razmišljanja na razloznim modelima poput GPT-5.

## Zadatak

Za ovaj zadatak možeš izabrati što ćeš napraviti.

Evo nekoliko prijedloga:

- Doradi aplikaciju za generator recepata kako bi je dodatno unaprijedio. Igraj se s vrijednostima temperature i promptovima da vidiš što možeš smisliti.
- Napravi "školskog partnera". Ova aplikacija bi trebala moći odgovarati na pitanja o nekoj temi, na primjer Python, gdje možeš imati promptove poput "Što je određena tema u Pythonu?", ili prompt koji kaže, pokaži mi kod za određenu temu itd.
- Povijesni bot, učini povijest živom, uputi bota da glumi određeni povijesni lik i postavljaj mu pitanja o njegovom životu i vremenu.

## Rješenje

### Školski partner

Ispod je početni prompt, pogledaj kako ga možeš koristiti i prilagoditi svojem ukusu.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Povijesni bot

Evo nekoliko promptova koje možeš koristiti:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Provjera znanja

Što radi pojam temperatura?

1. Kontrolira koliko je izlaz nasumičan.
1. Kontrolira koliko je odgovor velik.
1. Kontrolira koliko se tokena koristi.

## 🚀 Izazov

Dok radiš na zadatku, pokušaj mijenjati temperaturu, postavi je na 0, 0.5 i 1. Sjeti se da je 0 najmanje varijabilna, a 1 najviše. Koja vrijednost ti najbolje odgovara za tvoju aplikaciju?

## Odlično! Nastavi sa učenjem

Nakon što završiš ovu lekciju, pogledaj našu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da nastaviš podizati svoje znanje o Generativnoj AI!

Kreni na Lekciju 7 gdje ćemo pogledati kako [graditi chat aplikacije](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->