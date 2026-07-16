# Tekstigeneratsiooni rakenduste loomine

[![Tekstigeneratsiooni rakenduste loomine](../../../translated_images/et/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klõpsake ülaloleval pildil, et vaadata selle tunni videot)_

Sa oled selle õppekava jooksul näinud, et on olemas põhikontseptsioonid nagu promptid ja isegi terve distsipliin nimega "prompti inseneritöö". Paljud tööriistad, millega saad suhelda, nagu ChatGPT, Office 365, Microsoft Power Platform ja teised, toetavad sind promptide kasutamisel mingi ülesande täitmiseks.

Selleks, et lisada selline kogemus rakendusse, pead sa mõistma selliseid mõisteid nagu prompt, täitmised ja valima sobiva teegi, millega töötada. Just seda sa selles peatükis õpid.

## Sissejuhatus

Selles peatükis sa:

- Õpid tundma openai teeki ja selle põhikontseptsioone.
- Ehita tekstigeneratsiooni rakendus openai abil.
- Mõistad, kuidas kasutada selliseid mõisteid nagu prompt, temperatuur ja tokenid, et ehitada tekstigeneratsiooni rakendus.

## Õpieesmärgid

Selle tunni lõpetamisel oskad sa:

- Selgitada, mis on tekstigeneratsiooni rakendus.
- Ehita tekstigeneratsiooni rakendus openai abil.
- Konfigureerida oma rakendust nii, et kasutatakse rohkem või vähem tokeneid ja muuta ka temperatuuri, et saada varieeruvat väljundit.

## Mis on tekstigeneratsiooni rakendus?

Tavaliselt, kui ehitad rakendust, on sellel mingi kasutajaliides, mis võib olla näiteks:

- Käskluspõhine. Konsoolirakendused on tüüpilised rakendused, kus sa kirjutad käsu ja see täidab ülesande. Näiteks `git` on käskluspõhine rakendus.
- Kasutajaliides (UI). Mõnel rakendusel on graafiline kasutajaliides (GUI), kus sa klõpsad nuppe, sisestad teksti, valid valikuid ja muud.

### Konsooli- ja kasutajaliideserakendused on piiratud

Võrrelge seda käskluspõhise rakendusega, kus sa kirjutad käsu:

- **See on piiratud**. Sa ei saa lihtsalt kirjutada suvalist käsku, vaid ainult neid, mida rakendus toetab.
- **Keelepõhine**. Mõned rakendused toetavad mitut keelt, kuid vaikimisi on rakendus loodud konkreetse keele jaoks, isegi kui saad lisada rohkem keelte tuge.

### Tekstigeneratsiooni rakenduste eelised

Kuidas on tekstigeneratsiooni rakendus teistmoodi?

Tekstigeneratsiooni rakenduses on sul rohkem paindlikkust, sa ei ole piiratud etteantud käskude komplektiga ega kindla sisendkeelega. Selle asemel saad kasutada loomulikku keelt rakendusega suhtlemiseks. Teine eelis on see, et sa suhtled juba andmeallikaga, mis on väljaõpetatud suurel hulgal teavet, samas kui traditsiooniline rakendus võib olla piiratud andmebaasis oleva teabega.

### Mida ma saan tekstigeneratsiooni rakendusega ehitada?

Võid ehitada väga erinevaid asju. Näiteks:

- **Vestlusrobot**. Vestlusrobot, mis vastab küsimustele teemadel nagu sinu ettevõte ja selle tooted, võiks olla väga sobiv.
- **Abiline**. Suured keelemudelid (LLM) on suurepärased tekstide kokkuvõtmisel, tekstist info saamisel, tekstide loomisel nagu CV-d ja palju muud.
- **Koodi assistent**. Sõltuvalt kasutatavast keelemudelist saad ehitada koodi assistendi, mis aitab sul koodi kirjutada. Näiteks võid kasutada toodet nagu GitHub Copilot ja samuti ChatGPT oma koodi kirjutamise abistamiseks.

## Kuidas alustada?

Pead leidma viisi, kuidas integreeruda LLM-iga, mis tavaliselt tähendab kahte lähenemist:

- Kasutada API-t. Siin koostad veebipäringuid oma promptidega ja saad tagasi genereeritud teksti.
- Kasutada teeki. Teegid aitavad kapseldada API kõnesid ja muudavad nende kasutamise lihtsamaks.

## Teegid/SDK-d

On mõned tuntud teegid LLM-idega töötamiseks nagu:

- **openai**, see teek teeb lihtsaks mudeliga ühenduse loomise ja promptide edastamise.

Siis on teegid, mis toimivad kõrgemal tasemel nagu:

- **Langchain**. Langchain on tuntud ja toetab Pythoni.
- **Semantic Kernel**. Semantic Kernel on Microsofti teek, mis toetab keeli C#, Python ja Java.

## Esimene rakendus openai kasutades

Vaatame, kuidas saame ehitada oma esimese rakenduse, milliseid teeke vajame, kui palju on vaja ja nii edasi.

### Paigalda openai

On palju teeke OpenAI või Azure OpenAI-ga suhtlemiseks. Võid kasutada ka mitmeid programmeerimiskeeli nagu C#, Python, JavaScript, Java ja teised. Me valisime kasutada `openai` Pythoni teeki, nii et paigaldame selle `pip` abil.

```bash
pip install openai
```

### Loo ressurss

Pead tegema järgnevad sammud:

- Loo konto Azure'is [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Hangi ligipääs Azure OpenAI-le. Mine lehele [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ja taotle ligipääsu.

  > [!NOTE]
  > Kirjutamise ajal pead taotlema ligipääsu Azure OpenAI-le.

- Paigalda Python <https://www.python.org/>
- Loo Azure OpenAI teenuse ressurss. Vaata juhendit, kuidas [luua ressurssi](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Leia API võti ja lõpp-punkt

Nüüd pead ütlema oma `openai` teegile, millist API võtit kasutada. Oma API võtme leidmiseks mine oma Azure OpenAI ressursi jaotisse "Keys and Endpoint" ning kopeeri sealt "Key 1" väärtus.

![Võtmed ja lõpp-punkt Azure portaalis](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nüüd, kui sul on need andmed kopeeritud, juhime teegid nende kasutamiseks.

> [!NOTE]
> On soovitatav hoida API võti koodist eraldi. Seda saab teha keskkonnamuutujate abil.
>
> - Sea keskkonnamuutujaks `OPENAI_API_KEY` oma API võtme väärtus.
>   `export OPENAI_API_KEY='sk-...'`

### Seadista konfiguratsioon Azure'is

Kui kasutad Azure OpenAI-d (nüüd Microsoft Foundry osa), siis nii seadistad konfiguratsiooni. Kasutame tavalist `OpenAI` klienti, mis on suunatud Azure OpenAI `/openai/v1/` lõpp-punktile, mis töötab Responses API-ga ega vaja `api_version`-it:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Ülal seadistame järgmised asjad:

- `api_key`, see on sinu Azure portaali või Microsoft Foundry portaali API võti.
- `base_url`, see on sinu Foundry ressursi lõpp-punkt, mille lõppu on lisatud `/openai/v1/`. Stabiilne v1 lõpp-punkt toimib nii OpenAI kui Azure OpenAI puhul ilma `api_version` halduseta.

> [!NOTE] > `os.environ` loeb keskkonnamuutujaid. Seda saab kasutada selliste keskkonnamuutujate lugemiseks nagu `AZURE_OPENAI_API_KEY` ja `AZURE_OPENAI_ENDPOINT`. Määra need keskkonnamuutujad oma terminalis või kasuta teeki nagu `dotenv`.

## Teksti genereerimine

Teksti genereerimiseks kasutatakse Responses API-d meetodi `responses.create` kaudu. Näide:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # see on teie mudeli kasutuselevõtu nimi
    input=prompt,
    store=False,
)
print(response.output_text)
```

Ülaltoodud koodis loome vastuse, edastame kasutatava mudeli ja prompti. Siis trükime genereeritud teksti `response.output_text` kaudu.

### Mitmevoorulised vestlused

Responses API sobib nii ühevooruliseks tekstigeneratsiooniks kui ka mitmevoorulisteks vestlusrobotiteks - sa annad sõnumite nimekirja `input`-ina, et vestlust üles ehitada:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Selle funktsionaalsuse kohta tuleb rohkem peatükis.

## Harjutus - sinu esimene tekstigeneratsiooni rakendus

Nüüd, kui me õppisime, kuidas openai seadistada ja konfigureerida, on aeg ehitada oma esimene tekstigeneratsiooni rakendus. Selleks tee järgmist:

1. Loo virtuaalne keskkond ja paigalda openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Kui kasutad Windowsi, kirjuta `venv\Scripts\activate` asemel `source venv/bin/activate`.

   > [!NOTE]
   > Leia oma Azure OpenAI võti, minnes lehele [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ja otsi `Open AI`, vali `Open AI resource` ja siis vali `Keys and Endpoint` ning kopeeri `Key 1` väärtus.

1. Loo _app.py_ fail ja kirjuta sinna järgmine kood:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # lisa oma lõpetamiskood
   prompt = "Complete the following: Once upon a time there was a"

   # tee päring kasutades Responses API-d
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # prindi vastus
   print(response.output_text)
   ```

   > [!NOTE]
   > Kui kasutad tavalist OpenAI-d (mitte Azure), kasuta `client = OpenAI(api_key="<asenda see oma OpenAI võtmega>")` (ilma `base_url`ita) ja edasta mudeli nimeks näiteks `gpt-4o-mini` deploy'nime asemel.

   Sa peaksid nägema väljastust, mis on järgmine:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Erinevat tüüpi promptid erinevateks asjadeks

Nüüd, kui oled näinud, kuidas teksti genereerida prompti abil. Sul on isegi programm käivitatud ja valmis, mida saad muuta, et genereerida erinevat tüüpi tekste.

Prompte võib kasutada igasugusteks ülesanneteks. Näiteks:

- **Teksti genereerimine**. Näiteks võid genereerida luuletuse, viktoriiniküsimusi jms.
- **Info otsimine**. Sa võid kasutada promte info otsimiseks nagu näiteks "Mida tähendab CORS veebiarenduses?".
- **Koodi genereerimine**. Võid kasutada promte koodi genereerimiseks, näiteks regulaarexpressioni tegemiseks, et valideerida e-kirju või miks mitte genereerida terve programm, näiteks veebirakendus?

## Praktilisem kasutusjuht: retseptide generaator

Kujuta ette, et sul on kodus koostisosad ja tahad midagi kokata. Selleks vajad retsepti. Retseptide leidmiseks võid kasutada otsingumootorit või kasutada LLM-i.

Sa võiksid kirjutada sellise prompti:

> "Näita mulle 5 retsepti roale järgnevate koostisosadega: kana, kartulid ja porgandid. Koostisosade lõikes loetle iga retsepti puhul kõik kasutatud koostisosad."

Selle prompdi põhjal võid saada vastuse sarnane järgmisele:

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

See tulemus on suurepärane, ma tean, mida kokata. Selles punktis võiks kasulikud täiustused olla:

- Koostisosade filtreerimine, mida ma ei salli või mille suhtes olen allergiline.
- Ostunimekirja koostamine juhuks, kui mul kõiki koostisosi kodus ei ole.

Ülaltoodud juhtude jaoks lisame täiendava prompti:

> "Palun eemalda retseptidest küüslauk, sest olen allergiline, ja asenda see millegi muuga. Samuti palun tee ostunimekiri retseptide jaoks, arvestades, et mul on juba kodus kana, kartulid ja porgandid."

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

Need on sinu viis retsepti, milles pole mainitud küüslauku ja sul on ka ostunimekiri, arvestades seda, mis sul juba kodus on.

## Harjutus - ehita retseptide generaator

Nüüd, kui me oleme stsenaariumi läbi mänginud, kirjutame koodi, mis vastab demonstreeritud stsenaariumile. Selleks tee järgmist:

1. Kasuta olemasolevat _app.py_ faili lähtepunktina
1. Leia muutuja `prompt` ja muuda selle koodi järgmiseks:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Kui sa nüüd koodi jooksutad, peaks ehk sarnane väljund olema:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > MÄRKUS, sinu LLM on mittedeterministlik, seega võid saada igal käivitamisel erinevaid tulemusi.

   Suurepärane, vaatame, kuidas saame asju parandada. Parandamiseks tahame tagada, et kood oleks paindlik, nii et koostisosad ja retseptide arv oleks hõlpsasti muudetavad.

1. Muudame koodi järgmiselt:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpoleeri retseptide arv prompti ja koostisosadesse
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testkäivituse jaoks võiks kood välja näha selline:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Paranda lisades filter ja ostunimekiri

Nüüd on meil toimiv rakendus, mis suudab genereerida retsepte ja on paindlik, sest see sõltub kasutaja sisenditest, nii retseptide arvu kui ka koostisosade kohta.

Veel parendamiseks tahame lisada järgmise:

- **Filtreeri koostisosad välja**. Tahame võimaldada koostisosade väljasõelumist, mida me ei soovi või mille suhtes oleme allergilised. Selleks muudatuseks saame oma olemasoleva prompti lõppu lisada filtertingimuse nii:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ülal lisame prompti lõppu `{filter}` ja võtame ka kasutajalt filtri väärtuse.

  Näiteks võib programmi sisend välja näha järgmiselt:

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

  Nagu näha, on kõik retseptid, kus on piim, välja filtreeritud. Kuid kui sul on laktoositalumatus, sooviksid ehk filtreerida ka juustu sisaldavad retseptid, seega tuleb olla täpne.


- **Koosta ostunimekiri**. Tahame koostada ostunimekirja, arvestades seda, mis meil kodus juba olemas on.

  Selle funktsionaalsuse jaoks võiksime proovida lahendada kõik ühe promptiga või jagada see kaheks promptiks. Proovime viimast lähenemist. Siin soovitame lisada täiendava prompti, kuid selleks, et see toimiks, peame esimese prompti tulemuse lisama teise prompti kontekstiks.

  Leia koodist osa, mis prindib välja esimese prompti tulemuse, ja lisa alljärgnev kood sellele alla:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # kuva vastus
  print("Shopping list:")
  print(response.output_text)
  ```

  Pane tähele järgmist:

  1. Koostame uue prompti, lisades esimese prompti tulemuse uude prompti:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Teeme uue päringu, võttes arvesse ka esimese prompti korral küsitud tokenite arvu, seega seekord määrame `max_output_tokens` väärtuseks 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Kui seda koodi proovile panna, saame järgmise väljundi:

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

Seni on meil toimiv kood, kuid mõned täiendused võiksid asja veelgi paremaks muuta. Mõned asjad, mida peaksime tegema:

- **Eralda saladused koodist**, näiteks API võti. Saladused ei kuulu koodi ning neid tuleks hoida turvalises kohas. Saladuste eraldamiseks koodist võime kasutada keskkonnamuutujaid ja teeke nagu `python-dotenv`, et laadida need failist. Koodis näeks see välja järgmiselt:

  1. Loo `.env` fail järgmise sisuga:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Märkus, Azure OpenAI Microsoft Foundry jaoks tuleb määrata hoopis järgmised keskkonnamuutujad:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Koodis laadiksid keskkonnamuutujad selliselt:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Sõna tokenite pikkusest**. Me peaksime arvestama, kui palju tokeneid vajame soovitud teksti genereerimiseks. Tokenid maksavad raha, seega tuleb võimalusel kasutada tokeneid säästlikult. Näiteks — kas saaksime prompti sõnastada nii, et kasutaksime vähem tokeneid?

  Tokenite arvu muutmiseks saab kasutada `max_output_tokens` parameetrit. Näiteks kui soovid kasutada 100 tokenit, teeksid nii:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Katsetamine temperatuuriga**. Temperatuur on asi, millest me siiani pole rääkinud, kuid see on oluline kontekst programmi töö mõistmiseks. Mida kõrgem on temperatuuri väärtus, seda juhuslikum on väljund. Mida madalam temperatuuri väärtus, seda ennustatavam on väljund. Mõtle, kas soovid väljundis varieeruvust või mitte.

  Temperatuuri muutmiseks saab kasutada `temperature` parameetrit. Näiteks kui soovid kasutada temperatuuri 0.5, teeksid nii:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Märkus, mida lähemal 1.0-le, seda varieeruvam on väljund.

## Ülesanne

Selle ülesande puhul võid valida, mida ehitada.

Siin on mõned soovitused:

- Paranda veelgi retsepigeneraatori rakendust. Mängi temperatuuri väärtustega ja promptidega, et vaadata, mida suudad luua.
- Ehita "õpimitt". See rakendus peaks suutma vastata küsimustele teema kohta, näiteks Python; võid lisada promptid nagu "Mis on kindel teema Pythonis?", või prompti, mis ütleb: näita mulle koodi kindla teema kohta jne.
- Ajaloo-bot, too ajalugu ellu, käsu botil mängida kindlat ajaloolist tegelast ja ära temalt küsimusi tema elu ja ajastu kohta.

## Lahendus

### Õpimitt

Allpool on stardiprompt, vaata, kuidas sa saad seda kasutada ja oma äranägemise järgi kohandada.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Ajaloo-bot

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

Ülesande juures proovi varieerida temperatuuri, seadistades selle väärtusteks 0, 0.5 ja 1. Pea meeles, et 0 on kõige vähem varieeruv ja 1 kõige rohkem. Milline väärtus sobib su rakendusele kõige paremini?

## Tubli töö! Jätka õppimist

Pärast selle õppetüki lõpetamist vaata meie [Generatiivse tehisintellekti õppe kogumikku](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma Generatiivse tehisintellekti teadmiste taseme tõstmist!

Mine edasi õppetüki 7 juurde, kus vaatleme, kuidas [ehitada vestlusrakendusi](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->