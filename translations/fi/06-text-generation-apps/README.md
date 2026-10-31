# Tekstintuottosovellusten rakentaminen

[![Tekstintuottosovellusten rakentaminen](../../../translated_images/fi/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Olet nähnyt tähän mennessä tämän opetussuunnitelman kautta, että on olemassa ydinperiaatteita kuten kehotteet ja jopa kokonainen ala nimeltä "kehotteiden suunnittelu". Monet työkalut, joiden kanssa voit olla vuorovaikutuksessa kuten ChatGPT, Office 365, Microsoft Power Platform ja monet muut, tukevat sinua käyttämään kehotteita jonkin saavuttamiseksi.

Jos haluat lisätä tällaisen käyttökokemuksen sovellukseen, sinun täytyy ymmärtää käsitteet kuten kehotteet, täydennykset ja valita käytettävä kirjasto. Juuri tätä opit tässä luvussa.

## Johdanto

Tässä luvussa opit:

- Openai-kirjastosta ja sen ydinperiaatteista.
- Rakentamaan tekstintuottosovelluksen käyttäen openai-kirjastoa.
- Ymmärtämään, kuinka käyttää käsitteitä kuten kehotteet, lämpötila ja tokenit tekstintuottosovelluksen rakentamiseksi.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Selittää, mikä tekstintuottosovellus on.
- Rakentaa tekstintuottosovelluksen käyttäen openai-kirjastoa.
- Määrittää sovelluksesi käyttämään enemmän tai vähemmän tokeneita sekä säätää lämpötilaa, vaihtelevan tuloksen saamiseksi.

## Mikä on tekstintuottosovellus?

Tavallisesti kun rakennat sovellusta, siinä on jonkinlainen käyttöliittymä kuten alla:

- Komentopohjainen. Konsolisovellukset ovat tyypillisiä sovelluksia, joissa kirjoitat komennon ja se suorittaa tehtävän. Esimerkiksi `git` on komentopohjainen sovellus.
- Käyttöliittymä (UI). Joissakin sovelluksissa on graafisia käyttöliittymiä (GUI), joissa napsautat painikkeita, syötät tekstiä, valitset vaihtoehtoja ja muuta.

### Konsoli- ja käyttöliittymäsovellukset ovat rajallisia

Vertaa sitä komentopohjaiseen sovellukseen, jossa kirjoitat komennon:

- **Se on rajallinen**. Et voi kirjoittaa mitä tahansa komentoa, ainoastaan niitä, joita sovellus tukee.
- **Kieleen sidottu**. Jotkin sovellukset tukevat monia kieliä, mutta oletuksena sovellus on rakennettu tietylle kielelle, vaikka voit lisätä muitakin kieliä.

### Tekstintuottosovellusten edut

Miten sitten tekstintuottosovellus eroaa?

Tekstintuottosovelluksessa sinulla on enemmän joustavuutta, et ole sidottu joukkoon komentoja tai tiettyyn syötekieleen. Sen sijaan voit käyttää luonnollista kieltä ollaksesi vuorovaikutuksessa sovelluksen kanssa. Toinen etu on se, että olet jo vuorovaikutuksessa datalähteen kanssa, joka on koulutettu valtavalla tietomäärällä, kun taas perinteinen sovellus voi olla rajallinen suhteessa tietokannan sisältöön.

### Mitä voin rakentaa tekstintuottosovelluksella?

Voit rakentaa monenlaisia asioita. Esimerkiksi:

- **Chatbotin**. Chatbot, joka vastaa aiheisiin liittyviin kysymyksiin, kuten yrityksestäsi ja sen tuotteista, voisi olla hyvä valinta.
- **Avustajan**. Suuret kielimallit (LLM) ovat hyviä asioissa kuten tekstin tiivistäminen, insightien saaminen tekstistä, tekstin tuottaminen kuten ansioluettelot ja muuta.
- **Koodiavustajan**. Käyttämästäsi kielimallista riippuen voit rakentaa koodiavustajan, joka auttaa sinua kirjoittamaan koodia. Esimerkiksi voit käyttää tuotetta kuten GitHub Copilot sekä ChatGPT:tä koodin kirjoituksessa.

## Miten pääsen alkuun?

Sinun täytyy löytää tapa integroitua LLM:ään, joka yleensä käsittää seuraavat kaksi lähestymistapaa:

- Käyttää APIa. Tässä sinun täytyy rakentaa web-pyyntöjä kehotteellasi ja saat takaisin tuotetun tekstin.
- Käyttää kirjastoa. Kirjastot auttavat kapseloimaan API-kutsut ja tekevät niiden käytöstä helpompaa.

## Kirjastot/SDK:t

On muutamia hyvin tunnettuja kirjastoja LLM:ien kanssa työskentelyyn kuten:

- **openai**, tämä kirjasto helpottaa mallisi yhdistämistä ja kehotteiden lähettämistä.

Sitten on kirjastoja, jotka toimivat korkeamalla tasolla kuten:

- **Langchain**. Langchain on hyvin tunnettu ja tukee Pythonia.
- **Semantic Kernel**. Semantic Kernel on Microsoftin kirjasto, joka tukee kieliä C#, Python ja Java.

## Ensimmäinen sovellus openai-kirjastolla

Katsotaan, miten voimme rakentaa ensimmäisen sovelluksemme, mitä kirjastoja tarvitsemme, kuinka paljon on tarpeen ja muuta.

### Asenna openai

On monia kirjastoja OpenAI:n tai Azure OpenAI:n kanssa kommunikointiin. On myös mahdollista käyttää useita ohjelmointikieliä kuten C#, Python, JavaScript, Java ja muita. Olemme valinneet käyttää `openai` Python-kirjastoa, joten käytämme `pip` sen asentamiseen.

```bash
pip install openai
```

### Luo resurssi

Sinun täytyy suorittaa seuraavat vaiheet:

- Luo tili Azuren [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Hanki pääsy Azure OpenAI:hin. Siirry [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ja pyydä pääsyä.

  > [!NOTE]
  > Kirjoitushetkellä sinun pitää hakea pääsyä Azure OpenAI:hin.

- Asenna Python <https://www.python.org/>
- Luo Azure OpenAI -palveluresurssi. Katso tämä opastus siitä, miten [luoda resurssi](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Etsi API-avain ja päätepiste

Tässä vaiheessa sinun täytyy kertoa `openai` -kirjastollesi, mitä API-avainta käyttää. Löytääksesi API-avaimesi, siirry Azure OpenAI -resurssisi "Avaimet ja päätepiste" -osioon ja kopioi "Avain 1" -arvo.

![Avaimet ja päätepiste resurssin näkymä Azure-portaalissa](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nyt kun sinulla on tämä tieto kopioituna, ohjataan kirjastot käyttämään sitä.

> [!NOTE]
> On suositeltavaa erottaa API-avain koodistasi. Voit tehdä sen käyttämällä ympäristömuuttujia.
>
> - Aseta ympäristömuuttuja `OPENAI_API_KEY` API-avaimeksi.
>   `export OPENAI_API_KEY='sk-...'`

### Azure-konfiguraation asetukset

Jos käytät Azure OpenAI:ta (nykyisin osa Microsoft Foundryä), näin asetat konfiguraation. Käytämme tavallista `OpenAI` -asiakasta osoitettuna Azure OpenAI -`/openai/v1/` -päätepisteeseen, joka toimii Responses API:n kanssa eikä vaadi `api_version`:a:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Yllä asetamme seuraavat:

- `api_key`, tämä on API-avaimesi, joka löytyy Azure-portaalista tai Microsoft Foundry -portaalista.
- `base_url`, tämä on Foundry-resurssisi päätepiste, johon on lisätty `/openai/v1/`. Vakaasti toimiva v1-päätepiste toimii sekä OpenAI:n että Azure OpenAI:n kanssa ilman `api_version` hallintaa.

> [!NOTE] > `os.environ` lukee ympäristömuuttujia. Voit käyttää sitä lukemaan ympäristömuuttujia kuten `AZURE_OPENAI_API_KEY` ja `AZURE_OPENAI_ENDPOINT`. Aseta nämä ympäristömuuttujat terminaalissasi tai käyttämällä kirjastoa kuten `dotenv`.

## Tekstin generointi

Tekstin syntetisoimiseen käytetään Responses APIa `responses.create` -menetelmän kautta. Tässä esimerkki:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Yllä olevassa koodissa luomme vastauksen ja annamme mallin, jota haluamme käyttää, sekä kehotteen. Sitten tulostamme generoidun tekstin käyttäen `response.output_text`.

### Monivuorovaikutteiset keskustelut

Responses API soveltuu hyvin sekä yksittäisten vuorojen tekstin generoimiseen että monivuorovaikutteisiin chatbotteihin - annat listan viesteistä `input` muodossa keskustelun rakentamiseksi:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Lisää tästä toiminnallisuudesta seuraavassa luvussa.

## Harjoitus – ensimmäinen tekstintuottosovelluksesi

Nyt kun olemme oppineet, miten openai asennetaan ja konfiguroidaan, on aika rakentaa ensimmäinen tekstintuottosovelluksesi. Noudata näitä ohjeita:

1. Luo virtuaaliympäristö ja asenna openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jos käytät Windowsia, kirjoita `venv\Scripts\activate` sijasta `source venv/bin/activate`.

   > [!NOTE]
   > Etsi Azure OpenAI -avaimesi siirtymällä [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ja etsi `Open AI`, valitse `Open AI resource` ja sitten `Keys and Endpoint` ja kopioi `Key 1` arvo.

1. Luo tiedosto _app.py_ ja lisää siihen seuraava koodi:

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
   > Jos käytät tavallista OpenAI:ta (et Azurea), käytä `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (ei `base_url`) ja anna mallin nimi kuten `gpt-5-mini` käyttöön deployment-nimen sijaan.

   Näet ulostulon, joka näyttää plan seuraavalta:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Eri tyyppiset kehotteet eri tarkoituksiin

Nyt olet nähnyt, miten teksti generoidaan kehotteen avulla. Sinulla on jopa toimiva ohjelma käynnissä, jota voit muokata ja vaihtaa tuottamaan erilaisia tekstityyppejä.

Kehotteita voi käyttää moniin tehtäviin. Esimerkiksi:

- **Tuottaa tietynlaista tekstiä**. Voit esimerkiksi tuottaa runon, kysymyksiä tietovisaan jne.
- **Tiedon etsiminen**. Voit käyttää kehotteita etsiäksesi tietoa kuten esimerkkikysymys: 'Mitä CORS tarkoittaa web-kehityksessä?'.
- **Koodin generointi**. Voit käyttää kehotteita koodin tuottamiseen, esimerkiksi säännöllisen lausekkeen kehittämiseen sähköpostien validointiin tai miksei koko ohjelman, kuten web-sovelluksen generointiin?

## Käytännön esimerkki: reseptigeneraattori

Kuvittele, että sinulla on aineksia kotona ja haluat laittaa jotain ruokaa. Tarvitset reseptin. Reseptien löytämiseen voit käyttää hakukonetta tai voit käyttää LLM:ää.

Voisit kirjoittaa kehotteen näin:

> "Näytä 5 reseptiä ruoalle, jossa on seuraavat ainekset: kana, perunat ja porkkanat. Per resepti, listaa kaikki käytetyt ainekset."

Edellä mainitun kehotteen perusteella voit saada vastauksen, joka on tällainen:

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

Tämä tulos on mahtava, tiedän mitä laittaa. Tässä vaiheessa hyödyllisiä parannuksia voisivat olla:

- Suodattaa pois ainekset, joista en pidä tai joita olen allerginen.
- Tuottaa ostoslista siltä varalta, että minulla ei ole kaikkia aineksia kotona.

Yllä mainittuihin tarkoituksiin lisätään lisäkehotte:

> "Ole hyvä ja poista reseptit, joissa on valkosipulia, koska olen allerginen ja korvaa se jollain muulla. Laadi myös ostoslista resepteistä ottaen huomioon, että minulla on jo kotona kana, perunat ja porkkanat."

Nyt sinulla on uusi tulos, nimittäin:

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

Tässä ovat viisi reseptiä ilman valkosipulia sekä ostoslista, kun otetaan huomioon jo olemassa olevat ainekset kotona.

## Harjoitus – rakenna reseptigeneraattori

Nyt kun olemme pelanneet läpi skenaarion, kirjoitetaan koodi, joka vastaa demonstroitua skenaariota. Tee näin:

1. Käytä olemassa olevaa _app.py_-tiedostoa lähtökohtana.
1. Etsi `prompt` muuttuja ja vaihda sen koodi seuraavaan:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jos ajat koodin nyt, sinun pitäisi nähdä tulos, joka on lähempänä tällaista:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > HUOMIO, LLM:si ei ole deterministinen, joten saatat saada eri tuloksia joka kerta ohjelmaa suorittaessasi.

   Hienoa, katsotaan kuinka voimme parantaa asioita. Parantamiseksi haluamme varmistaa, että koodi on joustava, jotta ainesosia ja reseptien määrää voidaan muuttaa ja parantaa.

1. Muutetaan koodia seuraavasti:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Koodin testiajo voisi näyttää tältä:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Paranna lisäämällä suodatin ja ostoslista

Meillä on nyt toimiva sovellus, joka pystyy tuottamaan reseptejä ja se on joustava, koska se perustuu käyttäjän syötteisiin, sekä reseptien määrän että käytettyjen ainesten osalta.

Parantaaksemme sitä lisää, haluamme lisätä seuraavat ominaisuudet:

- **Suodata pois ainekset**. Haluamme pystyä suodattamaan pois ainekset, joista emme pidä tai joille olemme allergisia. Tämä tehdään muokkaamalla kehotetta ja lisäämällä siihen suodatusehto loppuun, vaikka näin:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Yllä lisätään `{filter}` kehotteen loppuun ja keräämme myös suodatusarvon käyttäjältä.

  Esimerkki ohjelman suorittamisesta voi nyt näyttää tältä:

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

  Kuten näet, reseptit, joissa on maitoa, on suodatettu pois. Mutta jos olet laktoosi-intolerantti, saatat haluta suodattaa myös reseptit, joissa on juustoa, joten täytyy olla selkeä.

- **Tuota ostoslista**. Haluamme tuottaa ostoslistan ottaen huomioon, mitä meillä jo on kotona.

  Tätä varten voisimme yrittää ratkaista kaiken yhdessä kehotteessa tai jakaa sen kahteen kehotteeseen. Kokeillaan jälkimmäistä. Tässä ehdotetaan lisäkehotteen lisäämistä, mutta siihen tarvitsemme ensimmäisen kehotteen tuloksen kontekstiksi toiselle kehotteelle.

  Etsi koodista osa, joka tulostaa ensimmäisen kehotteen tuloksen ja lisää seuraava koodi sen alle:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Huomioi seuraavat asiat:

  1. Rakennamme uuden kehotteen lisäämällä ensimmäisen kehotteen tuloksen uuden kehotteen yhteyteen:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Teemme uuden pyynnön, ottaen kuitenkin huomioon ensimmäisessä kehotteessa pyydetyt tokenit, joten tällä kertaa sanomme `max_output_tokens` olevan 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Kun ajat tämän koodin, saat nyt seuraavan ulostulon:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Paranna asetuksiasi

Se, mitä meillä on tähän mennessä, on toimivaa koodia, mutta joitakin säätöjä kannattaa tehdä parantaaksemme asioita edelleen. Joitakin asioita, jotka meidän kannattaa tehdä, ovat:

- **Erottele salaisuudet koodista**, kuten API-avain. Salaisuudet eivät kuulu koodiin ja ne tulisi säilyttää turvallisessa paikassa. Erotellaksemme salaisuudet koodista voimme käyttää ympäristömuuttujia ja kirjastoja kuten `python-dotenv` ladataksemme ne tiedostosta. Tässä on, miltä se näyttäisi koodissa:

  1. Luo tiedosto `.env` seuraavalla sisällöllä:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Huomaa, että Azure OpenAI:ssa Microsoft Foundryssa sinun täytyy sen sijaan asettaa seuraavat ympäristömuuttujat:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Koodissa voit ladata ympäristömuuttujat näin:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Sana tokeneiden pituudesta**. Meidän tulisi pohtia, kuinka monta tokenia tarvitsemme haluamamme tekstin luomiseen. Tokenit maksavat rahaa, joten missä mahdollista meidän tulee pyrkiä käyttämään tokenien määrää taloudellisesti. Voimmeko esimerkiksi muotoilla kehotteen niin, että voimme käyttää vähemmän tokeneita?

  Tokeneiden määrää voit muuttaa käyttämällä parametria `max_output_tokens`. Jos haluat esimerkiksi käyttää 100 tokenia, tekisit näin:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Kokeile lämpötilaa**. Lämpötila on asia, josta emme ole tähän mennessä puhuneet, mutta se on tärkeä konteksti ohjelmamme suorituskyvylle. Mitä korkeampi lämpötilan arvo on, sitä satunnaisempi on tulos. Vastaavasti mitä matalampi lämpötila on, sitä ennustettavampi tulos on. Mieti, haluatko vaihtelua tulokseesi vai et.

  Voit muuttaa lämpötilaa käyttämällä parametria `temperature`. Jos haluat lämpötilaksi 0.5, tekisit näin:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Huomaa, lähemmäs arvoa 1.0 mentäessä tulos on entistä vaihtelevampi.

- **Päättelymalleissa ei käytetä `temperature`**. Tämä on tärkeä muutos vuodelle 2026. Tällä hetkellä Microsoft Foundryn nykyiset, ei vanhentuneet mallit ovat **päättelymalleja** (GPT-5 -perhe, o-sarja) - ja ne **eivät tue `temperature` tai `top_p`** (eivätkä myöskään `max_tokens`; käytä `max_output_tokens`). Jos lähetät `temperature` osoitteeseen `gpt-5-mini`, saat virheen "parametri ei tuettu". Joten kokeillaksesi yllä olevaa lämpötilaesimerkkiä, osoita se mallille, joka edelleen tukee otannan säätimiä - esimerkiksi avoimelle **Llama**-mallille, kuten `Llama-3.3-70B-Instruct` Microsoft Foundryn malliluettelosta [Microsoft Foundry model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), jota kutsutaan Foundry Models / Azure AI Inference -päätepisteen kautta (samalla tavalla kuin `githubmodels-*` -esimerkeissä). Päättelymalleissa kuten GPT-5 outputia ohjataan eri tavalla:
  - **Prompt-suunnittelu** - selkeät ohjeet, esimerkit ja jäsennelty output (katso oppitunti [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) hoitavat sen, mitä ottosäätimet aiemmin tekivät.
  - **Päättelyn säätimet** - parametrit kuten päättelyn vaivannäkö/pitkäpuheisuus vaihtavat päättelyn syvyyden latenssin ja kustannusten kanssa.

  Lyhyesti: `temperature`/`top_p` ovat edelleen voimassa monissa malleissa (Llama, Mistral, Phi ja GPT-4.x -perhe - vaikka GPT-4.x on vanhentumassa), mutta suunta on prompt-suunnittelussa + päättelysäätimissä päättelymalleissa kuten GPT-5.

## Tehtävä

Tässä tehtävässä voit valita, mitä rakennat.

Tässä on joitakin ehdotuksia:

- Hienosäädä reseptigeneraattorisovellusta parantaaksesi sitä edelleen. Kokeile lämpötilan arvoja ja kehotteita nähdäksesi, mitä saat aikaan.
- Rakenna "opiskelukaveri". Tämän sovelluksen tulisi pystyä vastaamaan kysymyksiin tietystä aiheesta, esimerkiksi Pythonista. Voit käyttää kehotteita kuten "Mikä on tietty aihe Pythonissa?" tai kehotetta, joka sanoo, näytä minulle koodi tietystä aiheesta jne.
- Historia-botti, tuo historia eloon, ohjaa bottia esittämään tiettyä historiallista henkilöä ja kysy sille kysymyksiä sen elämästä ja ajasta.

## Ratkaisu

### Opiskelukaveri

Alla on aloituskehote, katso miten voit käyttää sitä ja hienosäätää sitä mieleiseksesi.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historia-botti

Tässä on joitakin kehotteita, joita voisit käyttää:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Tietotarkistus

Mitä lämpötila-käsite tekee?

1. Se säätelee, kuinka satunnainen tulos on.
1. Se säätelee, kuinka pitkä vastaus on.
1. Se säätelee, kuinka monta tokenia käytetään.

## 🚀 Haaste

Työskennellessäsi tehtävän parissa, yritä vaihdella lämpötilaa, kokeile asettaa se arvoihin 0, 0.5 ja 1. Muista, että 0 on vähiten vaihteleva ja 1 eniten. Mikä arvo toimii parhaiten sovelluksessasi?

## Hienoa työtä! Jatka oppimista

Kun olet suorittanut tämän oppitunnin, tutustu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) -kokoelmaamme jatkaaksesi Generatiivisen tekoälyn osaamisesi kehittämistä!

Siirry oppitunnille 7, jossa tarkastelemme, miten [rakentaa chat-sovelluksia](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->