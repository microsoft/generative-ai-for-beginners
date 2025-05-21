<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T17:27:23+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "sl"
}
-->
# Izgradnja aplikacija za generisanje teksta

> _(Kliknite na sliku iznad da pogledate video lekciju)_

Kroz ovaj kurikulum ste do sada videli osnovne pojmove poput prompta, pa čak i celu disciplinu nazvanu "inženjering prompta". Mnogi alati sa kojima možete komunicirati, kao što su ChatGPT, Office 365, Microsoft Power Platform i drugi, podržavaju korišćenje prompta za postizanje cilja.

Da biste dodali takvo iskustvo u aplikaciju, potrebno je da razumete koncepte poput prompta, završetaka i odaberete biblioteku sa kojom ćete raditi. To je upravo ono što ćete naučiti u ovom poglavlju.

## Uvod

U ovom poglavlju ćete:

- Naučiti o openai biblioteci i njenim osnovnim konceptima.
- Izgraditi aplikaciju za generisanje teksta koristeći openai.
- Razumeti kako koristiti koncepte kao što su prompt, temperatura i tokeni za izgradnju aplikacije za generisanje teksta.

## Ciljevi učenja

Na kraju ove lekcije, bićete u stanju da:

- Objasnite šta je aplikacija za generisanje teksta.
- Izgradite aplikaciju za generisanje teksta koristeći openai.
- Konfigurišete svoju aplikaciju da koristi više ili manje tokena i takođe promenite temperaturu za raznolik izlaz.

## Šta je aplikacija za generisanje teksta?

Obično kada gradite aplikaciju, ona ima neku vrstu interfejsa kao što su:

- Zasnovano na komandama. Konzolne aplikacije su tipične aplikacije gde kucate komandu i ona izvršava zadatak. Na primer, `git` je aplikacija zasnovana na komandama.
- Korisnički interfejs (UI). Neke aplikacije imaju grafičke korisničke interfejse (GUI) gde klikćete na dugmad, unosite tekst, birate opcije i više.

### Konzolne i UI aplikacije su ograničene

Uporedite to sa aplikacijom zasnovanom na komandama gde kucate komandu:

- **Ograničeno je**. Ne možete jednostavno kucati bilo koju komandu, već samo one koje aplikacija podržava.
- **Specifično za jezik**. Neke aplikacije podržavaju mnogo jezika, ali po defaultu aplikacija je napravljena za određeni jezik, čak i ako možete dodati podršku za više jezika.

### Prednosti aplikacija za generisanje teksta

Kako se aplikacija za generisanje teksta razlikuje?

U aplikaciji za generisanje teksta imate veću fleksibilnost, niste ograničeni na skup komandi ili određeni ulazni jezik. Umesto toga, možete koristiti prirodni jezik za interakciju sa aplikacijom. Još jedna prednost je što već komunicirate sa izvorom podataka koji je obučen na ogromnom korpusu informacija, dok bi tradicionalna aplikacija mogla biti ograničena na ono što je u bazi podataka.

### Šta mogu da izgradim sa aplikacijom za generisanje teksta?

Mnogo toga možete izgraditi. Na primer:

- **Chatbot**. Chatbot koji odgovara na pitanja o temama, kao što su vaša kompanija i njeni proizvodi, mogao bi biti dobar izbor.
- **Pomoćnik**. LLM-ovi su odlični u stvarima kao što su sažimanje teksta, dobijanje uvida iz teksta, proizvodnja teksta poput biografija i još mnogo toga.
- **Asistent za kod**. U zavisnosti od modela jezika koji koristite, možete izgraditi asistenta za kod koji vam pomaže da pišete kod. Na primer, možete koristiti proizvod kao što je GitHub Copilot, kao i ChatGPT, da vam pomogne u pisanju koda.

## Kako mogu da počnem?

Pa, potrebno je da pronađete način za integraciju sa LLM-om, što obično podrazumeva sledeća dva pristupa:

- Korišćenje API-ja. Ovde konstruisete web zahteve sa svojim promptom i dobijate generisani tekst nazad.
- Korišćenje biblioteke. Biblioteke pomažu u enkapsuliranju API poziva i čine ih lakšim za korišćenje.

## Biblioteke/SDK-ovi

Postoji nekoliko poznatih biblioteka za rad sa LLM-ovima kao što su:

- **openai**, ova biblioteka olakšava povezivanje sa vašim modelom i slanje promptova.

Zatim postoje biblioteke koje rade na višem nivou kao što su:

- **Langchain**. Langchain je dobro poznat i podržava Python.
- **Semantic Kernel**. Semantic Kernel je biblioteka od strane Microsoft-a koja podržava jezike C#, Python i Java.

## Prva aplikacija koristeći openai

Pogledajmo kako možemo izgraditi našu prvu aplikaciju, koje biblioteke su nam potrebne, koliko je potrebno i tako dalje.

### Instalacija openai

Postoji mnogo biblioteka za interakciju sa OpenAI ili Azure OpenAI. Moguće je koristiti brojne programske jezike kao što su C#, Python, JavaScript, Java i drugi. Odabrali smo da koristimo `openai` Python biblioteku, pa ćemo koristiti `pip` za instalaciju.

```bash
pip install openai
```

### Kreiranje resursa

Potrebno je da izvršite sledeće korake:

- Kreirajte nalog na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pristupite Azure OpenAI. Idite na [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) i zatražite pristup.

  > [!NOTE]
  > U vreme pisanja, potrebno je da se prijavite za pristup Azure OpenAI.

- Instalirajte Python <https://www.python.org/>
- Kreirajte Azure OpenAI Service resurs. Pogledajte ovaj vodič kako [kreirati resurs](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Lociranje API ključa i endpointa

U ovom trenutku, potrebno je da kažete svojoj `openai` biblioteci koji API ključ da koristi. Da biste pronašli svoj API ključ, idite na "Keys and Endpoint" sekciju vašeg Azure OpenAI resursa i kopirajte vrednost "Key 1".

Sada kada imate ovu informaciju kopiranu, hajde da uputimo biblioteke da je koriste.

> [!NOTE]
> Vredi odvojiti svoj API ključ od koda. Možete to uraditi korišćenjem promenljivih okruženja.
>
> - Postavite promenljivu okruženja `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Podešavanje konfiguracije Azure

Ako koristite Azure OpenAI, evo kako podesiti konfiguraciju:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Iznad postavljamo sledeće:

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

U gornjem kodu, kreiramo objekat završetka i prosleđujemo model koji želimo da koristimo i prompt. Zatim ispisujemo generisani tekst.

### Završeci za chat

Do sada ste videli kako smo koristili `Completion` to generate text. But there's another class called `ChatCompletion` koji je više prilagođen za chat botove. Evo primera kako ga koristiti:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Više o ovoj funkcionalnosti u narednom poglavlju.

## Vežba - vaša prva aplikacija za generisanje teksta

Sada kada smo naučili kako da podesimo i konfigurišemo openai, vreme je da izgradite svoju prvu aplikaciju za generisanje teksta. Da biste izgradili svoju aplikaciju, pratite ove korake:

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

1. Kreirajte _app.py_ fajl i dodajte mu sledeći kod:

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

## Različiti tipovi prompta za različite stvari

Sada ste videli kako generisati tekst koristeći prompt. Čak imate program koji radi i koji možete modifikovati i promeniti da generiše različite tipove teksta.

Promptovi se mogu koristiti za sve vrste zadataka. Na primer:

- **Generisanje tipa teksta**. Na primer, možete generisati pesmu, pitanja za kviz itd.
- **Pretraga informacija**. Možete koristiti promptove da tražite informacije kao što je sledeći primer 'Šta znači CORS u web razvoju?'.
- **Generisanje koda**. Možete koristiti promptove da generišete kod, na primer razvijanje regularnog izraza koji se koristi za validaciju emailova ili zašto ne generisati ceo program, kao što je web aplikacija?

## Praktičniji slučaj upotrebe: generator recepata

Zamislite da imate sastojke kod kuće i želite da skuvate nešto. Za to vam je potreban recept. Način da pronađete recepte je da koristite pretraživač ili možete koristiti LLM za to.

Mogli biste napisati prompt ovako:

> "Pokaži mi 5 recepata za jelo sa sledećim sastojcima: piletina, krompir i šargarepa. Po receptu, navedite sve korišćene sastojke"

S obzirom na gornji prompt, mogli biste dobiti odgovor sličan:

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

Ovaj rezultat je sjajan, znam šta da kuvam. U ovom trenutku, šta bi moglo biti korisno poboljšanje su:

- Filtriranje sastojaka koje ne volim ili na koje sam alergičan.
- Izrada liste za kupovinu, u slučaju da nemam sve sastojke kod kuće.

Za gornje slučajeve, dodajmo dodatni prompt:

> "Molim vas uklonite recepte sa belim lukom jer sam alergičan i zamenite ga nečim drugim. Takođe, molim vas izradite listu za kupovinu za recepte, uzimajući u obzir da već imam piletinu, krompir i šargarepu kod kuće."

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

To su vaših pet recepata, bez belog luka i imate listu za kupovinu uzimajući u obzir ono što već imate kod kuće.

## Vežba - izgradnja generatora recepata

Sada kada smo razradili scenario, hajde da napišemo kod koji odgovara prikazanom scenariju. Da bismo to uradili, pratite ove korake:

1. Koristite postojeći _app.py_ fajl kao početnu tačku
1. Pronađite `prompt` varijablu i promenite njen kod u sledeći:

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

1. Hajde da promenimo kod na sledeći način:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testiranje koda moglo bi izgledati ovako:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Poboljšanje dodavanjem filtera i liste za kupovinu

Sada imamo radnu aplikaciju sposobnu za proizvodnju recepata i fleksibilna je jer se oslanja na unose od korisnika, kako na broj recepata, tako i na korišćene sastojke.

Da bismo je dalje poboljšali, želimo da dodamo sledeće:

- **Filtriranje sastojaka**. Želimo da možemo filtrirati sastojke koje ne volimo ili na koje smo alergični. Da bismo postigli ovu promenu, možemo urediti naš postojeći prompt i dodati uslov za filtriranje na njegov kraj ovako:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Iznad, dodajemo `{filter}` na kraj prompta i takođe hvatamo vrednost filtera od korisnika.

  Primer unosa prilikom pokretanja programa sada može izgledati ovako:

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

  Kao što vidite, svi recepti sa mlekom su filtrirani. Ali, ako ste netolerantni na laktozu, možda želite da filtrirate recepte i sa sirom, tako da je potrebno biti jasan.

- **Izrada liste za kupovinu**. Želimo da izradimo listu za kupovinu, uzimajući u obzir ono što već imamo kod kuće.

  Za ovu funkcionalnost, mogli bismo pokušati da rešimo sve u jednom promptu ili bismo mogli da ga podelimo na dva prompta. Hajde da probamo drugi pristup. Ovde predlažemo dodavanje dodatnog prompta, ali da bi to radilo, potrebno je da dodamo rezultat prvog prompta kao kontekst za drugi prompt.

  Pronađite deo u kodu koji ispisuje rezultat iz prvog prompta i dodajte sledeći kod ispod:

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

  1. Konstruisali smo novi prompt dodavanjem rezultata iz prvog prompta u novi prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Napravili smo novi zahtev, ali takođe uzimajući u obzir broj tokena koje smo tražili u prvom promptu, tako da ovaj put kažemo `max_tokens` je 1200.

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

## Poboljšajte svoju postavku

Ono što imamo do sada je kod koji radi, ali postoje neka podešavanja koja bismo trebali uraditi da dodatno poboljšamo stvari. Neke stvari koje bismo trebali uraditi su:

- **Odvojiti tajne od koda**, kao što je API ključ. Tajne ne pripadaju kodu i treba ih čuvati na sigurnom mestu. Da biste odvojili tajne od koda, možete koristiti promenljive okruženja i biblioteke kao što je `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` fajl sa sledećim sadržajem:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Napomena, za Azure, potrebno je da postavite sledeće promenljive okruženja:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     U kodu, učitali biste promenljive okruženja ovako:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Reč o dužini tokena**. Trebali bismo razmotriti koliko tokena nam je potrebno za generisanje teksta koji želimo. Tokeni koštaju novac, tako da gde je moguće, trebali bismo pokušati biti ekonomični sa brojem tokena koje koristimo. Na primer, možemo li formulisati prompt tako da možemo koristiti manje tokena?

  Da biste promenili korišćene tokene, možete koristiti `max_tokens` parametar. Na primer, ako želite koristiti 100 tokena, uradili biste:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Eksperimentisanje sa temperaturom**. Temperatura je nešto što do sada nismo spomenuli, ali je važan kontekst za to kako naš program funkcioniše. Što je viša vrednost temperature, to će izlaz biti slučajniji. Nasuprot tome, što je niža vrednost temperature, izlaz će biti predvidljiviji. Razmotrite da li želite varijacije u svom izlazu ili ne.

  Da biste promenili temperaturu, možete koristiti `temperature` parametar. Na primer, ako želite koristiti temperaturu od 0.5, uradili biste:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Napomena, što je bliže 1.0, to je izlaz raznovrsniji.

## Zadatak

Za ovaj zadatak, možete izabrati šta da izgradite.

Evo nekih predloga:

- Doradite aplikaciju za generisanje recepata da je dodatno poboljšate. Igrajte se sa vrednostima temperature i promptovima da vidite šta možete smisliti.
- Izgradite "studij

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav se trudimo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije se priporoča profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.