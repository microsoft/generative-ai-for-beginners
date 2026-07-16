# Teksto generavimo programų kūrimas

[![Teksto generavimo programų kūrimas](../../../translated_images/lt/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Iki šiol šioje mokymo programoje matėte, kad yra pagrindinės sąvokos, tokios kaip užklausos, ir net visa disciplina, vadinama „užklausų inžinerija“. Daugelis įrankių, su kuriais galite bendrauti, kaip ChatGPT, Office 365, Microsoft Power Platform ir kiti, leidžia jums naudoti užklausas norint ką nors atlikti.

Norėdami pridėti tokią patirtį prie programos, turite suprasti tokias sąvokas kaip užklausos, užbaigimai ir pasirinkti biblioteką darbui. Būtent to išmoksite šiame skyriuje.

## Įvadas

Šiame skyriuje jūs:

- Sužinosite apie openai biblioteką ir jos pagrindines sąvokas.
- Kursite teksto generavimo programą naudodami openai.
- Suprasite, kaip naudoti tokias sąvokas kaip užklausa, temperatūra ir žetonai, kad sukurtumėte teksto generavimo programą.

## Mokymosi tikslai

Pamokos pabaigoje jūs galėsite:

- Paaiškinti, kas yra teksto generavimo programa.
- Sukurti teksto generavimo programą naudodami openai.
- Konfigūruoti savo programą naudoti daugiau ar mažiau žetonų ir pakeisti temperatūrą, kad būtų įvairus išvesties rezultatas.

## Kas yra teksto generavimo programa?

Paprastai kurdami programą, ji turi tam tikrą sąsają, kaip štai tokia:

- Komandų pagrindu. Konsolės programos yra tipinės programos, kuriose įvedate komandą ir ji atlieka užduotį. Pavyzdžiui, `git` yra komandų pagrindu veikianti programa.
- Vartotojo sąsaja (UI). Kai kurios programos turi grafinę vartotojo sąsają (GUI), kur spustelite mygtukus, įvedate tekstą, renkatės parinktis ir t. t.

### Konsolės ir UI programos yra ribotos

Palyginkite su komandų programa, kurioje įvedate komandą:

- **Ji yra ribota**. Negalite įvesti bet kokios komandos, tik tų, kurias programa palaiko.
- **Kalbai specifinė**. Kai kurios programos palaiko daug kalbų, bet pagal numatytuosius nustatymus programa skirta konkrečiai kalbai, net jei galite pridėti daugiau kalbų palaikymo.

### Teksto generavimo programų privalumai

Kaip teksto generavimo programa skiriasi?

Teksto generavimo programoje turite daugiau lankstumo, nesate apriboti komandomis ar konkrečia įvesties kalba. Vietoj to galite naudoti natūralią kalbą bendrauti su programa. Kitas privalumas – jūs jau bendraujate su duomenų šaltiniu, kuris buvo apmokytas didelėje informacijos bazėje, o tradicinė programa gali būti apribota turimais duomenimis.

### Ką galiu sukurti naudodamasis teksto generavimo programa?

Galite sukurti daugybę dalykų. Pavyzdžiui:

- **Pokalbį vedantį robotą**. Pokalbį vedantis robotas, atsakantis į klausimus apie jūsų įmonę ir jos produktus, būtų geras pasirinkimas.
- **Pagalbą**. LLM puikiai tinka tokiems dalykams kaip teksto santraukos, įžvalgų pateikimas, teksto generavimas, pvz., gyvenimo aprašymams ir pan.
- **Kodo asistentą**. Priklausomai nuo naudojamo kalbos modelio, galite sukurti kodo asistentą, kuris padės rašyti kodą. Pavyzdžiui, galite naudoti GitHub Copilot produktą arba ChatGPT, kad padėtų rašyti kodą.

## Kaip pradėti?

Turite rasti būdą, kaip integruotis su LLM – paprastai tai reiškia šiuos du metodus:

- Naudoti API. Čia kuriate internetinius užklausimus su savo užklausa ir gaunate sugeneruotą tekstą atgal.
- Naudoti biblioteką. Bibliotekos padeda suvynioti API kvietimus ir palengvina jų naudojimą.

## Bibliotekos/SDK

Yra keletas gerai žinomų bibliotekų darbui su LLM, pvz.:

- **openai**, ši biblioteka leidžia lengvai prisijungti prie savo modelio ir siųsti užklausas.

Yra ir aukštesnio lygio bibliotekų, pvz.:

- **Langchain**. Langchain yra gerai žinoma ir palaiko Python.
- **Semantic Kernel**. Semantic Kernel yra Microsoft biblioteka, palaikanti C#, Python ir Java kalbas.

## Pirmoji programa naudojant openai

Pažiūrėkime, kaip sukurti pirmąją programą, kokių bibliotekų reikia, kiek tai užtrunka ir pan.

### Įdiegti openai

Yra daug bibliotekų darbui su OpenAI ar Azure OpenAI. Galima naudoti įvairias programavimo kalbas, tokias kaip C#, Python, JavaScript, Java ir kt. Mes pasirinkome naudoti `openai` Python biblioteką, tad naudosime `pip` jos įdiegimui.

```bash
pip install openai
```

### Sukurti resursą

Turite atlikti šiuos veiksmus:

- Sukurti paskyrą Azure svetainėje [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Gauti prieigą prie Azure OpenAI. Eikite į [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ir paprašykite prieigos.

  > [!NOTE]
  > Rašymo metu reikia pateikti paraišką gauti Azure OpenAI prieigą.

- Įdiegti Python <https://www.python.org/>
- Sukurti Azure OpenAI paslaugos resursą. Šiame vadove pažiūrėkite, kaip [sukurti resursą](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Raskite API raktą ir galutinį tašką

Šiuo metu turite nurodyti, kokį API raktą turėtų naudoti jūsų `openai` biblioteka. Norėdami rasti API raktą, eikite į „Keys and Endpoint“ skiltį savo Azure OpenAI resurse ir nukopijuokite „Key 1“ reikšmę.

![Raktų ir galutinio taško resurso skydelis Azure portale](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Kai turite šią informaciją nukopijuotą, duokime instrukcijas bibliotekai ją naudoti.

> [!NOTE]
> Verta atskirti API raktą nuo kodo. Tai galite padaryti naudojant aplinkos kintamuosius.
>
> - Nustatykite aplinkos kintamąjį `OPENAI_API_KEY` savo API raktu.
>   `export OPENAI_API_KEY='sk-...'`

### Azure konfigūracijos nustatymas

Jei naudojate Azure OpenAI (dabar Microsoft Foundry dalis), štai kaip nustatyti konfigūraciją. Naudojame standartinį `OpenAI` klientą, nukreiptą į Azure OpenAI `/openai/v1/` galinį tašką, kuris veikia su Responses API ir nereikalauja `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Aukščiau nustatome:

- `api_key`, tai jūsų Azure portale arba Microsoft Foundry portale rastas API raktas.
- `base_url`, tai jūsų Foundry resurso galinis taškas su pridėtu `/openai/v1/`. Stabilus v1 galinis taškas veikia tiek OpenAI, tiek Azure OpenAI be `api_version` valdymo.

> [!NOTE] > `os.environ` skaito aplinkos kintamuosius. Jūs galite jį naudoti skaityti tokius kintamuosius kaip `AZURE_OPENAI_API_KEY` ir `AZURE_OPENAI_ENDPOINT`. Nustatykite šiuos kintamuosius terminale arba naudodami biblioteką kaip `dotenv`.

## Teksto generavimas

Teksto generuoti galima naudojant Responses API per `responses.create` metodą. Štai pavyzdys:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # tai yra jūsų modelio diegimo pavadinimas
    input=prompt,
    store=False,
)
print(response.output_text)
```

Aukščiau esantį kode sukuriame atsakymą, nurodydami norimą naudoti modelį ir užklausą. Tada išvedame sugeneruotą tekstą per `response.output_text`.

### Daugiaturniai pokalbiai

Responses API puikiai tinka tiek vieno karto teksto generavimui, tiek daugiaturniams pokalbiams – jūs pateikiate žinučių sąrašą `input` argumente, kad sukurtumėte pokalbį:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Apie šią funkciją skaitykite būsimame skyriuje.

## Užduotis – jūsų pirmoji teksto generavimo programa

Dabar, kai išmokome, kaip nustatyti ir sukonfigūruoti openai, metas sukurti jūsų pirmąją teksto generavimo programą. Norėdami ją sukurti, atlikite šiuos veiksmus:

1. Sukurkite virtualią aplinką ir įdiekite openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jei naudojate Windows, rašykite `venv\Scripts\activate` vietoje `source venv/bin/activate`.

   > [!NOTE]
   > Raskite savo Azure OpenAI raktą eidami į [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), ieškokite `Open AI`, pasirinkite `Open AI resursą`, tuomet pasirinkite `Keys and Endpoint` ir nukopijuokite `Key 1` reikšmę.

1. Sukurkite failą _app.py_ ir įrašykite jame šį kodą:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # pridėkite savo užbaigimo kodą
   prompt = "Complete the following: Once upon a time there was a"

   # atlikite užklausą naudodami Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # spausdinkite atsakymą
   print(response.output_text)
   ```

   > [!NOTE]
   > Jei naudojate paprastą OpenAI (ne Azure), naudokite `client = OpenAI(api_key="<pakeiskite šią reikšmę savo OpenAI raktu>")` (nereikia `base_url`) ir perduokite modelio pavadinimą, pavyzdžiui, `gpt-4o-mini`, o ne diegimo vardą.

   Jums turėtų būti parodytas toks išvesties pavyzdys:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Skirtingų tipų užklausos, skirtingiems dalykams

Dabar matote, kaip generuoti tekstą naudojant užklausą. Jūs netgi turite programą, kuri veikia ir kurią galite keisti, kad generuotumėte skirtingo tipo tekstus.

Užklausos gali būti naudojamos įvairioms užduotims. Pavyzdžiui:

- **Generuoti tam tikrą tekstą**. Pavyzdžiui, galite generuoti eilėraštį, klausimus viktorinai ir pan.
- **Ieškoti informacijos**. Galite naudoti užklausas ieškant informacijos, kaip pavyzdžiui 'Ką reiškia CORS interneto plėtroje?'.
- **Generuoti kodą**. Galite naudoti užklausas kodui generuoti, pvz., kurti reguliarias išraiškas el. pašto adresų patikrai ar net visą programą, pvz., interneto programą?

## Praktinis pavyzdys: receptų generatorius

Įsivaizduokite, kad namuose turite ingredientų ir norite ką nors pagaminti. Tam jums reikia recepto. Receptų galite ieškoti paieškos varikliu arba naudoti LLM.

Galite parašyti užklausą taip:

> "Parodyk man 5 receptus patiekalams su šiais ingredientais: vištiena, bulvės ir morkos. Kiekvienam receptui išvardink visus naudojamus ingredientus"

Gavę tokią užklausą, galite gauti atsakymą panašų į:

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

Šis rezultatas puikus, žinau, ką gaminti. Šiuo metu galimi tokie patobulinimai:

- Filtruoti ingredientus, kurie man nepatinka arba į kuriuos esu alergiškas.
- Sudaryti pirkinių sąrašą, jei namuose neturiu visų ingredientų.

Pridėsime papildomą užklausą šiems atvejams:

> "Prašau pašalinti receptus su česnaku, nes esu alergiškas, ir pakeisti jį kažkuo kitu. Taip pat, prašau sudaryti pirkinių sąrašą tiems receptams, atsižvelgiant į tai, kad namuose jau turiu vištienos, bulvių ir morkų."

Dabar turite naują rezultatą, būtent:

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

Tai jūsų penki receptai be česnako ir turite pirkinių sąrašą, atsižvelgiant į tai, ką jau turite namuose.

## Užduotis – sukurkite receptų generatorių

Dabar, kai sužaidėme scenarijų, parašykime kodą, atitinkantį parodytą scenarijų. Norėdami tai padaryti, atlikite šiuos veiksmus:

1. Naudokite esamą _app.py_ failą kaip pradinį tašką
1. Suraskite kintamąjį `prompt` ir pakeiskite jo kodą taip:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Paleidus kodą dabar turėtumėte matyti panašią išvestį:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > PASTABA: jūsų LLM veikia nedeterministiškai, tad kiekvieną kartą paleidus programą rezultatų gali būti skirtingi.

   Puiku, pažiūrėkime, kaip galime patobulinti. Norėdami patobulinti, norime, kad kodas būtų lankstus, kad galėtume keisti ingredientus ir receptų skaičių.

1. Pakeiskime kodą šiuo būdu:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # įterpkite receptų skaičių į užklausą ir ingredientus
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Kodo testo paleidimas gali atrodyti štai taip:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Patobulinkite pridėdami filtrą ir pirkinių sąrašą

Dabar turime veikiančią programą, kuri gali generuoti receptus ir yra lanksti, nes remiasi vartotojo įvestimis, tiek receptų skaičiui, tiek ingredientams.

Norėdami toliau patobulinti, pridėsime šiuos dalykus:

- **Išfiltruoti ingredientus**. Norime turėti galimybę išfiltruoti ingredientus, kurie mums nepatinka arba į kuriuos esame alergiški. Tam pakeitime esamą užklausą ir pridėsime filtro sąlygą pabaigoje:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Aukščiau pridėjome `{filter}` prie užklausos pabaigos ir taip pat gauname filtro reikšmę iš vartotojo.

  Programos paleidimo pavyzdinė įvestis dabar gali atrodyti taip:

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

  Kaip matote, visi receptai su pienu buvo išfiltruoti. Tačiau jei esate laktozės netolerantas, galbūt norėsite filtruoti ir receptus su sūriu, tad reikia būti aiškiam.


- **Sukurkite pirkinių sąrašą**. Norime sukurti pirkinių sąrašą, atsižvelgdami į tai, ką jau turime namuose.

  Šiai funkcijai galėtume pabandyti viską išspręsti vienu užklausimu arba galėtume padalinti į du užklausimus. Išbandykime antrąjį variantą. Čia siūlome pridėti papildomą užklausimą, bet kad tai veiktų, turime pridėti pirmojo užklausimo rezultatą kaip kontekstą antrajam užklausimui.

  Suraskite kodo vietą, kur išvedamas pirmojo užklausimo rezultatas, ir pridėkite žemiau esantį kodą:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # išspausdink atsakymą
  print("Shopping list:")
  print(response.output_text)
  ```

  Atkreipkite dėmesį į šiuos dalykus:

  1. Sukuriame naują užklausimą, pridedant pirmojo užklausimo rezultatą prie naujo užklausimo:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Atliekame naują užklausą, bet taip pat atsižvelgdami į pirmojo užklausimo tokenų skaičių, todėl šį kartą `max_output_tokens` nustatome 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Patikrinus šį kodą, gauname šį rezultatą:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Patobulinkite savo aplinką

Kol kas turimo kodo yra veikiantis, bet yra keletas patobulinimų, kuriuos reikėtų atlikti toliau gerinant situaciją. Keletas dalykų, kuriuos reikėtų padaryti:

- **Atskirkite slaptažodžius nuo kodo**, pavyzdžiui, API raktą. Slaptažodžiai nepriklauso kode ir turi būti saugomi saugioje vietoje. Slaptažodžių atskyrimui nuo kodo galime naudoti aplinkos kintamuosius ir bibliotekas, tokias kaip `python-dotenv`, kad juos įkeltume iš failo. Štai kaip tai atrodytų kode:

  1. Sukurkite `.env` failą su tokiu turiniu:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Atkreipkite dėmesį, kad naudojant Azure OpenAI Microsoft Foundry, reikės nustatyti šiuos aplinkos kintamuosius:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Kode aplinkos kintamuosius įkraunate taip:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Žodis apie tokenų ilgį**. Reikia apsvarstyti, kiek tokenų mums reikia tekstui sugeneruoti. Tokenai kainuoja, todėl, kur įmanoma, reikėtų stengtis naudoti kuo mažiau tokenų. Pavyzdžiui, ar galime užklausą suformuluoti taip, kad naudotume mažiau tokenų?

  Tokenų kiekį galite keisti naudodami `max_output_tokens` parametrą. Pavyzdžiui, jei norite naudoti 100 tokenų, darytumėte taip:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimentavimas su temperatūra**. Temperatūra yra dalykas, apie kurį iki šiol nekalbėjome, bet tai svarbus kontekstas, kaip veikia mūsų programa. Kuo temperatūros reikšmė aukštesnė, tuo atsakymas bus labiau atsitiktinis. Atvirkščiai, kuo temperatūros reikšmė žemesnė, tuo atsakymas bus labiau nuspėjamas. Pagalvokite, ar norite turėti įvairovę atsakyme, ar ne.

  Temperatūrą galite keisti naudodami `temperature` parametrą. Pavyzdžiui, jei norite naudoti temperatūrą 0.5, darytumėte taip:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Atkreipkite dėmesį, kad kuo arčiau 1.0, tuo įvairesnis bus atsakymas.

## Užduotis

Šiai užduočiai galite pasirinkti, ką norite sukurti.

Štai keletas pasiūlymų:

- Pakoreguokite receptų generatoriaus programėlę, kad dar labiau ją patobulintumėte. Išbandykite skirtingas temperatūros reikšmes ir užklausas bei pažiūrėkite, ką galite sukurti.
- Sukurkite „mokymosi draugą“. Ši programėlė turėtų gebėti atsakyti į klausimus apie temą, pvz., Python, galite turėti užklausų, tokių kaip „Kas yra tam tikra Python tema?“ arba užklausą „parodyk man kodą tam tikrai temai“ ir pan.
- Istorijos botas – prikelkite istoriją gyvai, nurodykite botui vaidinti tam tikrą istorijos asmenį ir užduokite jam klausimus apie jo gyvenimą ir laikus.

## Sprendimas

### Mokymosi draugas

Žemiau pateikiamas pradinio užklausimo pavyzdys, pažiūrėkite, kaip galite jį naudoti ir koreguoti pagal savo pageidavimus.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Istorijos botas

Štai keletas užklausų, kurias galėtumėte naudoti:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Žinių patikrinimas

Ką reiškia temperatūros sąvoka?

1. Ji valdo, kiek atsakymas yra atsitiktinis.
1. Ji valdo, kokia didelė yra atsakymo apimtis.
1. Ji valdo, kiek tokenų yra naudojama.

## 🚀 Iššūkis

Dirbdami su užduotimi, bandykite keisti temperatūrą, nustatykite ją į 0, 0.5 ir 1. Atminkite, kad 0 reiškia mažiausiai įvairovių, o 1 – daugiausiai. Koks nustatymas geriausiai tinka jūsų programėlei?

## Puikus darbas! Tęskite mokymąsi

Baigę šią pamoką, peržiūrėkite mūsų [Generatyvios AI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte savo žinias apie generatyvią AI!

Eikite į 7 pamoką, kurioje sužinosite, kaip [kurti pokalbių programas](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->