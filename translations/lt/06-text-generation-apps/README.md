# Teksto generavimo programų kūrimas

[![Teksto generavimo programų kūrimas](../../../translated_images/lt/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Spustelėkite aukščiau esantį vaizdą, kad peržiūrėtumėte pamokos vaizdo įrašą)_

Iki šiol šiame mokymo plane matėte pagrindines koncepcijas, tokias kaip užklausos, ir net visą discipliną, vadinamą „užklausų inžinerija“. Daugelis įrankių, su kuriais galite bendrauti, kaip ChatGPT, Office 365, Microsoft Power Platform ir kt., palaiko jus naudodami užklausas tam, kad pasiektumėte tam tikrą tikslą.

Kad pridėtumėte tokią patirtį programai, turite suprasti tokias sąvokas kaip užklausos, užbaigimai ir pasirinkti biblioteką darbui su jomis. Būtent to ir išmoksite šiame skyriuje.

## Įvadas

Šiame skyriuje jūs:

- Sužinosite apie openai biblioteką ir jos pagrindines koncepcijas.
- Sukursite teksto generavimo programą naudodami openai.
- Suprasite, kaip naudoti tokius konceptus kaip užklausa, temperatūra ir žetonai kuriant teksto generavimo programą.

## Mokymosi tikslai

Po šios pamokos jūs galėsite:

- Paaiškinti, kas yra teksto generavimo programa.
- Sukurti teksto generavimo programą naudojant openai.
- Konfigūruoti programą naudoti daugiau ar mažiau žetonų ir keisti temperatūrą, kad gautumėte įvairų rezultatą.

## Kas yra teksto generavimo programa?

Paprastai, kai kuriate programą, ji turi tam tikrą sąsają, pavyzdžiui, tokią:

- Komandų pagrindu. Konsolės programos yra tipinės programos, kuriose įvedate komandą ir ji atlieka užduotį. Pavyzdžiui, `git` yra komandų pagrindo programa.
- Vartotojo sąsają (UI). Kai kurios programos turi grafines vartotojo sąsajas (GUI), kuriose galite spustelėti mygtukus, įvesti tekstą, pasirinkti parinktis ir pan.

### Konsolės ir UI programų ribotumas

Palyginkite tai su komandine programa, kurioje įvedate komandą:

- **Ji yra ribota**. Negalite tiesiog įvesti bet kurios komandos, tik tų, kurias programa palaiko.
- **Kalbos specifinė**. Kai kurios programos palaiko daug kalbų, bet pagal nutylėjimą programa yra sukurta konkrečiai kalbai, net jei galima pridėti daugiau kalbų palaikymo.

### Teksto generavimo programų privalumai

O kaip gi teksto generavimo programa skiriasi?

Teksto generavimo programose turite daugiau lankstumo – nesate apriboti komandų rinkiniu ar konkrečia įvesties kalba. Vietoje to galite naudoti natūralią kalbą, kad bendrautumėte su programa. Kitas privalumas yra tai, kad jau bendraujate su duomenų šaltiniu, kuris buvo apmokytas didžiule informacijos apimtimi, o tradicinė programa gali būti ribojama duomenų bazės turiniu.

### Ką galiu sukurti su teksto generavimo programa?

Galite sukurti daugybę dalykų, pavyzdžiui:

- **Pokalbį vykdantį robotą (chatbot)**. Chatbotas, atsakantis į klausimus apie temas, tokias kaip jūsų įmonė ir jos produktai, galėtų būti puikus pasirinkimas.
- **Pagalbą teikiančią programą**. Dideli kalbos modeliai (LLMs) puikiai tinka užduotims, kaip teksto santraukų darymas, teksto analizė, tekstų, pavyzdžiui, gyvenimo aprašymų, kūrimas ir kt.
- **Kodo pagalbininką**. Priklausomai nuo naudojamo kalbos modelio, galite sukurti kodo pagalbininką, kuris padėtų rašyti kodą. Pavyzdžiui, galite naudoti produktus kaip GitHub Copilot ar ChatGPT kodui rašyti.

## Kaip pradėti?

Jums reikia rasti būdą, kaip integruotis su LLM, kuris paprastai apima šiuos du būdus:

- Naudoti API. Čia jūs sudarote interneto užklausas su savo užklausa ir gaunate sugeneruotą tekstą.
- Naudoti biblioteką. Bibliotekos padeda apjungti API kvietimus ir palengvina jų naudojimą.

## Bibliotekos/SDK

Yra kelios gerai žinomos bibliotekos darbui su LLM, tokios kaip:

- **openai**, ši biblioteka leidžia lengvai prisijungti prie jūsų modelio ir siųsti užklausas.

Taip pat yra bibliotekų, veikiančių aukštesniu lygiu, pavyzdžiui:

- **Langchain**. Langchain yra gerai žinoma ir palaiko Python.
- **Semantic Kernel**. Semantic Kernel yra Microsoft biblioteka, palaikanti kalbas C#, Python ir Java.

## Pirmoji programa naudojant openai

Pažiūrėkime, kaip galime sukurti pirmąją programą, kokių bibliotekų reikia, kiek jos reikalingos ir pan.

### Įdiekite openai

Yra daug bibliotekų, skirtų bendravimui su OpenAI arba Azure OpenAI. Gali būti naudojamos įvairios programavimo kalbos, tokios kaip C#, Python, JavaScript, Java ir kt. Pasirinkome naudoti `openai` Python biblioteką, todėl naudosime `pip` ją įdiegti.

```bash
pip install openai
```

### Sukurkite resursą

Turite atlikti šiuos veiksmus:

- Sukurkite paskyrą Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Gaukite prieigą prie Azure OpenAI. Eikite į [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ir paprašykite prieigos.

  > [!NOTE]
  > Šio teksto rašymo metu turite pateikti prašymą gauti prieigą prie Azure OpenAI.

- Įdiekite Python <https://www.python.org/>
- Sukurkite Azure OpenAI Service resursą. Peržiūrėkite šį vadovą, kaip [sukurti resursą](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Suraskite API raktą ir galutinį tašką

Šiuo metu turite pasakyti savo `openai` bibliotekai, kurį API raktą naudoti. Norėdami rasti API raktą, eikite į „Raktai ir galiniai taškai“ skyrių savo Azure OpenAI resurse ir nukopijuokite „Raktas 1“ reikšmę.

![Raktų ir galinių taškų skydelis Azure portale](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Dabar, kai turite šią informaciją nukopijuotą, nurodykime bibliotekoms ją naudoti.

> [!NOTE]
> Rekomenduojama API raktą atskirti nuo kodo. Tai galite padaryti naudodami aplinkos kintamuosius.
>
> - Nustatykite aplinkos kintamąjį `OPENAI_API_KEY` su savo API raktu.
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

Viršuje nustatome šiuos parametrus:

- `api_key`, tai jūsų API raktas, rastas Azure portale arba Microsoft Foundry portale.
- `base_url`, tai jūsų Foundry resurso galinis taškas su pridėtu `/openai/v1/`. Stabilus v1 galinis taškas veikia tiek su OpenAI, tiek su Azure OpenAI be `api_version` valdymo.

> [!NOTE] > `os.environ` skaito aplinkos kintamuosius. Galite jį naudoti, norėdami nuskaityti aplinkos kintamuosius kaip `AZURE_OPENAI_API_KEY` ir `AZURE_OPENAI_ENDPOINT`. Nustatykite šiuos aplinkos kintamuosius savo terminale ar naudodami biblioteką, pvz., `dotenv`.

## Teksto generavimas

Tekstą generuoti galima naudoti Responses API per `responses.create` metodą. Štai pavyzdys:

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

### Daugiapereiniai pokalbiai

Responses API puikiai tinka tiek vieno užklausos teksto generavimui, tiek daugiapereiniams chatbotams – pateikiate pranešimų sąrašą `input`, kad sukurtumėte pokalbį:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Daugiau apie šią funkciją bus kitame skyriuje.

## Užduotis – jūsų pirmoji teksto generavimo programa

Dabar, kai išmokome nustatyti ir konfigūruoti openai, laikas sukurti savo pirmąją teksto generavimo programą. Štai ko reikia imtis:

1. Sukurkite virtualią aplinką ir įdiekite openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jei naudojate Windows, rašykite `venv\Scripts\activate` vietoje `source venv/bin/activate`.

   > [!NOTE]
   > Suraskite savo Azure OpenAI raktą eidami į [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), raskite `Open AI`, pasirinkite `Open AI resource`, tada pasirinkite `Keys and Endpoint` ir nukopijuokite `Key 1` reikšmę.

1. Sukurkite failą _app.py_ ir įrašykite jame šį kodą:

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
   > Jei naudojate paprastą OpenAI (ne Azure), naudokite `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (be `base_url`) ir perduokite modelio pavadinimą kaip `gpt-5-mini` vietoje diegimo pavadinimo.

   Turėtumėte pamatyti tokį rezultatą:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Skirtingų tipų užklausos – skirtingiems tikslams

Dabar matėte, kaip generuoti tekstą naudojant užklausą. Netgi turite veikiantį programą, kurią galite modifikuoti ir keisti, kad generuotumėte skirtingus tekstus.

Užklausos gali būti naudojamos įvairioms užduotims. Pavyzdžiui:

- **Generuoti tekstų tipą**. Pavyzdžiui, galite sugeneruoti eilėraštį, klausimus viktorinai ir kt.
- **Ieškoti informacijos**. Galite naudoti užklausas informacijai ieškoti, pavyzdžiui, „Ką reiškia CORS interneto kūrime?“.
- **Generuoti kodą**. Galite naudoti užklausas kuriant kodą, pavyzdžiui, kurti reguliarios išraiškos šabloną elektroniniams laiškams tikrinti ar kodą visai programai, pavyzdžiui, žiniatinklio programai.

## Praktinis pavyzdys: receptų generatorius

Įsivaizduokite, kad namuose turite ingredientų ir norite ką nors pagaminti. Tam reikia recepto. Receptų galite ieškoti naudodami paieškos variklį arba pasitelkti LLM.

Galite sukurti tokią užklausą:

> „Pateikite 5 receptus patiekalui su šiais ingredientais: vištiena, bulvės, morkos. Kiekvienam receptui išvardinkite visus ingredientus.“

Gavęs aukščiau pateiktą užklausą, galite gauti panašų atsakymą:

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

Šis rezultatas puikus, žinau, ką gaminti. Šiuo momentu būtų naudinga patobulinimai:

- Filtruoti ingredientus, kurių nemėgstu arba kuriems esu alergiškas.
- Sudaryti pirkinių sąrašą, jei namuose neturiu visų ingredientų.

Tokiu atveju pridėkime papildomą užklausą:

> „Prašau pašalinti receptus su česnaku, nes esu alergiškas, ir pakeisti jį kažkuo kitu. Taip pat sudarykite pirkinių sąrašą receptams, atsižvelgiant į tai, kad namuose jau turiu vištieną, bulves ir morkas.“

Dabar turite naują rezultatą, t. y.:

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

Tai jūsų penki receptai, be česnako ir su pirkinių sąrašu, atsižvelgiant į turimus ingredientus.

## Užduotis – sukurkite receptų generatorių

Dabar, kai apžaidėme scenarijų, parašykime kodą, atitinkantį šį scenarijų. Štai ką daryti:

1. Naudokite esamą _app.py_ failą kaip pradinį tašką
1. Suraskite kintamąjį `prompt` ir pakeiskite jo kodą taip:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jei dabar paleisite kodą, turėtumėte matyti panašų rezultatą:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > PAŽYMA, jūsų LLM nėra determinuotas, todėl kiekvieną kartą paleidus programą gali būti skirtingi rezultatai.

   Puiku, pažiūrėkime, kaip galime patobulinti dalykus. Norėdami tobulinti, norime, kad kodas būtų lankstus, kad būtų galima pakeisti ingredientus ir receptų skaičių.

1. Pakeiskime kodą taip:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Šį kodą išbandyti galėtų atrodyti taip:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Tobulinkite pridėdami filtrą ir pirkinių sąrašą

Dabar turime veikiančią programą, kuri gali generuoti receptus ir yra lanksti, nes remiasi naudotojo pateiktomis įėjimo reikšmėmis – tiek receptų kiekiu, tiek ingredientais.

Norėdami toliau patobulinti, pridėkime šiuos dalykus:

- **Filtruoti ingredientus**. Norime galėti filtruoti ingredientus, kurių nemėgstame arba kuriems esame alergiški. Tam pakeitimui galime redaguoti esamą užklausą ir pridėti filtravimo sąlygą pabaigoje, kaip čia:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Aukščiau pabaigoje užklausos pridėjome `{filter}` ir taip pat surenkame filtro reikšmę iš naudotojo.

  Pavyzdinė programos paleidimo įvestis dabar gali atrodyti taip:

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

  Kaip matote, visi receptai su pienu išfiltruoti. Tačiau jei esate laktozės netolerantas, galbūt norėsite filtruoti ir sūrio turinčius receptus, tad aiškumas yra svarbus.

- **Sukurti pirkinių sąrašą**. Norime sudaryti pirkinių sąrašą atsižvelgiant į tai, ką jau turime namuose.

  Šiai funkcijai galime bandyti išspręsti viską vienoje užklausoje arba padalinti į dvi užklausas. Pabandykime antrą būdą. Čia siūlome pridėti papildomą užklausą, bet tam, kad ji veiktų, turime pridėti pirmos užklausos rezultatą kaip kontekstą antrai užklausoje.

  Suraskite kodo dalį, kuri išveda pirmos užklausos rezultatą, ir po ja pridėkite šį kodą:

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

  1. Kuriame naują užklausą pridėdami pirmos užklausos rezultatą prie naujos užklausos:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Darome naują užklausą, taip pat atsižvelgdamas į žetonų skaičių, kurį prašėme pirmoje užklausoje, todėl šįkart nustatome `max_output_tokens` 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Išbandę šį kodą dabar gauname tokį rezultatą:

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

Tai, ką turime iki šiol, yra veikiantis kodas, tačiau yra keletas patobulinimų, kuriuos turėtume atlikti, kad dar labiau pagerintume situaciją. Kai kurios dalykai, kuriuos turėtume padaryti:

- **Atskirti slaptažodžius nuo kodo**, pavyzdžiui, API raktą. Slaptažodžiai neturi būti įrašyti į kodą ir turėtų būti saugomi saugioje vietoje. Norėdami atskirti slaptažodžius nuo kodo, galime naudoti aplinkos kintamuosius ir tokias bibliotekas kaip `python-dotenv`, kad juos užkrauti iš failo. Štai kaip tai atrodytų kode:

  1. Sukurkite `.env` failą su šiuo turiniu:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Pastaba, Azure OpenAI Microsoft Foundry atveju turite nustatyti šiuos aplinkos kintamuosius vietoj to:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Kode aplinkos kintamuosius užkrautumėte taip:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Žodis apie žetonų ilgį**. Turėtume apsvarstyti, kiek žetonų mums reikia sugeneruoti norimą tekstą. Žetonai kainuoja pinigus, todėl, kur galima, turėtume stengtis taupyti naudojamų žetonų skaičių. Pavyzdžiui, ar galime suformuluoti užklausą taip, kad naudotume mažiau žetonų?

  Norėdami pakeisti naudojamų žetonų skaičių, galite naudoti parametrą `max_output_tokens`. Pavyzdžiui, jei norite naudoti 100 žetonų, darykite taip:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimentavimas su temperatūra**. Temperatūra yra dalykas, apie kurį iki šiol nekalbėjome, bet ji yra svarbus programos veikimo kontekstas. Kuo aukštesnė temperatūros reikšmė, tuo atsitiktinesnis bus rezultatas. Atvirkščiai – kuo žemesnė temperatūra, tuo labiau prognozuojamas bus rezultatas. Apsvarstykite, ar norite variacijų savo rezultate, ar ne.

  Norėdami pakeisti temperatūrą, galite naudoti parametrą `temperature`. Pavyzdžiui, jei norite temperatūrą nustatyti 0.5, darykite taip:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Pastaba, kuo arčiau 1.0, tuo įvairesnis bus rezultatas.

- **Reasoning modeliai nenaudoja `temperature`**. Tai svarbus 2026 metų pokytis. Dabartiniai, nepasenę Microsoft Foundry modeliai yra **reasoning modeliai** (GPT-5 šeima, o-serija) – ir jie **nesupportina `temperature` ar `top_p`** (taip pat ir `max_tokens`; naudokite `max_output_tokens`). Jei siųsite `temperature` į `gpt-5-mini`, gausite klaidą "parametras nepalaikomas". Taigi norėdami išbandyti aukščiau pateiktą temperatūros pavyzdį, pasirinkite modelį, kuris vis dar palaiko sampling valdiklius – pavyzdžiui, atvirą **Llama** modelį `Llama-3.3-70B-Instruct` iš [Microsoft Foundry modelių katalogo](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), kuris kviečiamas per Foundry Models / Azure AI Inference galinį tašką (taip pat kaip `githubmodels-*` pavyzdžiai). Reasoning modeliams, pvz., GPT-5, išvestį kontroliuojame kitaip:
  - **Promptų inžinerija** – aiškios instrukcijos, pavyzdžiai ir struktūrizuotas išvesties formatas (žiūrėkite pamoką [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) atlieka darbą, kurį anksčiau atlikdavo sampling nustatymai.
  - **Reasoning valdikliai** – parametrai, tokie kaip reasoning pastangos/verbališkumas, keičia reasoning gylį pagal delsą ir kainą.

  Apibendrinant: `temperature`/`top_p` vis dar galioja daugelyje modelių (Llama, Mistral, Phi ir GPT-4.x šeimoje – nors GPT-4.x ir nyksta), bet kryptis juda link promptų inžinerijos ir reasoning valdiklių reasoning modeliuose kaip GPT-5.

## Užduotis

Šiai užduočiai galite pasirinkti, ką norite sukurti.

Štai keletas pasiūlymų:

- Patobulinkite receptų generatoriaus programėlę. Eksperimentuokite su temperatūros reikšmėmis ir užklausomis, pažiūrėkite, ką galite sukurti.
- Sukurkite „studijų draugą“. Ši programėlė turėtų gebėti atsakyti į klausimus apie tam tikrą temą, pavyzdžiui, Python. Galite naudoti užklausas, pavyzdžiui, „Kas yra tam tikra tema Python?“, arba paprašyti parodyti kodo pavyzdžių tam tikrai temai.
- Istorijos robotas, padarykite istoriją gyvą, nurodykite robotui vaidinti tam tikrą istorinį veikėją ir užduokite jam klausimų apie jo gyvenimą ir laikmetį.

## Sprendimas

### Studijų draugas

Žemiau pateiktas pradinės užklausos pavyzdys, pažiūrėkite, kaip galite jį naudoti ir pritaikyti pagal savo norą.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Istorijos robotas

Štai keletas užklausų, kurias galite naudoti:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Žinių patikrinimas

Ką daro temperatūros sąvoka?

1. Ji kontroliuoja, kiek atsakymas yra atsitiktinis.
1. Ji kontroliuoja, kokio ilgio yra atsakymas.
1. Ji kontroliuoja, kiek žetonų yra naudojama.

## 🚀 Iššūkis

Dirbdami su užduotimi, pamėginkite keisti temperatūrą, nustatykite ją kaip 0, 0.5 ir 1. Atminkite, kad 0 yra mažiausiai įvairu, o 1 – labiausiai. Kuri reikšmė geriausiai tinka jūsų programėlei?

## Puikus darbas! Tęskite mokymąsi

Užbaigus šią pamoką, peržiūrėkite mūsų [Generatyviosios AI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte žinias apie generatyviąją AI!

Eikite į 7-ąją pamoką, kur aptarsime, kaip [kurti pokalbių programėles](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->