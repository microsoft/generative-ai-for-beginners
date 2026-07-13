# Tekstintuotantosovellusten rakentaminen

[![Tekstintuotantosovellusten rakentaminen](../../../translated_images/fi/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin video)_

Olet tähän mennessä nähnyt tässä opetussuunnitelmassa, että on keskeisiä käsitteitä kuten kehotteet ja jopa kokonainen ala nimeltä "prompt-tekniikka". Monet työkalut, kuten ChatGPT, Office 365, Microsoft Power Platform ja monet muut, tukevat sinua kehotteiden avulla jonkin saavuttamisessa.

Jotta voisit lisätä tällaisen kokemuksen sovellukseen, sinun on ymmärrettävä käsitteitä kuten kehotteet, täydennykset ja valittava kirjasto, jonka kanssa työskennellä. Juuri tämän opit tässä luvussa.

## Johdanto

Tässä luvussa:

- Opit openai-kirjastosta ja sen keskeisistä käsitteistä.
- Rakennat tekstintuotantosovelluksen käyttäen openai-kirjastoa.
- Ymmärrät, miten käytät käsitteitä kuten kehotetta, lämpötilaa ja tokeneita tekstintuotantosovelluksen rakentamisessa.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Selittää, mikä tekstintuotantosovellus on.
- Rakentaa tekstintuotantosovelluksen openai-kirjastolla.
- Määrittää sovelluksesi käyttämään enemmän tai vähemmän tokeneita sekä muuttaa lämpötilaa vaihtelevan tuloksen saamiseksi.

## Mikä on tekstintuotantosovellus?

Normaalisti kun rakennat sovelluksen, siinä on jonkinlainen käyttöliittymä, esimerkiksi:

- Komentorivipohjainen. Konsolisovellukset ovat tyypillisiä sovelluksia, joissa kirjoitat komennon ja sovellus suorittaa tehtävän. Esimerkiksi `git` on komentorivisovellus.
- Käyttöliittymä (UI). Joissakin sovelluksissa on graafinen käyttöliittymä (GUI), jossa napsautat painikkeita, syötät tekstiä, valitset vaihtoehtoja ja muuta.

### Konsoli- ja UI-sovellukset ovat rajallisia

Vertaa sitä komentorivisovellukseen, jossa kirjoitat komennon:

- **Se on rajallista**. Et voi kirjoittaa mitä tahansa komentoa, vain niitä, joita sovellus tukee.
- **Kielispesifistä**. Jotkut sovellukset tukevat monia kieliä, mutta oletuksena sovellus on rakennettu tietylle kielelle, vaikka voit lisätä kielitukea.

### Tekstintuotantosovellusten hyödyt

Mikä siis erottaa tekstintuotantosovelluksen?

Tekstintuotantosovelluksessa sinulla on enemmän joustavuutta, et ole sidottu komentojoukkoon tai tiettyyn syötekieleen. Sen sijaan voit käyttää luonnollista kieltä vuorovaikutukseen sovelluksen kanssa. Toinen etu on, että olet jo tekemisissä tietolähteen kanssa, joka on koulutettu valtavalla tietomäärällä, kun taas perinteinen sovellus saattaa olla rajoitettu tietokannan sisältöön.

### Mitä voin rakentaa tekstintuotantosovelluksella?

Voit rakentaa monia asioita. Esimerkiksi:

- **Chatbotin**. Chatbot, joka vastaa kysymyksiin aiheista kuten yrityksesi ja sen tuotteiden osalta, voi olla hyvä valinta.
- **Avustajan**. Suuret kielimallit (LLM) ovat hyviä esimerkiksi tekstin tiivistämisessä, tiedon hankinnassa tekstistä, tekstien tuottamisessa kuten ansioluettelot ja muuta.
- **Koodiavustajan**. Riippuen käyttämästäsi kielimallista, voit rakentaa koodiavustajan joka auttaa koodin kirjoittamisessa. Esimerkiksi voit käyttää tuotteita kuten GitHub Copilot sekä ChatGPT:tä koodin tuottamiseen.

## Miten pääsen alkuun?

Sinun täytyy löytää tapa integroitua LLM:ään, mikä yleensä tarkoittaa kahta lähestymistapaa:

- Käytä APIa. Tässä muodostat web-pyyntöjä kehotteellasi ja saat tuotetun tekstin takaisin.
- Käytä kirjastoa. Kirjastot kapseloivat API-kutsut ja tekevät niistä helpompia käyttää.

## Kirjastot/SDK:t

On muutamia tunnettuja kirjastoja LLM:ien kanssa työskentelyyn, kuten:

- **openai**, tämä kirjasto helpottaa malliin yhdistämistä ja kehotteiden lähettämistä.

Sitten on kirjastoja, jotka toimivat korkeammalla tasolla, kuten:

- **Langchain**. Langchain on tunnettu ja tukee Pythonia.
- **Semantic Kernel**. Semantic Kernel on Microsoftin kirjasto, joka tukee kieliä C#, Python ja Java.

## Ensimmäinen sovellus openai:lla

Katsotaanpa, miten rakennamme ensimmäisen sovelluksemme, mitä kirjastoja tarvitsemme, kuinka paljon vaaditaan ja niin edelleen.

### Asenna openai

On monia kirjastoja OpenAI:n tai Azure OpenAI:n kanssa työskentelyyn. On mahdollista käyttää useita ohjelmointikieliä kuten C#, Python, JavaScript, Java ja muuta. Olemme valinneet käyttää `openai` Python-kirjastoa, joten käytämme `pip`:iä sen asentamiseen.

```bash
pip install openai
```

### Luo resurssi

Sinun tulee suorittaa seuraavat vaiheet:

- Luo tili Azuren palvelussa [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Hanki pääsy Azure OpenAI:hin. Mene osoitteeseen [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ja hae pääsyä.

  > [!NOTE]
  > Kirjoittamisajankohtana sinun täytyy hakea pääsyä Azure OpenAI:hin.

- Asenna Python <https://www.python.org/>
- Luo Azure OpenAI Service -resurssi. Katso opas resurssin [luomiseen](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Etsi API-avain ja päätepiste

Nyt sinun tulee kertoa `openai`-kirjastolle, mitä API-avainta käyttää. Löytääksesi API-avaimesi, mene Azure OpenAI -resurssisi "Keys and Endpoint" -osioon ja kopioi sieltä "Key 1" -arvo.

![Keys and Endpoint -resurssilauta Azure Portalissa](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nyt kun sinulla on tämä tieto kopioituna, ohjeistetaan kirjastot käyttämään sitä.

> [!NOTE]
> On suositeltavaa erottaa API-avain koodistasi. Voit tehdä sen ympäristömuuttujilla.
>
> - Aseta ympäristömuuttuja `OPENAI_API_KEY` API-avaimellesi.
>   `export OPENAI_API_KEY='sk-...'`

### Määritä konfiguraatio Azurelle

Jos käytät Azure OpenAI:ta (nykyään osa Microsoft Foundry -palvelua), näin asetat konfiguraation. Käytämme vakiintunutta `OpenAI`-asiakasta osoitettuna Azure OpenAI -päätepisteeseen `/openai/v1/`, joka toimii Responses API:n kanssa eikä tarvitse `api_version`-määritystä:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Yllä asetamme seuraavat:

- `api_key`, eli API-avaimesi, joka löytyy Azure-portaalista tai Microsoft Foundry -portaalista.
- `base_url`, eli Foundry-resurssisi päätepiste, johon on liitetty `/openai/v1/`. Tämä vakaa v1-päätepiste toimii sekä OpenAI:n että Azure OpenAI:n kanssa ilman `api_version`-hallintaa.

> [!NOTE] > `os.environ` lukee ympäristömuuttujia. Voit käyttää sitä lukemaan ympäristömuuttujat kuten `AZURE_OPENAI_API_KEY` ja `AZURE_OPENAI_ENDPOINT`. Aseta nämä ympäristömuuttujat terminaalissasi tai käytä kirjastoa kuten `dotenv`.

## Tuota tekstiä

Tekstin tuottamiseen käytetään Responses API:a `responses.create`-metodin kautta. Tässä esimerkki:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # tämä on mallisi käyttöönoton nimi
    input=prompt,
    store=False,
)
print(response.output_text)
```

Yllä olevassa koodissa luomme vastauksen, annamme mallin ja kehotteen, sitten tulostamme tuotetun tekstin `response.output_text`:in kautta.

### Monikierroskeskustelut

Responses API soveltuu hyvin sekä yksittäisen vuoron tekstintuotantoon että monikierros-chatbotteihin - annat viestilistan `input`-parametrissa keskustelun rakentamiseksi:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Tästä toiminnallisuudesta lisää tulevassa luvussa.

## Harjoitus - ensimmäinen tekstintuotantosovellus

Nyt kun olemme oppineet kuinka asettaa ja konfiguroida openai-kirjasto, on aika rakentaa ensimmäinen tekstintuotantosovelluksesi. Tee seuraavasti:

1. Luo virtuaaliympäristö ja asenna openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jos käytät Windowsia, kirjoita `venv\Scripts\activate` komentojen `source venv/bin/activate` sijasta.

   > [!NOTE]
   > Löydä Azure OpenAI -avaimesi menemällä osoitteeseen [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), hae `Open AI`, valitse `Open AI resource`, sitten `Keys and Endpoint` ja kopioi `Key 1` -arvo.

1. Luo tiedosto _app.py_ ja lisää siihen seuraava koodi:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # lisää täydennyskoodisi
   prompt = "Complete the following: Once upon a time there was a"

   # tee pyyntö Responses API:n avulla
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # tulosta vastaus
   print(response.output_text)
   ```

   > [!NOTE]
   > Jos käytät puhdasta OpenAI:ta (ei Azurea), käytä `client = OpenAI(api_key="<korvaa tämä arvo OpenAI-avaimellasi>")` (ilman `base_url`) ja anna mallin nimeksi esimerkiksi `gpt-4o-mini` käyttöönottotunnuksen sijasta.

   Näet tulosteen, joka näyttää esimerkiksi tältä:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Erilaisia kehotetyyppejä eri tarkoituksiin

Nyt olet nähnyt, miten teksti tuotetaan kehotteen avulla. Sinulla on jo ohjelma käynnissä, jota voit muokata ja muuttaa tuottamaan erilaisia tekstityyppejä.

Kehotteita voidaan käyttää kaikenlaisiin tehtäviin, esimerkiksi:

- **Tuottaa tietynlaista tekstiä**. Voit esimerkiksi luoda runon, kysymyksiä tietovisaan jne.
- **Hakea tietoa**. Voit käyttää kehotteita tietojen hakemiseen, kuten esimerkissä "Mitä CORS tarkoittaa web-kehityksessä?".
- **Tuottaa koodia**. Voit käyttää kehotteita koodin tuottamiseen, esimerkiksi kirjoittaa säännöllisen lausekkeen sähköpostien validointiin tai jopa luoda kokonaisen ohjelman, kuten web-sovelluksen.

## Käytännöllisempi sovellus: reseptigeneraattori

Kuvittele, että sinulla on aineksia kotona ja haluat kokata jotain. Tarvitset reseptin. Reseptin löytämiseen voit käyttää hakukonetta tai LLM:ää.

Voisit kirjoittaa kehotteen esimerkiksi näin:

> "Näytä minulle 5 reseptiä ruokalajiin, jossa on seuraavat ainekset: kana, perunat ja porkkanat. Listaa jokaista reseptiä kohden kaikki käytetyt ainekset."

Saamasi vastaus voisi olla esimerkiksi:

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

Tämä tulos on loistava, tiedän mitä kokata. Tässä vaiheessa hyödyllisiä parannuksia voisivat olla:

- Suodatus pois aineksista, joista en pidä tai joille olen allerginen.
- Ostoslistan tuottaminen, jos minulla ei ole kaikkia aineksia kotona.

Näitä varten lisätään lisäkehotteita:

> "Poista resepteistä valkosipuli, koska olen sille allerginen, ja korvaa jollain muulla. Tee myös ostoslista resepteille, ottaen huomioon että minulla on jo kana, perunat ja porkkanat kotona."

Nyt saat uuden tuloksen, nimittäin:

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

Tässä ovat viisi reseptiä ilman valkosipulia ja ostoslistakin on mukana, jolloin otetaan huomioon kotona jo olemassa olevat ainekset.

## Harjoitus - rakenna reseptigeneraattori

Kun olemme käyneet skenaarion läpi, kirjoitetaan koodi vastaamaan sitä. Toimi näin:

1. Käytä olemassa olevaa _app.py_ -tiedostoa lähtökohtana
1. Etsi muuttuja `prompt` ja muokkaa sen koodi seuraavaksi:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jos ajat nyt koodin, pitäisi tulosteen näyttää suunnilleen tältä:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > HUOMAUTUS, LLM:si on epädeterministinen, joten voit saada erilaisia tuloksia joka kerta kun suoritat ohjelman.

   Loistavaa, katsotaan miten voimme parantaa asioita. Halumme on tehdä koodista joustavaa, jotta reseptien lukumäärää ja ainesosia voidaan helposti muuttaa.

1. Muutetaan koodia seuraavasti:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpoloida reseptien määrä kehotteeseen ja ainesosiin
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testiajona koodi voisi näyttää tältä:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Paranna lisäämällä suodatin ja ostoslista

Nyt meillä on toimiva sovellus, joka pystyy tuottamaan reseptejä ja on joustava, koska se perustuu käyttäjän antamiin syötteisiin, sekä reseptien määrään että käytettäviin aineksiin.

Parantaaksemme sitä haluamme lisätä seuraavat toiminnot:

- **Suodata pois ainekset**. Haluamme voida poistaa aineksia, joista emme pidä tai joille olemme allergisia. Tämän muutoksen teemme muokkaamalla olemassa olevaa kehotettamme ja lisäämällä loppuun suodattimen, esimerkiksi näin:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Yllä lisäämme `{filter}` kehotteen loppuun ja otamme myös käyttäjän antaman suodatinarvon talteen.

  Esimerkiksi ohjelman suoritus voisi nyt näyttää tältä:

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

  Kuten näet, kaikki reseptit, joissa on maitoa, on suodatettu pois. Mutta jos olet laktoosi-intolerantti, saatat haluta suodattaa pois myös juustolliset reseptit, joten selkeys on tarpeen.


- **Tuota ostoslista**. Haluamme tuottaa ostoslistan ottaen huomioon, mitä meillä jo on kotona.

  Tätä toimintoa varten voisimme yrittää ratkaista kaiken yhdellä kehotteella tai jakaa sen kahteen kehotteeseen. Kokeillaan jälkimmäistä lähestymistapaa. Tässä ehdotamme lisättävän toisen kehotteen, mutta jotta se toimisi, meidän täytyy lisätä ensimmäisen kehotteen tulos kontekstina toiseen kehotteeseen.

  Etsi koodi, joka tulostaa ensimmäisen kehotteen tuloksen ja lisää seuraava koodi sen alle:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # tulosta vastaus
  print("Shopping list:")
  print(response.output_text)
  ```

  Huomaa seuraavat asiat:

  1. Rakennamme uutta kehotetta lisäämällä ensimmäisen kehotteen tuloksen uuteen kehotteeseen:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Teemme uuden pyynnön, mutta otamme huomioon myös ensimmäisessä kehotteessa pyydetyn token-määrän, joten tällä kertaa asetamme `max_output_tokens` arvoksi 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Kun kokeilemme tätä koodia, saamme seuraavan tulosteen:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Paranna asetustasi

Tähän asti meillä on toimiva koodi, mutta on joitain säätöjä, joita meidän tulisi tehdä parantaaksemme asioita edelleen. Joitakin tekemistä asioista ovat:

- **Erota salaisuudet koodista**, kuten API-avain. Salaisuudet eivät kuulu koodiin ja ne tulisi säilyttää turvallisessa paikassa. Salaisuuksien erottamiseksi koodista voimme käyttää ympäristömuuttujia ja kirjastoja kuten `python-dotenv` lataamaan ne tiedostosta. Näin se näyttäisi koodissa:

  1. Luo `.env`-tiedosto seuraavalla sisällöllä:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Huomaa, että Azure OpenAI:ssa Microsoft Foundryssä sinun tulee asettaa seuraavat ympäristömuuttujat sen sijaan:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Koodissa lataisit ympäristömuuttujat näin:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Sana token-pituudesta**. Meidän tulisi harkita kuinka monta tokenia tarvitsemme tuottaaksemme halutun tekstin. Tokenit maksavat rahaa, joten siellä missä mahdollista, meidän tulisi olla taloudellisia tokenien käytössä. Voimmeko esimerkiksi sanoa kehotteen niin, että voimme käyttää vähemmän tokeneita?

  Muuttaaksesi käytettyjä tokeneita voit käyttää parametria `max_output_tokens`. Esimerkiksi, jos haluat käyttää 100 tokenia, tekisit näin:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Lämpötilan kokeilu**. Lämpötila on asia, jota emme ole tähän asti maininneet, mutta se on tärkeää ohjelmamme suorituskyvylle. Mitä korkeampi lämpötila-arvo on, sitä satunnaisempi tuloste on. Vastaavasti mitä matalampi lämpötila-arvo on, sitä ennustettavampi tuloste on. Mieti haluatko vaihtelua tulosteeseesi vai et.

  Muuttaaksesi lämpötilaa, voit käyttää parametria `temperature`. Esimerkiksi jos haluat käyttää lämpötilaa 0.5, tekisit näin:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Huomaa, että mitä lähempänä arvo on 1.0, sitä vaihtelevampi tuloste on.

## Tehtävä

Tässä tehtävässä voit valita, mitä rakennat.

Tässä on joitakin ehdotuksia:

- Säädä reseptigeneraattorisovellusta parantaaksesi sitä edelleen. Kokeile lämpötila-arvoja ja kehotteita nähdäksesi, mitä voit keksiä.
- Rakenna "opiskelutoveri". Tämän sovelluksen tulisi pystyä vastaamaan kysymyksiin tietystä aiheesta, esimerkiksi Pythonista, voit käyttää kehotteita kuten "Mikä on tietty aihe Pythonissa?", tai kehotetta, joka sanoo, näytä minulle koodi tietystä aiheesta jne.
- Historia-botti, tee historiasta elävää, ohjeista bottia esittämään tietty historiallinen hahmo ja kysy siitä kysymyksiä sen elämästä ja ajasta.

## Ratkaisu

### Opiskelutoveri

Alla on aloituskehotus, katso miten voit käyttää sitä ja säätää sitä mieleiseksesi.

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

## Tietotesti

Mitä käsite lämpötila tekee?

1. Se määrää, kuinka satunnainen tuloste on.
1. Se määrää, kuinka suuri vastaus on.
1. Se määrää, kuinka monta tokenia käytetään.

## 🚀 Haaste

Kun työskentelet tehtävän parissa, kokeile vaihdella lämpötilaa, kokeile asettaa se arvoihin 0, 0.5 ja 1. Muista, että 0 on vähiten vaihteleva ja 1 eniten. Mikä arvo toimii parhaiten sovelluksessasi?

## Hienoa työtä! Jatka oppimista

Tämän oppitunnin suorittamisen jälkeen tutustu [Generative AI Learning -kokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generative AI -tietosi nostamista seuraavalle tasolle!

Siirry oppitunnille 7, jossa tarkastelemme, kuinka [rakentaa chat-sovelluksia](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->