<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T17:23:33+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "sr"
}
-->
# Izgradnja aplikacija za generisanje teksta

> _(Kliknite na sliku iznad da pogledate video ovog predavanja)_

Do sada ste kroz ovaj kurikulum videli da postoje osnovni koncepti kao što su upiti i čak cela disciplina zvana "inženjering upita". Mnogi alati sa kojima možete komunicirati, kao što su ChatGPT, Office 365, Microsoft Power Platform i drugi, podržavaju korišćenje upita da biste postigli nešto.

Da biste dodali takvo iskustvo u aplikaciju, potrebno je da razumete koncepte kao što su upiti, završeci i da odaberete biblioteku sa kojom ćete raditi. Upravo to ćete naučiti u ovom poglavlju.

## Uvod

U ovom poglavlju, vi ćete:

- Naučiti o biblioteci openai i njenim osnovnim konceptima.
- Napraviti aplikaciju za generisanje teksta koristeći openai.
- Razumeti kako koristiti koncepte kao što su upit, temperatura i tokeni za izgradnju aplikacije za generisanje teksta.

## Ciljevi učenja

Na kraju ovog predavanja, moći ćete da:

- Objasnite šta je aplikacija za generisanje teksta.
- Napravite aplikaciju za generisanje teksta koristeći openai.
- Konfigurišete vašu aplikaciju da koristi više ili manje tokena i takođe promenite temperaturu za različite rezultate.

## Šta je aplikacija za generisanje teksta?

Obično kada pravite aplikaciju, ona ima neku vrstu interfejsa kao što je sledeći:

- Na bazi komandi. Konzolne aplikacije su tipične aplikacije gde kucate komandu i ona izvršava zadatak. Na primer, `git` je aplikacija na bazi komandi.
- Korisnički interfejs (UI). Neke aplikacije imaju grafičke korisničke interfejse (GUI) gde kliknete na dugmad, unosite tekst, birate opcije i više.

### Konzolne i UI aplikacije su ograničene

Uporedite to sa aplikacijom na bazi komandi gde kucate komandu:

- **Ograničena je**. Ne možete samo kucati bilo koju komandu, već samo one koje aplikacija podržava.
- **Jezik specifičan**. Neke aplikacije podržavaju mnoge jezike, ali po defaultu aplikacija je napravljena za specifičan jezik, čak i ako možete dodati više podrške za jezike.

### Prednosti aplikacija za generisanje teksta

Kako je aplikacija za generisanje teksta drugačija?

U aplikaciji za generisanje teksta imate više fleksibilnosti, niste ograničeni na skup komandi ili specifičan ulazni jezik. Umesto toga, možete koristiti prirodni jezik za interakciju sa aplikacijom. Još jedna prednost je što već komunicirate sa izvorom podataka koji je obučen na velikom korpusu informacija, dok tradicionalna aplikacija može biti ograničena na ono što je u bazi podataka.

### Šta mogu napraviti sa aplikacijom za generisanje teksta?

Možete napraviti mnogo stvari. Na primer:

- **Četbot**. Četbot koji odgovara na pitanja o temama, kao što su vaša kompanija i njeni proizvodi, mogao bi biti dobar izbor.
- **Pomoćnik**. LLM-ovi su odlični u stvarima kao što su sažimanje teksta, dobijanje uvida iz teksta, proizvodnja teksta kao što su biografije i više.
- **Asistent za kod**. U zavisnosti od jezičkog modela koji koristite, možete napraviti asistenta za kod koji vam pomaže u pisanju koda. Na primer, možete koristiti proizvod kao što je GitHub Copilot, kao i ChatGPT, da vam pomogne u pisanju koda.

## Kako mogu početi?

Pa, treba da pronađete način da se integrišete sa LLM što obično podrazumeva sledeća dva pristupa:

- Korišćenje API-ja. Ovde konstruisete web zahteve sa vašim upitom i dobijate generisani tekst nazad.
- Korišćenje biblioteke. Biblioteke pomažu da se enkapsuliraju API pozivi i olakšavaju njihovo korišćenje.

## Biblioteke/SDK-ovi

Postoji nekoliko poznatih biblioteka za rad sa LLM-ovima kao što su:

- **openai**, ova biblioteka olakšava povezivanje sa vašim modelom i slanje upita.

Zatim postoje biblioteke koje rade na višem nivou kao što su:

- **Langchain**. Langchain je dobro poznat i podržava Python.
- **Semantic Kernel**. Semantic Kernel je biblioteka kompanije Microsoft koja podržava jezike C#, Python i Java.

## Prva aplikacija koristeći openai

Hajde da vidimo kako možemo napraviti našu prvu aplikaciju, koje biblioteke su nam potrebne, koliko je potrebno i tako dalje.

### Instalirajte openai

Postoje mnoge biblioteke za interakciju sa OpenAI ili Azure OpenAI. Moguće je koristiti mnoge programske jezike kao što su C#, Python, JavaScript, Java i više. Odabrali smo da koristimo biblioteku `openai` Python, pa ćemo koristiti `pip` za instalaciju.

```bash
pip install openai
```

### Kreirajte resurs

Potrebno je da izvršite sledeće korake:

- Kreirajte nalog na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pristupite Azure OpenAI. Idite na [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) i zatražite pristup.

  > [!NOTE]
  > U vreme pisanja, potrebno je aplicirati za pristup Azure OpenAI.

- Instalirajte Python <https://www.python.org/>
- Kreirajte Azure OpenAI Service resurs. Pogledajte ovaj vodič kako da [kreirate resurs](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Locirajte API ključ i endpoint

U ovom trenutku, potrebno je da kažete vašoj `openai` biblioteci koji API ključ da koristi. Da biste pronašli vaš API ključ, idite na sekciju "Keys and Endpoint" vašeg Azure OpenAI resursa i kopirajte vrednost "Key 1".

Sada kada ste kopirali ove informacije, hajde da uputimo biblioteke da ih koriste.

> [!NOTE]
> Vredi odvojiti vaš API ključ od koda. To možete učiniti korišćenjem varijabli okruženja.
>
> - Postavite varijablu okruženja `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Postavite konfiguraciju za Azure

Ako koristite Azure OpenAI, evo kako postavljate konfiguraciju:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Gore postavljamo sledeće:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` klasa. Evo primera:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

U gornjem kodu, kreiramo objekat završetka i prosleđujemo model koji želimo da koristimo i upit. Zatim ispisujemo generisani tekst.

### Završeci za čet

Do sada ste videli kako smo koristili `Completion` to generate text. But there's another class called `ChatCompletion` koji je više prilagođen za četbotove. Evo primera kako ga koristiti:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Više o ovoj funkcionalnosti u narednom poglavlju.

## Vežba - vaša prva aplikacija za generisanje teksta

Sada kada smo naučili kako da postavimo i konfigurišemo openai, vreme je da napravite svoju prvu aplikaciju za generisanje teksta. Da biste napravili vašu aplikaciju, pratite ove korake:

1. Kreirajte virtuelno okruženje i instalirajte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ako koristite Windows, kucajte `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` vrednost.

1. Kreirajte _app.py_ fajl i unesite sledeći kod:

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
   > Ako koristite Azure OpenAI, potrebno je da postavite `api_type` to `azure` and set the `api_key` na vaš Azure OpenAI ključ.

   Trebalo bi da vidite izlaz sličan sledećem:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Različite vrste upita za različite stvari

Sada ste videli kako generisati tekst koristeći upit. Čak imate program koji radi i koji možete modifikovati i menjati da generiše različite vrste teksta.

Upiti se mogu koristiti za sve vrste zadataka. Na primer:

- **Generišite vrstu teksta**. Na primer, možete generisati pesmu, pitanja za kviz itd.
- **Pretražujte informacije**. Možete koristiti upite za pretragu informacija kao što je sledeći primer 'Šta znači CORS u web razvoju?'.
- **Generišite kod**. Možete koristiti upite za generisanje koda, na primer razvijajući regularni izraz koji se koristi za validaciju email-ova ili zašto ne generisati ceo program, kao što je web aplikacija?

## Praktičniji slučaj upotrebe: generator recepata

Zamislite da imate sastojke kod kuće i želite da skuvate nešto. Za to vam je potreban recept. Način da pronađete recepte je korišćenje pretraživača ili možete koristiti LLM za to.

Možete napisati upit ovako:

> "Pokaži mi 5 recepata za jelo sa sledećim sastojcima: piletina, krompir i šargarepa. Po receptu, navedi sve korišćene sastojke"

S obzirom na gornji upit, možete dobiti odgovor sličan:

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

Ovaj rezultat je odličan, znam šta da kuvam. U ovom trenutku, korisna poboljšanja mogu biti:

- Filtriranje sastojaka koje ne volim ili na koje sam alergičan.
- Proizvodnja liste za kupovinu, u slučaju da nemam sve sastojke kod kuće.

Za gore navedene slučajeve, dodajmo dodatni upit:

> "Molim vas uklonite recepte sa belim lukom jer sam alergičan i zamenite ga nečim drugim. Takođe, molim vas napravite listu za kupovinu za recepte, uzimajući u obzir da već imam piletinu, krompir i šargarepe kod kuće."

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

To su vaši recepti, bez pomena belog luka, a imate i listu za kupovinu uzimajući u obzir ono što već imate kod kuće.

## Vežba - napravite generator recepata

Sada kada smo razradili scenario, hajde da napišemo kod koji odgovara demonstriranom scenariju. Da bismo to uradili, pratite ove korake:

1. Koristite postojeći _app.py_ fajl kao početnu tačku
1. Pronađite `prompt` promenljivu i promenite njen kod na sledeći način:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ako sada pokrenete kod, trebalo bi da vidite izlaz sličan:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NAPOMENA, vaš LLM je nedeterministički, tako da možete dobiti različite rezultate svaki put kada pokrenete program.

   Sjajno, hajde da vidimo kako možemo poboljšati stvari. Da bismo poboljšali stvari, želimo da osiguramo da je kod fleksibilan, tako da sastojci i broj recepata mogu biti poboljšani i promenjeni.

1. Promenimo kod na sledeći način:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Pokretanje koda za testiranje moglo bi izgledati ovako:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Poboljšanje dodavanjem filtera i liste za kupovinu

Sada imamo funkcionalnu aplikaciju sposobnu za proizvodnju recepata i fleksibilna je jer se oslanja na ulaze korisnika, kako na broj recepata, tako i na korišćene sastojke.

Da bismo je dodatno poboljšali, želimo da dodamo sledeće:

- **Filtrirajte sastojke**. Želimo da možemo filtrirati sastojke koje ne volimo ili na koje smo alergični. Da bismo postigli ovu promenu, možemo urediti naš postojeći upit i dodati uslov filtera na kraj njega ovako:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Gore, dodajemo `{filter}` na kraj upita i takođe hvatamo vrednost filtera od korisnika.

  Primer unosa pri pokretanju programa sada može izgledati ovako:

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

  Kao što možete videti, svi recepti sa mlekom su filtrirani. Ali, ako ste netolerantni na laktozu, možda želite da filtrirate i recepte sa sirom, tako da postoji potreba za jasnim razjašnjenjem.

- **Proizvodnja liste za kupovinu**. Želimo da napravimo listu za kupovinu, uzimajući u obzir ono što već imamo kod kuće.

  Za ovu funkcionalnost, mogli bismo pokušati da rešimo sve u jednom upitu ili bismo mogli da ga podelimo na dva upita. Hajde da pokušamo drugi pristup. Ovde predlažemo dodavanje dodatnog upita, ali da bi to funkcionisalo, moramo dodati rezultat prvog upita kao kontekst za drugi upit.

  Pronađite deo u kodu koji ispisuje rezultat iz prvog upita i dodajte sledeći kod ispod:

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

  Obratite pažnju na sledeće:

  1. Konstruisali smo novi upit dodavanjem rezultata iz prvog upita u novi upit:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Pravimo novi zahtev, ali takođe uzimajući u obzir broj tokena koji smo tražili u prvom upitu, tako da ovaj put kažemo `max_tokens` je 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Testiranjem ovog koda, sada dolazimo do sledećeg izlaza:

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

Ono što imamo do sada je kod koji radi, ali postoje neka podešavanja koja bi trebalo da uradimo kako bismo dodatno poboljšali stvari. Neke stvari koje bismo trebali uraditi su:

- **Odvojite tajne od koda**, kao što je API ključ. Tajne ne pripadaju kodu i treba ih čuvati na sigurnom mestu. Da bismo odvojili tajne od koda, možemo koristiti varijable okruženja i biblioteke kao što je `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` fajl sa sledećim sadržajem:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Napomena, za Azure, potrebno je da postavite sledeće varijable okruženja:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     U kodu, učitali biste varijable okruženja ovako:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Reč o dužini tokena**. Trebalo bi da razmislimo o tome koliko tokena treba da generišemo tekst koji želimo. Tokeni koštaju novac, tako da gde god je moguće, trebali bismo pokušati da budemo ekonomični sa brojem tokena koje koristimo. Na primer, možemo li formulisati upit tako da koristimo manje tokena?

  Da biste promenili korišćene tokene, možete koristiti parametar `max_tokens`. Na primer, ako želite da koristite 100 tokena, uradili biste:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Eksperimentisanje sa temperaturom**. Temperatura je nešto što do sada nismo pomenuli, ali je važan kontekst za to kako naš program funkcioniše. Što je viša vrednost temperature, to će izlaz biti nasumičniji. Obrnuto, što je niža vrednost temperature, to će izlaz biti predvidljiviji. Razmislite da li želite varijaciju u vašem izlazu ili ne.

  Da biste promenili temperaturu, možete koristiti parametar `temperature`. Na primer, ako želite da koristite temperaturu od 0.5, uradili biste:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Napomena, što je bliže 1.0, to će izlaz biti raznovrsniji.

## Zadatak

Za ovaj zadatak, možete odabrati šta želite da napravite.

Evo nekoliko predloga:

- Prilagodite aplikaciju za generisanje recepata kako biste je dodatno poboljšali. Igrajte se sa vrednostima temperature

**Одричање од одговорности**:  
Овај документ је преведен коришћењем AI услуге превођења [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо вас да будете свесни да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације, препоручује се професионални превод од стране људи. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења која произилазе из употребе овог превода.