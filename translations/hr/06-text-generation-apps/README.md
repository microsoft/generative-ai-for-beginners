<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-18T01:28:48+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "hr"
}
-->
# Izrada aplikacija za generiranje teksta

[![Izrada aplikacija za generiranje teksta](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.hr.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite na sliku iznad za pregled videa ove lekcije)_

Do sada ste kroz ovaj kurikulum vidjeli da postoje osnovni koncepti poput upita (prompts) i čak cijela disciplina nazvana "inženjering upita". Mnogi alati s kojima možete komunicirati, poput ChatGPT-a, Office 365, Microsoft Power Platforma i drugih, omogućuju vam korištenje upita za postizanje određenih ciljeva.

Da biste dodali takvo iskustvo u aplikaciju, trebate razumjeti koncepte poput upita, dovršetaka (completions) i odabrati biblioteku s kojom ćete raditi. Upravo to ćete naučiti u ovom poglavlju.

## Uvod

U ovom poglavlju ćete:

- Naučiti o biblioteci openai i njezinim osnovnim konceptima.
- Izraditi aplikaciju za generiranje teksta koristeći openai.
- Razumjeti kako koristiti koncepte poput upita, temperature i tokena za izradu aplikacije za generiranje teksta.

## Ciljevi učenja

Na kraju ove lekcije, moći ćete:

- Objasniti što je aplikacija za generiranje teksta.
- Izraditi aplikaciju za generiranje teksta koristeći openai.
- Konfigurirati svoju aplikaciju za korištenje više ili manje tokena te promijeniti temperaturu za raznolike rezultate.

## Što je aplikacija za generiranje teksta?

Obično kada izrađujete aplikaciju, ona ima neku vrstu sučelja poput sljedećeg:

- Temeljeno na naredbama. Konzolne aplikacije su tipične aplikacije gdje upisujete naredbu i ona izvršava zadatak. Na primjer, `git` je aplikacija temeljena na naredbama.
- Korisničko sučelje (UI). Neke aplikacije imaju grafička korisnička sučelja (GUI) gdje klikate gumbe, unosite tekst, birate opcije i slično.

### Ograničenja konzolnih i UI aplikacija

Usporedite to s aplikacijom temeljenom na naredbama gdje upisujete naredbu:

- **Ograničeno je**. Ne možete upisati bilo koju naredbu, već samo one koje aplikacija podržava.
- **Specifično za jezik**. Neke aplikacije podržavaju mnoge jezike, ali u osnovi su izrađene za određeni jezik, čak i ako možete dodati podršku za više jezika.

### Prednosti aplikacija za generiranje teksta

Kako se onda aplikacija za generiranje teksta razlikuje?

U aplikaciji za generiranje teksta imate više fleksibilnosti, niste ograničeni na skup naredbi ili određeni ulazni jezik. Umjesto toga, možete koristiti prirodni jezik za interakciju s aplikacijom. Još jedna prednost je što već komunicirate s izvorom podataka koji je treniran na velikom korpusu informacija, dok je tradicionalna aplikacija možda ograničena na ono što se nalazi u bazi podataka.

### Što mogu izraditi s aplikacijom za generiranje teksta?

Možete izraditi mnogo toga. Na primjer:

- **Chatbot**. Chatbot koji odgovara na pitanja o temama, poput vaše tvrtke i njezinih proizvoda, mogao bi biti dobar izbor.
- **Pomoćnik**. LLM-ovi su izvrsni u stvarima poput sažimanja teksta, dobivanja uvida iz teksta, stvaranja teksta poput životopisa i slično.
- **Asistent za kodiranje**. Ovisno o modelu jezika koji koristite, možete izraditi asistenta za kodiranje koji vam pomaže pisati kod. Na primjer, možete koristiti proizvod poput GitHub Copilot-a ili ChatGPT-a za pomoć pri pisanju koda.

## Kako početi?

Treba pronaći način za integraciju s LLM-om, što obično uključuje sljedeća dva pristupa:

- Koristite API. Ovdje konstruirate web zahtjeve s vašim upitom i dobivate generirani tekst natrag.
- Koristite biblioteku. Biblioteke pomažu u enkapsulaciji API poziva i olakšavaju njihovo korištenje.

## Biblioteke/SDK-ovi

Postoji nekoliko poznatih biblioteka za rad s LLM-ovima, poput:

- **openai**, ova biblioteka olakšava povezivanje s vašim modelom i slanje upita.

Zatim postoje biblioteke koje djeluju na višoj razini, poput:

- **Langchain**. Langchain je poznat i podržava Python.
- **Semantic Kernel**. Semantic Kernel je biblioteka tvrtke Microsoft koja podržava jezike C#, Python i Java.

## Prva aplikacija koristeći openai

Pogledajmo kako možemo izraditi našu prvu aplikaciju, koje biblioteke trebamo, koliko je potrebno i tako dalje.

### Instalacija openai

Postoji mnogo biblioteka za interakciju s OpenAI ili Azure OpenAI. Moguće je koristiti brojne programske jezike poput C#, Python, JavaScript, Java i drugih. Odabrali smo koristiti Python biblioteku `openai`, pa ćemo je instalirati pomoću `pip`.

```bash
pip install openai
```

### Kreiranje resursa

Potrebno je izvršiti sljedeće korake:

- Kreirajte račun na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Dobijte pristup Azure OpenAI. Idite na [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) i zatražite pristup.

  > [!NOTE]
  > U trenutku pisanja, potrebno je podnijeti zahtjev za pristup Azure OpenAI.

- Instalirajte Python <https://www.python.org/>
- Kreirajte resurs za Azure OpenAI Service. Pogledajte ovaj vodič kako [kreirati resurs](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Pronalaženje API ključa i krajnje točke

Sada trebate reći svojoj `openai` biblioteci koji API ključ koristiti. Da biste pronašli svoj API ključ, idite na odjeljak "Keys and Endpoint" u vašem Azure OpenAI resursu i kopirajte vrijednost "Key 1".

![Resurs Keys and Endpoint u Azure Portalu](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sada kada ste kopirali ove informacije, uputimo biblioteke da ih koriste.

> [!NOTE]
> Vrijedi odvojiti vaš API ključ od koda. To možete učiniti pomoću varijabli okruženja.
>
> - Postavite varijablu okruženja `OPENAI_API_KEY` na vaš API ključ.
>   `export OPENAI_API_KEY='sk-...'`

### Postavljanje konfiguracije za Azure

Ako koristite Azure OpenAI, evo kako postaviti konfiguraciju:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Ovdje postavljamo sljedeće:

- `api_type` na `azure`. Ovo govori biblioteci da koristi Azure OpenAI, a ne OpenAI.
- `api_key`, ovo je vaš API ključ pronađen u Azure Portalu.
- `api_version`, ovo je verzija API-ja koju želite koristiti. U trenutku pisanja, najnovija verzija je `2023-05-15`.
- `api_base`, ovo je krajnja točka API-ja. Možete je pronaći u Azure Portalu pored vašeg API ključa.

> [!NOTE] > `os.getenv` je funkcija koja čita varijable okruženja. Možete je koristiti za čitanje varijabli okruženja poput `OPENAI_API_KEY` i `API_BASE`. Postavite ove varijable okruženja u svom terminalu ili pomoću biblioteke poput `dotenv`.

## Generiranje teksta

Način generiranja teksta je korištenje klase `Completion`. Evo primjera:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

U gornjem kodu kreiramo objekt za dovršavanje i prosljeđujemo model koji želimo koristiti i upit. Zatim ispisujemo generirani tekst.

### Dovršavanje razgovora

Do sada ste vidjeli kako koristimo `Completion` za generiranje teksta. No, postoji još jedna klasa nazvana `ChatCompletion` koja je prikladnija za chatbotove. Evo primjera kako je koristiti:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Više o ovoj funkcionalnosti u nadolazećem poglavlju.

## Vježba - vaša prva aplikacija za generiranje teksta

Sada kada smo naučili kako postaviti i konfigurirati openai, vrijeme je da izradimo vašu prvu aplikaciju za generiranje teksta. Da biste izradili svoju aplikaciju, slijedite ove korake:

1. Kreirajte virtualno okruženje i instalirajte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ako koristite Windows, upišite `venv\Scripts\activate` umjesto `source venv/bin/activate`.

   > [!NOTE]
   > Pronađite svoj Azure OpenAI ključ tako da odete na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), potražite `Open AI` i odaberete resurs `Open AI`, zatim odaberite `Keys and Endpoint` i kopirajte vrijednost `Key 1`.

1. Kreirajte datoteku _app.py_ i dodajte sljedeći kod:

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
   > Ako koristite Azure OpenAI, trebate postaviti `api_type` na `azure` i postaviti `api_key` na vaš Azure OpenAI ključ.

   Trebali biste vidjeti izlaz sličan sljedećem:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Različite vrste upita za različite zadatke

Sada ste vidjeli kako generirati tekst koristeći upit. Čak imate program koji radi i koji možete mijenjati kako biste generirali različite vrste teksta.

Upiti se mogu koristiti za razne zadatke. Na primjer:

- **Generiranje vrste teksta**. Na primjer, možete generirati pjesmu, pitanja za kviz itd.
- **Pretraživanje informacija**. Možete koristiti upite za traženje informacija, poput sljedećeg primjera 'Što znači CORS u web razvoju?'.
- **Generiranje koda**. Možete koristiti upite za generiranje koda, na primjer za razvoj regularnog izraza koji se koristi za validaciju e-mailova ili zašto ne generirati cijeli program, poput web aplikacije?

## Praktičniji primjer: generator recepata

Zamislite da imate sastojke kod kuće i želite nešto skuhati. Za to vam je potreban recept. Jedan način pronalaženja recepata je korištenje tražilice ili možete koristiti LLM za to.

Možete napisati upit poput sljedećeg:

> "Prikaži mi 5 recepata za jelo s sljedećim sastojcima: piletina, krumpir i mrkva. Za svaki recept, navedite sve korištene sastojke."

S obzirom na gornji upit, mogli biste dobiti odgovor sličan:

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

Ovaj rezultat je odličan, znam što mogu skuhati. U ovom trenutku, korisna poboljšanja mogla bi biti:

- Filtriranje sastojaka koje ne volim ili na koje sam alergičan.
- Izrada popisa za kupovinu, u slučaju da nemam sve sastojke kod kuće.

Za gore navedene slučajeve, dodajmo dodatni upit:

> "Molim te ukloni recepte s češnjakom jer sam alergičan i zamijeni ga nečim drugim. Također, izradi popis za kupovinu za recepte, uzimajući u obzir da već imam piletinu, krumpir i mrkvu kod kuće."

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

To su vaših pet recepata, bez spominjanja češnjaka, a također imate i popis za kupovinu uzimajući u obzir ono što već imate kod kuće.

## Vježba - izradite generator recepata

Sada kada smo razradili scenarij, napišimo kod koji odgovara prikazanom scenariju. Da bismo to učinili, slijedite ove korake:

1. Koristite postojeću datoteku _app.py_ kao početnu točku.
1. Pronađite varijablu `prompt` i promijenite njezin kod u sljedeći:

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

   > NAPOMENA, vaš LLM je nedeterministički, pa možete dobiti različite rezultate svaki put kad pokrenete program.

   Odlično, pogledajmo kako možemo poboljšati stvari. Da bismo poboljšali stvari, želimo osigurati da je kod fleksibilan, tako da se sastojci i broj recepata mogu mijenjati.

1. Promijenimo kod na sljedeći način:

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

### Poboljšanje dodavanjem filtera i popisa za kupovinu

Sada imamo funkcionalnu aplikaciju sposobnu za izradu recepata, a fleksibilna je jer se oslanja na unos korisnika, kako u pogledu broja recepata, tako i sastojaka koji se koriste.

Da bismo je dodatno poboljšali, želimo dodati sljedeće:

- **Filtriranje sastojaka**. Želimo biti u mogućnosti filtrirati sastojke koje ne volimo ili na koje smo alergični. Da bismo to postigli, možemo urediti naš postojeći upit i dodati uvjet za filtriranje na njegov kraj, kao što je prikazano:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Gore dodajemo `{filter}` na kraj upita i također bilježimo vrijednost filtera od korisnika.

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

  Kao što možete vidjeti, svi recepti s mlijekom su filtrirani. No, ako ste netolerantni na laktozu, možda ćete htjeti filtrirati i recepte s sirom, pa je potrebno biti jasan.

- **Izrada popisa za kupovinu**. Želimo izraditi popis za kupovinu, uzimajući u obzir ono što već imamo kod kuće.

  Za ovu funkcionalnost mogli bismo pokušati riješiti sve u jednom upitu ili bismo to mogli podijeliti u dva upita. Pokušajmo s drugim pristupom. Ovdje predlažemo dodavanje dodatnog upita, ali da bi to funkcioniralo, trebamo dodati rezultat prvog upita kao kontekst za drugi upit.

  Pronađite dio u kodu koji ispisuje rezultat prvog upita i dodajte sljedeći kod ispod:
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

  Obratite pažnju na sljedeće:

  1. Kreiramo novi prompt dodavanjem rezultata iz prvog prompta u novi prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Postavljamo novi zahtjev, ali također uzimamo u obzir broj tokena koji smo tražili u prvom promptu, pa ovaj put postavljamo `max_tokens` na 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Isprobavajući ovaj kod, dolazimo do sljedećeg rezultata:

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

Ono što imamo do sada je kod koji radi, ali postoje neke prilagodbe koje bismo trebali napraviti kako bismo dodatno poboljšali stvari. Neke od stvari koje bismo trebali učiniti su:

- **Odvojite tajne od koda**, poput API ključa. Tajne ne pripadaju kodu i trebale bi se čuvati na sigurnom mjestu. Kako bismo odvojili tajne od koda, možemo koristiti varijable okruženja i biblioteke poput `python-dotenv` za učitavanje iz datoteke. Evo kako bi to izgledalo u kodu:

  1. Kreirajte `.env` datoteku sa sljedećim sadržajem:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Napomena, za Azure, trebate postaviti sljedeće varijable okruženja:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     U kodu biste učitali varijable okruženja na sljedeći način:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Riječ o duljini tokena**. Trebali bismo razmotriti koliko tokena trebamo za generiranje teksta koji želimo. Tokeni koštaju novac, pa gdje god je moguće, trebali bismo pokušati biti ekonomični s brojem tokena koje koristimo. Na primjer, možemo li formulirati prompt tako da koristimo manje tokena?

  Za promjenu broja korištenih tokena, možete koristiti parametar `max_tokens`. Na primjer, ako želite koristiti 100 tokena, učinili biste sljedeće:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Eksperimentiranje s temperaturom**. Temperatura je nešto što dosad nismo spomenuli, ali je važan kontekst za način na koji naš program funkcionira. Što je viša vrijednost temperature, to će izlaz biti nasumičniji. Suprotno tome, što je niža vrijednost temperature, to će izlaz biti predvidljiviji. Razmislite želite li varijaciju u svom izlazu ili ne.

  Za promjenu temperature, možete koristiti parametar `temperature`. Na primjer, ako želite koristiti temperaturu od 0.5, učinili biste sljedeće:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Napomena, što je bliže 1.0, to je izlaz raznovrsniji.

## Zadatak

Za ovaj zadatak, možete odabrati što želite izraditi.

Evo nekoliko prijedloga:

- Prilagodite aplikaciju za generiranje recepata kako biste je dodatno poboljšali. Eksperimentirajte s vrijednostima temperature i promptovima kako biste vidjeli što možete postići.
- Izradite "study buddy". Ova aplikacija trebala bi moći odgovarati na pitanja o nekoj temi, na primjer Pythonu. Mogli biste imati promptove poput "Što je određena tema u Pythonu?" ili prompt koji kaže "Pokaži mi kod za određenu temu" itd.
- Povijesni bot, oživite povijest, uputite bot da glumi određenog povijesnog lika i postavljajte mu pitanja o njegovom životu i vremenu.

## Rješenje

### Study buddy

Ispod je početni prompt, pogledajte kako ga možete koristiti i prilagoditi prema svojim željama.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Povijesni bot

Evo nekih promptova koje biste mogli koristiti:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Provjera znanja

Što radi koncept temperature?

1. Kontrolira koliko je izlaz nasumičan.
1. Kontrolira koliko je velik odgovor.
1. Kontrolira koliko se tokena koristi.

## 🚀 Izazov

Dok radite na zadatku, pokušajte varirati temperaturu, pokušajte je postaviti na 0, 0.5 i 1. Zapamtite da je 0 najmanje raznovrsno, a 1 najraznovrsnije. Koja vrijednost najbolje funkcionira za vašu aplikaciju?

## Odlično obavljeno! Nastavite učiti

Nakon što završite ovu lekciju, pogledajte našu [Generative AI Learning kolekciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kako biste nastavili unapređivati svoje znanje o generativnoj umjetnoj inteligenciji!

Prijeđite na Lekciju 7 gdje ćemo pogledati kako [izraditi aplikacije za chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.