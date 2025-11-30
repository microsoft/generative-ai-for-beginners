<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-18T01:38:19+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "sl"
}
-->
# Gradnja aplikacij za generiranje besedila

[![Gradnja aplikacij za generiranje besedila](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.sl.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite zgornjo sliko za ogled videa te lekcije)_

V tem učnem načrtu ste doslej spoznali osnovne koncepte, kot so pozivi, in celo celotno disciplino, imenovano "inženiring pozivov". Številna orodja, s katerimi lahko komunicirate, kot so ChatGPT, Office 365, Microsoft Power Platform in druga, vam omogočajo uporabo pozivov za dosego določenega cilja.

Če želite takšno izkušnjo dodati v aplikacijo, morate razumeti koncepte, kot so pozivi, zaključki, in izbrati knjižnico za delo. Točno to boste spoznali v tem poglavju.

## Uvod

V tem poglavju boste:

- Spoznali knjižnico openai in njene osnovne koncepte.
- Zgradili aplikacijo za generiranje besedila z uporabo openai.
- Razumeli, kako uporabiti koncepte, kot so poziv, temperatura in žetoni, za gradnjo aplikacije za generiranje besedila.

## Cilji učenja

Na koncu te lekcije boste lahko:

- Razložili, kaj je aplikacija za generiranje besedila.
- Zgradili aplikacijo za generiranje besedila z uporabo openai.
- Konfigurirali svojo aplikacijo za uporabo več ali manj žetonov ter spreminjali temperaturo za raznolik izhod.

## Kaj je aplikacija za generiranje besedila?

Običajno ima aplikacija, ki jo zgradite, nekakšen vmesnik, kot je naslednji:

- Na osnovi ukazov. Konzolne aplikacije so tipične aplikacije, kjer vnesete ukaz in ta izvede nalogo. Na primer, `git` je aplikacija na osnovi ukazov.
- Uporabniški vmesnik (UI). Nekatere aplikacije imajo grafične uporabniške vmesnike (GUI), kjer klikate gumbe, vnašate besedilo, izbirate možnosti in več.

### Omejitve konzolnih in UI aplikacij

Primerjajte to z aplikacijo na osnovi ukazov, kjer vnesete ukaz:

- **Je omejeno**. Ne morete vnesti kar koli, le ukaze, ki jih aplikacija podpira.
- **Je jezikovno specifično**. Nekatere aplikacije podpirajo več jezikov, vendar je aplikacija privzeto zgrajena za določen jezik, tudi če lahko dodate podporo za več jezikov.

### Prednosti aplikacij za generiranje besedila

Kako se torej aplikacija za generiranje besedila razlikuje?

V aplikaciji za generiranje besedila imate večjo prilagodljivost, niste omejeni na nabor ukazov ali določen vhodni jezik. Namesto tega lahko uporabljate naravni jezik za interakcijo z aplikacijo. Druga prednost je, da že komunicirate z virom podatkov, ki je bil usposobljen na obsežnem korpusu informacij, medtem ko je tradicionalna aplikacija morda omejena na tisto, kar je v bazi podatkov.

### Kaj lahko zgradim z aplikacijo za generiranje besedila?

Obstaja veliko stvari, ki jih lahko zgradite. Na primer:

- **Klepetalni robot**. Klepetalni robot, ki odgovarja na vprašanja o temah, kot so vaše podjetje in njegovi izdelki, bi lahko bil dobra izbira.
- **Pomočnik**. LLM-ji so odlični pri stvareh, kot so povzemanje besedila, pridobivanje vpogledov iz besedila, ustvarjanje besedila, kot so življenjepisi, in več.
- **Pomočnik za kodiranje**. Odvisno od modela jezika, ki ga uporabljate, lahko zgradite pomočnika za kodiranje, ki vam pomaga pisati kodo. Na primer, lahko uporabite izdelek, kot je GitHub Copilot, ali ChatGPT za pomoč pri pisanju kode.

## Kako začeti?

Najti morate način za integracijo z LLM, kar običajno vključuje naslednja dva pristopa:

- Uporaba API-ja. Tukaj sestavljate spletne zahteve s svojim pozivom in dobite generirano besedilo nazaj.
- Uporaba knjižnice. Knjižnice pomagajo inkapsulirati klice API-ja in jih narediti enostavnejše za uporabo.

## Knjižnice/SDK-ji

Obstaja nekaj dobro znanih knjižnic za delo z LLM-ji, kot so:

- **openai**, ta knjižnica omogoča enostavno povezavo z vašim modelom in pošiljanje pozivov.

Potem so tu še knjižnice, ki delujejo na višji ravni, kot so:

- **Langchain**. Langchain je dobro znan in podpira Python.
- **Semantic Kernel**. Semantic Kernel je knjižnica podjetja Microsoft, ki podpira jezike C#, Python in Java.

## Prva aplikacija z uporabo openai

Poglejmo, kako lahko zgradimo svojo prvo aplikacijo, katere knjižnice potrebujemo, koliko je potrebno in tako naprej.

### Namestitev openai

Obstaja veliko knjižnic za interakcijo z OpenAI ali Azure OpenAI. Možno je uporabljati številne programske jezike, kot so C#, Python, JavaScript, Java in več. Izbrali smo uporabo Python knjižnice `openai`, zato jo bomo namestili z `pip`.

```bash
pip install openai
```

### Ustvarite vir

Izvesti morate naslednje korake:

- Ustvarite račun na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pridobite dostop do Azure OpenAI. Obiščite [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) in zaprosite za dostop.

  > [!NOTE]
  > V času pisanja je potrebno zaprositi za dostop do Azure OpenAI.

- Namestite Python <https://www.python.org/>
- Ustvarite vir storitve Azure OpenAI. Oglejte si ta vodič za [ustvarjanje vira](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Poiščite API ključ in končno točko

Na tej točki morate knjižnici `openai` povedati, kateri API ključ naj uporablja. Če želite najti svoj API ključ, pojdite na razdelek "Keys and Endpoint" v svojem viru Azure OpenAI in kopirajte vrednost "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Zdaj, ko ste kopirali te informacije, knjižnicam povejte, naj jih uporabijo.

> [!NOTE]
> Vredno je ločiti vaš API ključ od kode. To lahko storite z uporabo okoljskih spremenljivk.
>
> - Nastavite okoljsko spremenljivko `OPENAI_API_KEY` na vaš API ključ.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavitev konfiguracije Azure

Če uporabljate Azure OpenAI, tukaj je, kako nastavite konfiguracijo:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Zgoraj nastavljamo naslednje:

- `api_type` na `azure`. To pove knjižnici, naj uporablja Azure OpenAI in ne OpenAI.
- `api_key`, to je vaš API ključ, ki ga najdete v Azure Portalu.
- `api_version`, to je različica API-ja, ki jo želite uporabiti. V času pisanja je najnovejša različica `2023-05-15`.
- `api_base`, to je končna točka API-ja. Najdete jo v Azure Portalu poleg vašega API ključa.

> [!NOTE] > `os.getenv` je funkcija, ki bere okoljske spremenljivke. Uporabite jo lahko za branje okoljskih spremenljivk, kot sta `OPENAI_API_KEY` in `API_BASE`. Te okoljske spremenljivke nastavite v svojem terminalu ali z uporabo knjižnice, kot je `dotenv`.

## Generiranje besedila

Način generiranja besedila je uporaba razreda `Completion`. Tukaj je primer:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

V zgornji kodi ustvarimo objekt za zaključek in podamo model, ki ga želimo uporabiti, ter poziv. Nato natisnemo generirano besedilo.

### Zaključki klepeta

Doslej ste videli, kako smo uporabljali `Completion` za generiranje besedila. Obstaja pa še en razred, imenovan `ChatCompletion`, ki je bolj primeren za klepetalne robote. Tukaj je primer uporabe:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Več o tej funkcionalnosti v prihajajočem poglavju.

## Vaja - vaša prva aplikacija za generiranje besedila

Zdaj, ko smo se naučili, kako nastaviti in konfigurirati openai, je čas, da zgradimo svojo prvo aplikacijo za generiranje besedila. Za gradnjo aplikacije sledite tem korakom:

1. Ustvarite virtualno okolje in namestite openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Če uporabljate Windows, vnesite `venv\Scripts\activate` namesto `source venv/bin/activate`.

   > [!NOTE]
   > Poiščite svoj Azure OpenAI ključ tako, da obiščete [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), poiščete `Open AI` in izberete `Open AI resource`, nato pa izberete `Keys and Endpoint` ter kopirate vrednost `Key 1`.

1. Ustvarite datoteko _app.py_ in vanjo vnesite naslednjo kodo:

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
   > Če uporabljate Azure OpenAI, morate nastaviti `api_type` na `azure` in `api_key` na svoj Azure OpenAI ključ.

   Videti bi morali izhod, podoben naslednjemu:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Različne vrste pozivov za različne namene

Zdaj ste videli, kako generirati besedilo z uporabo poziva. Imate celo program, ki ga lahko spreminjate in prilagajate za generiranje različnih vrst besedila.

Pozivi se lahko uporabljajo za različne naloge. Na primer:

- **Generiranje vrste besedila**. Na primer, lahko generirate pesem, vprašanja za kviz itd.
- **Iskanje informacij**. Pozive lahko uporabite za iskanje informacij, kot je naslednji primer 'Kaj pomeni CORS v spletnem razvoju?'.
- **Generiranje kode**. Pozive lahko uporabite za generiranje kode, na primer za razvoj regularnega izraza za preverjanje veljavnosti e-poštnih naslovov ali zakaj ne bi generirali celotnega programa, kot je spletna aplikacija?

## Bolj praktičen primer: generator receptov

Predstavljajte si, da imate doma sestavine in želite nekaj skuhati. Za to potrebujete recept. Način, kako najti recepte, je uporaba iskalnika ali pa lahko za to uporabite LLM.

Lahko napišete poziv, kot je:

> "Pokaži mi 5 receptov za jed z naslednjimi sestavinami: piščanec, krompir in korenje. Za vsak recept naštej vse uporabljene sestavine."

Glede na zgornji poziv lahko dobite odgovor, podoben temu:

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

Ta rezultat je odličen, vem, kaj lahko skuham. Na tej točki bi bile koristne naslednje izboljšave:

- Filtriranje sestavin, ki mi niso všeč ali na katere sem alergičen.
- Ustvarjanje nakupovalnega seznama, če doma nimam vseh sestavin.

Za zgornje primere dodajmo dodaten poziv:

> "Prosim, odstrani recepte s česnom, saj sem nanj alergičen, in ga zamenjaj z nečim drugim. Prav tako prosim, da ustvariš nakupovalni seznam za recepte, upoštevajoč, da imam doma že piščanca, krompir in korenje."

Zdaj imate nov rezultat, in sicer:

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

To je vaših pet receptov, brez omembe česna, poleg tega pa imate tudi nakupovalni seznam, ki upošteva, kaj že imate doma.

## Vaja - zgradite generator receptov

Zdaj, ko smo preigrali scenarij, napišimo kodo, ki ustreza prikazanemu scenariju. Za to sledite tem korakom:

1. Uporabite obstoječo datoteko _app.py_ kot izhodišče.
1. Poiščite spremenljivko `prompt` in spremenite njeno kodo v naslednjo:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Če zdaj zaženete kodo, bi morali videti izhod, podoben:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, vaš LLM je nedeterminističen, zato lahko ob vsakem zagonu programa dobite različne rezultate.

   Odlično, poglejmo, kako lahko stvari izboljšamo. Da bi izboljšali stvari, želimo zagotoviti, da je koda prilagodljiva, tako da je mogoče izboljšati in spremeniti sestavine ter število receptov.

1. Spremenimo kodo na naslednji način:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testni zagon kode bi lahko izgledal takole:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Izboljšava z dodajanjem filtra in nakupovalnega seznama

Zdaj imamo delujočo aplikacijo, ki je sposobna ustvariti recepte, in je prilagodljiva, saj se zanaša na vnose uporabnika, tako glede števila receptov kot tudi uporabljenih sestavin.

Za nadaljnjo izboljšavo želimo dodati naslednje:

- **Filtriranje sestavin**. Želimo imeti možnost filtriranja sestavin, ki nam niso všeč ali na katere smo alergični. Za izvedbo te spremembe lahko uredimo obstoječi poziv in na njegov konec dodamo pogoj za filtriranje, kot je:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Zgoraj dodamo `{filter}` na konec poziva in zajamemo vrednost filtra od uporabnika.

  Primer vnosa pri zagonu programa lahko zdaj izgleda takole:

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

  Kot vidite, so bili vsi recepti z mlekom izločeni. Če pa ste intolerantni na laktozo, boste morda želeli izločiti tudi recepte s sirom, zato je pomembno biti jasen.

- **Ustvarjanje nakupovalnega seznama**. Želimo ustvariti nakupovalni seznam, upoštevajoč, kaj že imamo doma.

  Za to funkcionalnost bi lahko poskusili rešiti vse v enem pozivu ali pa bi to razdelili na dva poziva. Poskusimo slednji pristop. Tukaj predlagamo dodajanje dodatnega poziva, vendar za to potrebujemo rezultat prvega poziva kot kontekst za drugi poziv.

  Poiščite del kode, ki natisne rezultat prvega poziva, in spodaj dodajte naslednjo kodo:
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

  Upoštevajte naslednje:

  1. Sestavljamo nov poziv tako, da dodamo rezultat prvega poziva k novemu pozivu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Naredimo novo zahtevo, pri čemer upoštevamo število žetonov, ki smo jih zahtevali v prvem pozivu, zato tokrat nastavimo `max_tokens` na 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Ko preizkusimo to kodo, pridemo do naslednjega izhoda:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Izboljšajte svojo nastavitev

Kar imamo do sedaj, je koda, ki deluje, vendar obstajajo nekatere prilagoditve, ki bi jih morali narediti, da bi stvari še izboljšali. Nekaj stvari, ki bi jih morali storiti, so:

- **Ločite skrivnosti od kode**, kot je API ključ. Skrivnosti ne sodijo v kodo in jih je treba shraniti na varno mesto. Za ločitev skrivnosti od kode lahko uporabimo okoljske spremenljivke in knjižnice, kot je `python-dotenv`, da jih naložimo iz datoteke. Tukaj je primer, kako bi to izgledalo v kodi:

  1. Ustvarite datoteko `.env` z naslednjo vsebino:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Opomba, za Azure morate nastaviti naslednje okoljske spremenljivke:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     V kodi bi okoljske spremenljivke naložili takole:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Beseda o dolžini žetonov**. Morali bi razmisliti, koliko žetonov potrebujemo za generiranje besedila, ki ga želimo. Žetoni stanejo denar, zato bi morali, kjer je to mogoče, poskušati biti varčni pri številu uporabljenih žetonov. Na primer, ali lahko oblikujemo poziv tako, da uporabimo manj žetonov?

  Za spremembo uporabljenih žetonov lahko uporabite parameter `max_tokens`. Na primer, če želite uporabiti 100 žetonov, bi to storili takole:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Eksperimentiranje s temperaturo**. Temperatura je nekaj, česar do sedaj nismo omenjali, vendar je pomemben kontekst za delovanje našega programa. Višja kot je vrednost temperature, bolj naključen bo izhod. Nasprotno, nižja kot je vrednost temperature, bolj predvidljiv bo izhod. Razmislite, ali želite variacije v svojem izhodu ali ne.

  Za spremembo temperature lahko uporabite parameter `temperature`. Na primer, če želite uporabiti temperaturo 0.5, bi to storili takole:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Opomba, bližje kot je vrednost 1.0, bolj raznolik bo izhod.

## Naloga

Za to nalogo lahko izberete, kaj želite zgraditi.

Tukaj je nekaj predlogov:

- Prilagodite aplikacijo za generiranje receptov, da jo še izboljšate. Eksperimentirajte z vrednostmi temperature in pozivi, da vidite, kaj lahko ustvarite.
- Zgradite "učnega pomočnika". Ta aplikacija bi morala biti sposobna odgovarjati na vprašanja o določeni temi, na primer Python. Lahko bi imeli pozive, kot so "Kaj je določena tema v Pythonu?", ali pa poziv, ki pravi, pokaži mi kodo za določeno temo itd.
- Zgodovinski bot, oživite zgodovino, naročite botu, naj igra določen zgodovinski lik in mu postavljajte vprašanja o njegovem življenju in času.

## Rešitev

### Učni pomočnik

Spodaj je začetni poziv, poglejte, kako ga lahko uporabite in prilagodite svojim željam.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Zgodovinski bot

Tukaj so nekateri pozivi, ki bi jih lahko uporabili:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Preverjanje znanja

Kaj počne koncept temperature?

1. Nadzira, kako naključen je izhod.
1. Nadzira, kako velik je odziv.
1. Nadzira, koliko žetonov se uporabi.

## 🚀 Izziv

Med delom na nalogi poskusite spreminjati temperaturo, poskusite jo nastaviti na 0, 0.5 in 1. Ne pozabite, da je 0 najmanj raznolik, 1 pa najbolj raznolik. Katera vrednost najbolje deluje za vašo aplikacijo?

## Odlično delo! Nadaljujte z učenjem

Po zaključku te lekcije si oglejte našo [zbirko učenja o generativni umetni inteligenci](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da še naprej nadgrajujete svoje znanje o generativni umetni inteligenci!

Pojdite na lekcijo 7, kjer bomo pogledali, kako [zgraditi klepetalne aplikacije](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.