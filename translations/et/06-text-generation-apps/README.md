# Teksti genereerimise rakenduste loomine

[![Teksti genereerimise rakenduste loomine](../../../translated_images/et/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klõpsa ülaloleval pildil, et vaadata selle õppetunni videot)_

Selle õppekava jooksul oled juba näinud, et on põhimõisted nagu promptid ja isegi kogu valdkond nimega „promptide inseneriteadus“. Paljud tööriistad, millega saad suhelda, nagu ChatGPT, Office 365, Microsoft Power Platform ja teised, toetavad sind promptide kasutamisel millegi saavutamiseks.

Et lisada selline kogemus rakendusse, pead mõistma mõisteid nagu promptid, täiendused ja valima, millist teeki kasutada. Just seda sa selles peatükis õpid.

## Sissejuhatus

Selles peatükis sa:

- Õpid openai teegi ja selle põhimõistete kohta.
- Ehitad teksti genereerimise rakenduse kasutades openai.
- Mõistad, kuidas kasutada mõisteid nagu prompt, temperatuur ja tokenid, et ehitada teksti genereerimise rakendus.

## Õpieesmärgid

Selle õppetunni lõpus saad:

- Selgitada, mis on teksti genereerimise rakendus.
- Ehita teksti genereerimise rakendus kasutades openai.
- Konfigureeri oma rakendust kasutama rohkem või vähem tokeneid ja muuda ka temperatuuri erineva väljundi saamiseks.

## Mis on teksti genereerimise rakendus?

Tavaliselt, kui ehitad rakendust, on sellel mingi kasutajaliides nagu alljärgnev:

- Käskluspõhine. Konsoolirakendused on tüüpilised rakendused, kus kirjutad käsu ja see täidab ülesande. Näiteks on `git` käskluspõhine rakendus.
- Kasutajaliides (UI). Mõnel rakendusel on graafilised kasutajaliidesed (GUI), kus klikid nuppe, sisestad teksti, valid valikuid ja muud.

### Konsooli- ja kasutajaliidese rakendused on piiratud

Võrdle seda käsuga põhineva rakendusega, kus kirjutad käsu:

- **See on piiratud**. Sa ei saa lihtsalt kirjutada mõnda suvalist käsku, vaid ainult neid, mida rakendus toetab.
- **Keelepõhine**. Mõned rakendused toetavad mitut keelt, kuid vaikimisi on rakendus loodud konkreetse keele jaoks, isegi kui saad lisada rohkem keeletoe.

### Teksti genereerimise rakenduste eelised

Kuidas on aga teksti genereerimise rakendus eriline?

Teksti genereerimise rakenduses on sul rohkem paindlikkust, sa ei ole piiratud kindla käskude komplekti ega konkreetse sisendkelega. Selle asemel saad kasutada loomulikku keelt, et suhelda rakendusega. Teine eelis on see, et sa juba suhtled andmeallikaga, mis on treenitud tohutu hulga info peal, samas kui traditsiooniline rakendus võib olla piiratud sellega, mis andmebaasis on.

### Mida saan ehitada teksti genereerimise rakendusega?

On palju asju, mida võid ehitada. Näiteks:

- **Vestlusrobot**. Vestlusrobot, mis vastab küsimustele teemadel nagu sinu ettevõte ja selle tooted, võiks olla sobiv.
- **Abi**. LLM-id on suurepärased asjade nagu teksti kokkuvõtete tegemisel, tekstist arusaamade saamisel, tekstide tootmisel nagu CV-d ja muud.
- **Koodi assistent**. Sõltuvalt kasutatavast keelemudelist saad ehitada koodi assistendi, mis aitab sul koodi kirjutada. Näiteks võid kasutada toodet nagu GitHub Copilot või ChatGPT, mis aitavad sul koodi kirjutada.

## Kuidas alustada?

Sa pead leidma viisi LLMiga integreerimiseks, mis tavaliselt tähendab kahte lähenemist:

- Kasutada API-d. Siin ehitad veebipäringud oma promptiga ja saad tagasi genereeritud teksti.
- Kasutada teeki. Teegid aitavad kapseldada API kõnesid ja teevad nende kasutamise lihtsamaks.

## Teegid/SDK-d

On mõningaid hästi tuntud teeke LLMidega töötamiseks, näiteks:

- **openai**, see teek teeb lihtsaks oma mudeliga ühenduse loomise ja promptide saatmise.

Siis on ka kõrgema taseme teegid, näiteks:

- **Langchain**. Langchain on hästi tuntud ja toetab Pythoni.
- **Semantic Kernel**. Semantic Kernel on Microsofti teek, mis toetab keeli C#, Python ja Java.

## Esimene rakendus kasutades openai

Vaatame, kuidas ehitada oma esimene rakendus, milliseid teeke vajame, kui palju on vajalik ja nii edasi.

### Paigalda openai

On palju teeke OpenAI või Azure OpenAI-ga suhtlemiseks. Võid kasutada mitmeid programmeerimiskeeli nagu C#, Python, JavaScript, Java ja teisi. Me valisime kasutada `openai` Pythoni teeki, nii et kasutame `pip` selle installimiseks.

```bash
pip install openai
```

### Loo ressurss

Pead tegema järgmised sammud:

- Loo konto Azure'is [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)].
- Saa ligipääs Azure OpenAI-le. Mine [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst)] ja taotle ligipääsu.

  > [!NOTE]
  > Kirjutamise ajal pead taotlema ligipääsu Azure OpenAI-le.

- Paigalda Python <https://www.python.org/>.
- Loo Azure OpenAI Service ressurss. Vaata juhendit, kuidas [luua ressurss](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Leia API võti ja lõpp-punkt

Nüüd pead ütlema oma `openai` teegile, millist API võtit kasutada. Oma API võtme leidmiseks mine oma Azure OpenAI ressursi sektsiooni "Keys and Endpoint" ja kopeeri sealt „Key 1“ väärtus.

![Võtmete ja lõpp-punkti paneel Azure portaalis](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Kui sul on see info kopeeritud, juhendame teeke selle kasutamiseks.

> [!NOTE]
> Väärt on hoida oma API võti eraldi oma koodist. Seda saab teha kasutades keskkonnamuutujaid.
>
> - Sea keskkonnamuutuja `OPENAI_API_KEY` oma API võtmele.
>   `export OPENAI_API_KEY='sk-...'`

### Azure konfiguratsiooni seadistamine

Kui kasutad Azure OpenAI (nüüd osa Microsoft Foundry'st), siis nii seadistad konfiguratsiooni. Kasutame standardset `OpenAI` klienti, mis osutab Azure OpenAI `/openai/v1/` lõpp-punktile, see töötab Responses API-ga ja ei vaja `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Ülal seadistame järgmist:

- `api_key` — see on su API võti, mille leiad Azure portaalist või Microsoft Foundry portaalist.
- `base_url` — see on sinu Foundry ressursi lõpp-punkt, kuhu on lisatud `/openai/v1/`. Stabiilne v1 lõpp-punkt töötab nii OpenAI kui Azure OpenAI-ga ilma `api_version` halduseta.

> [!NOTE] > `os.environ` loeb keskkonnamuutujaid. Võid seda kasutada keskkonnamuutujate nagu `AZURE_OPENAI_API_KEY` ja `AZURE_OPENAI_ENDPOINT` lugemiseks. Sea need keskkonnamuutujad oma terminalis või kasuta teeki nagu `dotenv`.

## Teksti genereerimine

Teksti genereerimiseks kasuta Responses API-d meetodi `responses.create` kaudu. Näide:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Ülaltoodud koodis loome vastuse ja anname mudeli, mida soovime kasutada, ja prompti. Seejärel prindime genereeritud teksti meetodi `response.output_text` kaudu.

### Mitme-kaarega vestlused

Responses API sobib hästi nii ühekordseks teksti genereerimiseks kui ka mitme kaarega vestlusrobotite jaoks — sa annad sõnumite nimekirja `input`, et üles ehitada vestlust:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Selle funktsionaalsuse kohta tuleb lähemalt järgmises peatükis.

## Harjutus - sinu esimene teksti genereerimise rakendus

Kui nüüd oskate openai seadistada ja konfigureerida, on aeg ehitada oma esimene teksti genereerimise rakendus. Rakenduse loomisel järgi neid samme:

1. Loo virtuaalne keskkond ja paigalda openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Kui kasutad Windowsi, kirjuta `venv\Scripts\activate` asemel `source venv/bin/activate`.

   > [!NOTE]
   > Leia oma Azure OpenAI võti, minnes [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst)], otsides `Open AI`, vali `Open AI resource`, seejärel vali `Keys and Endpoint` ja kopeeri `Key 1` väärtus.

1. Loo _app.py_ fail ja pane sinna järgmine kood:

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
   > Kui kasutad tavapärast OpenAI-d (mitte Azure), kasuta `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (ilma `base_url`) ja anna mudeli nimi nagu `gpt-5-mini` asemel juurutusnimele.

   Pead nägema midagi sellist:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Erinevad promptide tüübid erinevate ülesannete jaoks

Nüüd oled näinud, kuidas teksti genereerida prompti abil. Sul on ka programm, mis töötab ja mida saab muuta, et genereerida erinevat tüüpi teksti.

Prompte saab kasutada igasugusteks ülesanneteks. Näiteks:

- **Genereeri mingi teksti tüüp**. Näiteks saad genereerida luuletust, viktoriiniküsimusi jms.
- **Otsi infot**. Saad kasutada prompti info otsimiseks, nt „Mida tähendab CORS veebiarenduses?“.
- **Genereeri koodi**. Prompte saab kasutada koodi genereerimiseks, näiteks regulaarekspriimi loomisel e-kirjade valideerimiseks või miks mitte terve programmi, näiteks veebiäpi genereerimiseks?

## Praktilisem näide: retseptigeneraator

Kujuta ette, et sul on kodus koostisosad ja tahad süüa teha. Selleks vajad retsepti. Retseptide leidmiseks võid kasutada otsingumootorit või siis LLM-i.

Sa võiksid kirjutada prompti näiteks nii:

> "Näita mulle 5 retsepti roale, milles on järgmised koostisosad: kana, kartul ja porgand. Iga retsepti kohta loetle kõik kasutatud koostisosad."

Selle prompti peale võid saada vastuse, mis on sarnane:

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

See tulemus on hea, ma tean, mida süüa teha. Sellisel juhul võiks kasulik olla:

- Filtreerida välja koostisosad, mida ma ei salli või millele olen allergiline.
- Luua ostunimekiri juhuks, kui mul ei ole kõiki koostisosi kodus.

Selliste juhtumite jaoks lisame oma prompti lisaks:

> "Palun eemalda retseptidest küüslauk, sest olen sellele allergiline, ja asenda see millegagi muuga. Samuti palun koostada ostunimekiri retseptide jaoks, arvestades, et mul on juba kodus kana, kartul ja porgand."

Nüüd on sul uus tulemus, nimelt:

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

Need on sinu viis retsepti, kus pole küüslauku ja sul on ka arvestatud ostunimekiri selle põhjal, mis sul juba kodus olemas on.

## Harjutus - ehita retseptigeneraator

Nüüd, kus mängisime läbi stsenaariumi, kirjutame selle stsenaariumi jaoks sobiva koodi. Tee nii:

1. Kasuta olemasolevat _app.py_ faili lähtepunktina
1. Leia muutujat `prompt` ja muuda selle koodi järgmiseks:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Kui nüüd koodi jooksutad, peaksid nägema midagi sarnast:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > PANGE TÄHELE, su LLM on mittetäielikult deterministlik, nii et võid saada iga kord erinevaid tulemusi, kui programmi jooksutad.

   Väga hea, vaatame, kuidas asju parandada. Et asju parandada, tahame, et kood oleks paindlik, nii et nii koostisosad kui retseptide arv on kergesti muudetavad ja täiustatavad.

1. Muudame koodi nii:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Koodi testimiseks võiks see välja näha nii:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Paranda, lisades filtri ja ostunimekirja

Nüüd on meil töötav rakendus, mis suudab genereerida retsepte ja on paindlik, kuna võtab kasutajalt nii retseptide arvu kui kasutatavate koostisosade sisendi.

Et seda veelgi parendada, tahame lisada järgmist:

- **Filtreeri välja koostisosad**. Tahame saada võimaluse filtreerida välja koostisosad, mida me ei salli või millele oleme allergilised. Selleks võime muuta oma olemasolevat prompti ning lisada selle lõppu filtri tingimuse näiteks nii:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ülal lisame prompti lõppu `{filter}` ning samuti võtame kasutajalt filtri väärtuse.

  Näide programmi jooksutamisest võib nüüd olla järgmine:

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

  Nagu näha, on kõik retseptid, mis sisaldasid piima, välja filtreeritud. Kui oled laktoosi talumatu, võid samuti soovida välja filtreerida retseptid, mis sisaldavad juustu, seega on vajadus olla täpne.

- **Genereeri ostunimekiri**. Tahame genereerida ostunimekirja, arvestades, mis meil juba kodus olemas on.

  Selle funktsionaalsuse jaoks võiks proovida kas lahendada kõik ühe promptiga või jagada see kaheks promptiks. Proovime teist varianti. Sellisel juhul lisame eelneva prompti tulemuse järgmise prompti kontekstiks.

  Leia koodist koht, kus prinditakse välja esimese prompti tulemus ja lisa sinna järgmine koodiosa:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Pane tähele järgmist:

  1. Koostame uue prompti, lisades sellele esimese prompti tulemuse:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Teeme uue päringu, kuid arvestades, et esimese prompti puhul palusime x tokeneid, siis nüüd kasutame `max_output_tokens` väärtust 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Kui selle koodi ikka jooksutame, saame järgmise väljundi:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Paranda oma seadistust

Seni on meil olemas töötav kood, kuid on mõned kohandused, mida peaksime tegema, et asju veelgi parandada. Mõned asjad, mida peaksime tegema, on:

- **Eralda saladused koodist**, näiteks API võti. Saladused ei kuulu koodi ja need tuleks hoida turvalises kohas. Saladuste eraldamiseks koodist saame kasutada keskkonnamuutujaid ja selliseid teeke nagu `python-dotenv`, et laadida neid failist. Koodis näeks see välja järgmiselt:

  1. Loo `.env` fail järgmise sisuga:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Märkus, Azure OpenAI kasutamisel Microsoft Foundrys tuleb selle asemel seada järgmised keskkonnamuutujad:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Koodis laadiksid keskkonnamuutujad järgmiselt:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Sõna tokeni pikkusest**. Me peaksime kaaluma, kui palju tokeneid on vaja, et genereerida soovitud tekst. Tokenite kasutamine maksab raha, seega peaksime võimalikult palju püüdma olla säästlik tokenite arvuga. Näiteks, kas saame prompti nii sõnastada, et kasutada vähem tokeneid?

  Tokeneid kasutamise muutmiseks võid kasutada parameetrit `max_output_tokens`. Näiteks, kui soovid kasutada 100 tokenit, teeksid umbes nii:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Katsetamine temperatuuriga**. Temperatuur on midagi, millest seni pole räägitud, aga see on oluline kontekst, kuidas meie programm töötab. Mida kõrgem temperatuurit väärtus, seda juhuslikum on väljund. Vastupidi, madalam temperatuurit väärtus teeb väljundi ennustatavamaks. Mõtle, kas soovid väljundis varieeruvust või mitte.

  Temperatuuri muutmiseks võid kasutada parameetrit `temperature`. Näiteks, kui soovid kasutada temperatuuri 0.5, teeksid umbes nii:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Märkus, mida lähemal väärtus on 1.0-le, seda varieeruvam on väljund.

- **Järeldus: reasoningu mudelid ei kasuta `temperature`**. See on oluline 2026. aasta nihe. Praegused, Microsoft Foundry mitte-vananenud mudelid on **reasoningu mudelid** (GPT-5 seeria, o-seeria) - ja need **ei toeta `temperature` ega `top_p`** (ega ka `max_tokens`; kasuta `max_output_tokens`). Kui saadad `temperature` aadressile `gpt-5-mini`, saad "parameeter ei ole toetatud" vea. Nii et temperatuuri näite proovimiseks suuna see mudelile, mis toetab endiselt valikukontrolle - näiteks avatud **Llama** mudel nagu `Llama-3.3-70B-Instruct` Microsoft Foundry mudelite kataloogist [Microsoft Foundry mudelite kataloog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), kutsutakse Foundry Models / Azure AI Inference lõpp-punkti kaudu (nagu ka `githubmodels-*` näidised). GPT-5 tüüpi reasoningu mudelite puhul juhid väljundit teisiti:
  - **Prompti inseneritöö** - selged juhised, näited ja struktureeritud väljund (loe lähemalt [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) teevad seda tööd, mida varem tegid valikukangid.
  - **Reasoningu kontrollid** - sellised parameetrid nagu reasoningu pingutus/ sõnaküllus vahetavad reasoningu sügavust latentsuse ja kulu vastu.

  Lühidalt: `temperature`/`top_p` on endiselt kehtivad paljudel mudelitel (Llama, Mistral, Phi ja GPT-4.x seeria - kuigi GPT-4.x on vananemas), kuid tulevikusuunaks on prompti inseneritöö + reasoningu kontrollid reasoningu mudelitel nagu GPT-5.

## Ülesanne

Selle ülesande puhul võid valida, mida ehitada.

Siin on mõned soovitused:

- Paranda veelgi retseptide genereerimise rakendust. Katseta temperatuuri väärtustega ja promptidega, et näha, mida saad luua.
- Ehita "õppimise kaaslane". Sellel rakendusel peaks olema võime vastata küsimustele teatud teema kohta, näiteks Python; võid kasutada promptina “Mis on mingi teema Pythonis?” või prompti, mis ütleb, näita mulle koodi mingi teema kohta jne.
- Ajaloo-bot, too ajalugu ellu, käsu botil mängida mõnd ajaloolist tegelast ja esita talle küsimusi selle elu ja aja kohta.

## Lahendus

### Õppimise kaaslane

Allpool on algne prompt, vaata, kuidas saad seda kasutada ja oma maitse järgi kohandada.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Ajaloo bot

Siin on mõned promptid, mida võid kasutada:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Teadmiste kontroll

Mida teeb mõiste temperatuur?

1. See kontrollib, kui juhuslik väljund on.
1. See kontrollib, kui suur vastus on.
1. See kontrollib, kui palju tokeneid kasutatakse.

## 🚀 Väljakutse

Töötades ülesandega, proovi varieerida temperatuuri, proovi seada see väärtustele 0, 0.5 ja 1. Pea meeles, et 0 on kõige vähem varieeruv ja 1 kõige rohkem. Milline väärtus töötab su rakendusele kõige paremini?

## Hea töö! Jätka õppimist

Pärast selle tunni lõpetamist vaata meie [Geneeriva tehisintellekti õppekogumit](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma geneeriva AI teadmiste taseme tõstmist!

Liigu edasi 7. õppetunni juurde, kus uurime, kuidas [ehitada vestlusrakendusi](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->