# Teksto generavimo programų kūrimas

[![Teksto generavimo programų kūrimas](../../../translated_images/lt/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Spauskite aukščiau esantį vaizdą, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Iki šiol matėte per šią mokymo programą, kad yra pagrindinės sąvokos, tokios kaip užklausos ir net visa disciplina vadinama „užklausų inžinerija“. Daugelis įrankių, su kuriais galite sąveikauti, kaip ChatGPT, Office 365, Microsoft Power Platform ir kt., leidžia jums naudoti užklausas norint pasiekti tam tikrą rezultatą.

Norint tokią patirtį pridėti prie programos, turite suprasti tokias sąvokas kaip užklausos, atsakymai ir pasirinkti biblioteką darbui. Būtent to ir išmoksite šiame skyriuje.

## Įvadas

Šiame skyriuje jūs:

- Sužinosite apie openai biblioteką ir jos pagrindines sąvokas.
- Sukursite teksto generavimo programą naudodami openai.
- Suprasite, kaip naudoti tokius konceptus kaip užklausa, temperatūra ir žetonai kuriant teksto generavimo programą.

## Mokymosi tikslai

Šios pamokos pabaigoje jūs galėsite:

- Paaiškinti, kas yra teksto generavimo programa.
- Sukurti teksto generavimo programą naudojant openai.
- Konfigūruoti programą naudoti daugiau ar mažiau žetonų bei keisti temperatūrą, siekiant įvairaus rezultato.

## Kas yra teksto generavimo programa?

Paprastai, kai kuriate programą, ji turi tam tikrą vartotojo sąsają, pavyzdžiui, tokią:

- Komandų pagrindu veikianti. Konsolinės programos yra įprastos programos, kuriose įvedate komandą ir ji atlieka užduotį. Pavyzdžiui, `git` yra komandų pagrindu veikianti programa.
- Vartotojo sąsaja (UI). Kai kurios programos turi grafinę vartotojo sąsają (GUI), kur spaudžiate mygtukus, įvedate tekstą, pasirenkate parinktis ir daugiau.

### Konsolinės ir UI programos yra ribotos

Palyginkite su komandine programa, kurioje įvedate komandą:

- **Ji yra ribota**. Negalite tiesiog įvesti bet kokios komandos, tik tas, kurias programa palaiko.
- **Kalbos specifinė**. Kai kurios programos palaiko daugybę kalbų, tačiau pagal numatytuosius nustatymus programa yra sukurta konkrečiai kalbai, net jei galite pridėti daugiau kalbų palaikymą.

### Teksto generavimo programų privalumai

Tai kuo skiriasi teksto generavimo programa?

Teksto generavimo programoje turite daugiau lankstumo, nesate apriboti komandų rinkiniu ar konkrečia įvesties kalba. Vietoje to galite naudoti natūralią kalbą sąveikai su programa. Kita nauda yra ta, kad jūs jau sąveikaujate su duomenų šaltiniu, kuris buvo apmokytas pagal didelį informacijos korpusą, o tradicinė programa galėtų būti ribota tuo, kas yra duomenų bazėje.

### Ką galiu sukurti naudodamas teksto generavimo programą?

Yra daug dalykų, kuriuos galite sukurti, pavyzdžiui:

- **Pokalbių robotą**. Pokalbių robotas, atsakantis į klausimus apie temas, pavyzdžiui, jūsų įmonę ir jos produktus, gali būti puikus pasirinkimas.
- **Pagalbininką**. LLM puikiai tinka tokiems dalykams kaip teksto santraukų kūrimas, įžvalgų gavimas iš teksto, teksto generavimas kaip gyvenimo aprašymai ir daugiau.
- **Kodo asistentą**. Priklausomai nuo naudojamo kalbos modelio, galite sukurti kodo pagalbininką, kuris padeda rašyti kodą. Pavyzdžiui, galite naudoti produktus kaip GitHub Copilot bei ChatGPT, kad padėtų rašyti kodą.

## Kaip pradėti?

Na, reikia rasti būdą, kaip integruotis su LLM, kas paprastai apima šiuos du būdus:

- Naudoti API. Čia kuriate internetinius užklausimus su savo užklausa ir gaunate sugeneruotą tekstą atgal.
- Naudoti biblioteką. Bibliotekos padeda apjungti API kvietimus ir palengvina jų naudojimą.

## Bibliotekos/SDK

Yra keletas gerai žinomų bibliotekų darbui su LLM, pavyzdžiui:

- **openai**, ši biblioteka palengvina prisijungimą prie jūsų modelio ir užklausų siuntimą.

Tada yra bibliotekos, veikiančios aukštesniu lygiu, kaip:

- **Langchain**. Langchain yra gerai žinoma ir palaiko Python.
- **Semantic Kernel**. Semantic Kernel yra Microsoft sukurta biblioteka palaikanti C#, Python ir Java kalbas.

## Pirmoji programa naudojant openai

Pažiūrėkime, kaip galime sukurti pirmą programą, kokių bibliotekų reikės, kiek yra reikalavimų ir t.t.

### Įdiegti openai

Yra daugybė bibliotekų, skirtų sąveikai su OpenAI ar Azure OpenAI. Taip pat galima naudoti įvairias programavimo kalbas, kaip C#, Python, JavaScript, Java ir kitas. Pasirinkome naudoti `openai` Python biblioteką, todėl naudosime `pip` ją įdiegti.

```bash
pip install openai
```

### Sukurti išteklių

Turite atlikti šiuos veiksmus:

- Susikurti paskyrą Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Gauti prieigą prie Azure OpenAI. Eikite į [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ir pateikite prieigos prašymą.

  > [!NOTE]
  > Rašymo metu reikia pateikti prašymą gauti prieigą prie Azure OpenAI.

- Įdiegti Python <https://www.python.org/>
- Susikurti Azure OpenAI paslaugos išteklių. Kaip [sukurti išteklių](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst), žr. šią gaires.

### Rasti API raktą ir galinį tašką

Šiuo metu turite nurodyti savo `openai` bibliotekai, kurį API raktą naudoti. Norėdami rasti savo API raktą, eikite į savo Azure OpenAI ištekliaus skyrių „Raktai ir galinis taškas“ ir nukopijuokite „Raktas 1“ reikšmę.

![Raktų ir galinio taško ištekliaus skydelis Azure portale](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Dabar, kai turite šią informaciją nukopijuotą, leiskite mums nurodyti bibliotekoms ją naudoti.

> [!NOTE]
> Verta atskirti savo API raktą nuo kodo. Tai galima padaryti naudojant aplinkos kintamuosius.
>
> - Nustatykite aplinkos kintamąjį `OPENAI_API_KEY` su savo API raktu.
>   `export OPENAI_API_KEY='sk-...'`

### Nustatyti Azure konfigūraciją

Jei naudojate Azure OpenAI (dabar Microsoft Foundry dalis), taip nustatote konfigūraciją. Naudojame standartinį `OpenAI` klientą, nukreiptą į Azure OpenAI `/openai/v1/` galinį tašką, kuris veikia su Responses API ir nereikalauja `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Aukščiau nustatome šiuos dalykus:

- `api_key`, tai jūsų API raktas, rastas Azure portale ar Microsoft Foundry portale.
- `base_url`, tai jūsų Foundry išteklių galinis taškas su pridėtu `/openai/v1/`. Stabilus v1 galinis taškas veikia tiek OpenAI, tiek Azure OpenAI, nereikalaujant `api_version` valdymo.

> [!NOTE] > `os.environ` skaito aplinkos kintamuosius. Galite jį naudoti, kad perskaitytumėte aplinkos kintamuosius kaip `AZURE_OPENAI_API_KEY` ir `AZURE_OPENAI_ENDPOINT`. Nustatykite šiuos kintamuosius savo terminale arba naudodami biblioteką kaip `dotenv`.

## Teksto generavimas

Teksto generavimui naudojamas Responses API per `responses.create` metodą. Štai pavyzdys:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Aukščiau esančiame kode sukuriame atsakymą ir perduodame norimą naudoti modelį bei užklausą. Tada išvedame sugeneruotą tekstą per `response.output_text`.

### Daugiafazių pokalbių įgyvendinimas

Responses API puikiai tinka tiek vienfaziam teksto generavimui, tiek daugiafaziams pokalbių robotams – pateikiate pranešimų sąrašą `input`, kad sukurtumėte pokalbį:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Daugiau apie šią funkciją bus kitame skyriuje.

## Pratybos – jūsų pirmoji teksto generavimo programa

Dabar, kai sužinojome, kaip nustatyti ir konfigūruoti openai, laikas sukurti jūsų pirmąją teksto generavimo programą. Norėdami ją sukurti, atlikite šiuos veiksmus:

1. Sukurkite virtualią aplinką ir įdiekite openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jei naudojate Windows, įveskite `venv\Scripts\activate` vietoje `source venv/bin/activate`.

   > [!NOTE]
   > Raskite savo Azure OpenAI raktą eidami į [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ir ieškokite `Open AI`, pasirinkite `Open AI resource`, tada pasirinkite `Keys and Endpoint` ir nukopijuokite `Key 1` reikšmę.

1. Sukurkite failą _app.py_ ir įdėkite šį kodą:

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
   > Jei naudojate paprastą OpenAI (ne Azure), naudokite `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (be `base_url`) ir perduokite modelio pavadinimą, pvz., `gpt-5-mini` vietoje diegimo pavadinimo.

   Turėtumėte pamatyti rezultatą panašų į šį:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Skirtingi užklausų tipai, skirti skirtingiems tikslams

Dabar matėte, kaip sugeneruoti tekstą naudojant užklausą. Jūs jau turite programą, kuri veikia ir kurią galite keisti, kad generuotų skirtingų tipų tekstą.

Užklausos gali būti naudojamos įvairioms užduotims. Pavyzdžiui:

- **Generuoti tam tikrą tekstą**. Pavyzdžiui, galite generuoti eilėraštį, klausimus viktorinai ir pan.
- **Ieškoti informacijos**. Galite naudoti užklausas ieškoti informacijos, pvz., „Ką reiškia CORS interneto svetainių kūrime?“
- **Generuoti kodą**. Galite naudoti užklausas kurti kodą, pvz., reguliarios išraiškos, skirtos patikrinti el. pašto adresus, arba net sukurti visą programą, pavyzdžiui, internetinę programą.

## Praktinis pavyzdys: receptų generatorius

Įsivaizduokite, kad namuose turite ingredientų ir norite ką nors pagaminti. Tam jums reikia recepto. Vienas būdas rasti receptų yra naudoti paieškos variklį, o kitas – naudoti LLM.

Galite sukurti tokią užklausą:

> „Rodyk man 5 receptus patiekalams su šiais ingredientais: vištiena, bulvės ir morkos. Kiekvienam receptui išvardinkite visus ingredientus.“

Gavę aukščiau nurodytą užklausą, galite gauti atsakymą, panašų į:

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

Šis rezultatas puikus, žinau, ką gaminti. Šiuo metu tai, kas galėtų būti naudinga, yra:

- Filtruoti ingredientus, kurių nemėgstu arba kuriems esu alergiškas.
- Sudaryti pirkinių sąrašą, jei namuose neturiu visų ingredientų.

Šiems atvejams pridėsime papildomą užklausą:

> „Prašau pašalinti receptus su česnaku, nes esu alergiškas, ir pakeisti kitu ingredientu. Taip pat sukurkite pirkinių sąrašą pagal receptus, atsižvelgdami, kad namuose jau turiu vištieną, bulves ir morkas.“

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

Tai jūsų penki receptai be jokio česnako ir taip pat turite pirkinių sąrašą, atsižvelgiant į tai, ką jau turite namuose.

## Pratybos – sukurkite receptų generatorių

Dabar, kai aptarėme situaciją, parašykite kodą, atitinkantį pateiktą pavyzdį. Norėdami tai padaryti, atlikite šiuos veiksmus:

1. Naudokite esamą failą _app.py_ kaip pradinį tašką
1. Suraskite kintamąjį `prompt` ir pakeiskite jo kodą taip:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Paleidus šį kodą, turėtumėte gauti panašų rezultatą:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > PASTABA, jūsų LLM yra nedeterministinis, todėl kiekvieną kartą paleidus programą galite gauti skirtingus rezultatus.

   Puiku, pažiūrėkime, kaip galime patobulinti. Norėdami patobulinti, turime užtikrinti, kad kodas būtų lankstus, todėl ingredientai ir receptų skaičius gali būti keičiamas.

1. Pakeiskime kodą taip:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testuojant kodą, jis gali atrodyti taip:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Pagerinkite pridėdami filtrą ir pirkinių sąrašą

Dabar turime veikiančią programą, galinčią kurti receptus, ir ji yra lanksti, nes leidžia keisti vartotojo įvestis, tiek receptų skaičių, tiek ingredientus.

Norėdami toliau tobulinti, pridėsime šiuos dalykus:

- **Filtruoti ingredientus**. Norime galėti filtruoti ingredientus, kurių nemėgstame arba esame alergiški. Norėdami tai pasiekti, galime redaguoti esamą užklausą ir pridėti filter kriterijų prie jos pabaigos taip:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Aukščiau prie užklausos pabaigos pridedame `{filter}` ir taip pat gauname filtro reikšmę iš vartotojo.

  Pavyzdinė programos įvestis dabar gali atrodyti taip:

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

  Kaip matote, visi receptai, kuriuose yra pieno, buvo atmesti. Bet jei esate laktozės netolerantas, taip pat norėtumėte atmesti receptus su sūriu, todėl aiškumas yra būtinas.

- **Sukurti pirkinių sąrašą**. Norime sukurti pirkinių sąrašą, atsižvelgiant į tai, ką jau turime namuose.

  Dėl šios funkcijos galėtume bandyti viską išspręsti viena užklausa arba padalinti į dvi užklausas. Išbandykime antrą variantą. Čia siūlome pridėti papildomą užklausą, bet tam reikės pirmos užklausos rezultatus naudoti kaip kontekstą antroje užklausoje.

  Suraskite kodą, kuris išveda pirmos užklausos rezultatą, ir pridėkite žemiau šį kodą:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Atkreipkite dėmesį į šiuos dalykus:

  1. Kuriame naują užklausą, pridėdami pirmos užklausos rezultatus prie naujos užklausos:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Mes darome naują užklausą, bet taip pat atsižvelgiame į žetonų skaičių, kurį paprašėme pirmajame raginime, taigi šį kartą sakome, kad `max_output_tokens` yra 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Vykdydami šį kodą, dabar gauname tokį rezultatą:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Tobulinkite savo sąranką

Ką turime iki šiol, tai veikiantis kodas, tačiau yra keletas patobulinimų, kuriuos turėtume atlikti, kad viską dar labiau pagerintume. Kai ką turėtume padaryti:

- **Atskirti slaptažodžius nuo kodo**, pavyzdžiui, API raktą. Slaptažodžiai nepriklauso kodui ir turėtų būti saugomi saugioje vietoje. Norėdami atskirti slaptažodžius nuo kodo, galime naudoti aplinkos kintamuosius ir tokias bibliotekas kaip `python-dotenv`, kad juos įkeltume iš failo. Štai kaip tai atrodytų kode:

  1. Sukurkite `.env` failą su tokiu turiniu:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Pastaba, Azure OpenAI Microsoft Foundry atveju, vietoj to turite nustatyti šiuos aplinkos kintamuosius:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Kode aplinkos kintamuosius įkeliate taip:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Žodis apie žetonų ilgį**. Turėtume apsvarstyti, kiek žetonų reikia sugeneruoti norimą tekstą. Žetonai kainuoja, todėl, kur įmanoma, turėtume stengtis būti ekonomingi žetonų kiekiu. Pavyzdžiui, ar galime formuluoti užklausą taip, kad naudotume mažiau žetonų?

  Norėdami keisti naudojamų žetonų skaičių, galite naudoti `max_output_tokens` parametrą. Pavyzdžiui, jei norite naudoti 100 žetonų, darykite taip:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimentuokite su temperatūra**. Temperatūra yra dalykas, kurio iki šiol neaptarėme, bet ji svarbi, kaip mūsų programa veikia. Kuo didesnė temperatūros reikšmė, tuo atsitiktinesnis bus rezultatas. Atvirkščiai - kuo mažesnė temperatūra, tuo prognozuojamesnis bus rezultatas. Apsvarstykite, ar norite, kad rezultatas kisti.

  Norėdami pakeisti temperatūrą, galite naudoti `temperature` parametrą. Pavyzdžiui, jei norite naudoti temperatūrą 0.5, darykite taip:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Pastaba, kuo arčiau 1.0, tuo įvairesnis bus rezultatas.

- **Logikos modeliai nenaudoja `temperature`**. Tai svarbus 2026 metų pokytis. Dabartiniai, nepasenę Microsoft Foundry modeliai yra **logikos modeliai** (GPT-5 šeima, o-serija) - ir jie **nepalaiko `temperature` ar `top_p`** (nei `max_tokens`; naudokite `max_output_tokens`). Jei siunčiate `temperature` į `gpt-5-mini`, gausite klaidą „parametras nepalaikomas“. Taigi, norėdami išbandyti temperatūros pavyzdį aukščiau, naudokite modelį, kuris dar palaiko mėginių kontrolę - pavyzdžiui, atvirą **Llama** modelį, tokį kaip `Llama-3.3-70B-Instruct` iš [Microsoft Foundry modelių katalogo](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), kviečiamą per Foundry Models / Azure AI Inference tašką (taip pat, kaip ir `githubmodels-*` pavyzdžiai). Logikos modeliams, pvz. GPT-5, rezultatas valdomas kitaip:
  - **Užklausų kūrimas** - aiškios instrukcijos, pavyzdžiai ir struktūruota išvestis (žr. pamoką [04 - Užklausų kūrimas](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) atlieka darbą, kurį anksčiau atlikdavo mėginių reguliatoriai.
  - **Logikos valdymas** - tokie parametrai kaip pastangų/verbalumo lygis keičia logikos gylį ir įtakoja delsą bei kainą.

  Trumpai: `temperature`/`top_p` vis dar veikia daugelyje modelių (Llama, Mistral, Phi ir GPT-4.x šeimoje - nors GPT-4.x yra nykstantis), bet kryptis yra užklausų kūrimas + logikos valdymas logikos modeliams kaip GPT-5.

## Užduotis

Šiai užduočiai galite pasirinkti, ką sukurti.

Štai keletas pasiūlymų:

- Patobulinkite receptų generatoriaus programėlę, kad ji būtų dar geresnė. Pažaiskite su temperatūros reikšmėmis ir užklausomis, kad pamatytumėte, ką galite sukurti.
- Sukurkite "studijų draugą". Ši programa turėtų sugebėti atsakyti į klausimus apie temą, pavyzdžiui, Python; galite turėti tokius užklausimus kaip „Kas yra tam tikra tema Python?“ arba užklausą, kurioje būtų prašoma parodyti kodą tam tikrai temai ir pan.
- Istorijos botą: prikelkite istoriją gyvai, nurodykite botui vaidinti tam tikrą istorinę asmenybę ir užduokite jai klausimus apie gyvenimą ir laikmetį.

## Sprendimas

### Studijų draugas

Žemiau pateikiama pradinė užklausa; pažiūrėkite, kaip ją galite naudoti ir pritaikyti pagal savo skonį.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Istorijos botas

Štai keletas užklausų, kurias galite naudoti:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Žinių patikrinimas

Ką daro temperatūros sąvoka?

1. Ji kontroliuoja, kiek atsakymas yra atsitiktinis.
1. Ji kontroliuoja, kokio dydžio yra atsakymas.
1. Ji kontroliuoja, kiek naudojama žetonų.

## 🚀 Iššūkis

Dirbdami su užduotimi, pabandykite keisti temperatūrą: nustatykite ją 0, 0.5 ir 1. Atminkite, kad 0 reiškia mažiausiai įvairų, o 1 – daugiausiai. Kokia reikšmė geriausiai veikia jūsų programėlėje?

## Puikus darbas! Toliau mokykitės

Baigę šią pamoką, peržiūrėkite mūsų [Generatyviosios AI mokymų kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte žinias apie generatyviąją AI!

Eikite į 7 pamoką, kurioje apžvelgsime, kaip [kurti pokalbių programas](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->