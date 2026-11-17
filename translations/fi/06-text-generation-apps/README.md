# Tekstin generointisovellusten rakentaminen

[![Tekstin generointisovellusten rakentaminen](../../../translated_images/fi/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Olet tähän mennessä nähnyt tämän opintokokonaisuuden aikana, että on olemassa peruskäsitteitä kuten kehotteet ja jopa kokonainen ala nimeltään "kehotteiden suunnittelu". Monet työkalut, joiden kanssa voit olla vuorovaikutuksessa, kuten ChatGPT, Office 365, Microsoft Power Platform ja muut, tukevat kehotteiden käyttöä jonkin tehtävän suorittamisessa.

Jotta voit lisätä tällaisen kokemuksen sovellukseen, sinun täytyy ymmärtää käsitteitä kuten kehotteet, lopputulokset ja valita kirjasto, jonka kanssa työskennellä. Juuri nämä opit tässä luvussa.

## Johdanto

Tässä luvussa opit:

- Openai-kirjastosta ja sen keskeisistä käsitteistä.
- Rakentamaan tekstin generointisovelluksen käyttäen openai-kirjastoa.
- Ymmärtämään, kuinka käyttää käsitteitä kuten kehotteet, lämpötila ja tokenit tekstin generointisovelluksen rakentamiseen.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Selittää, mitä tekstin generointisovellus on.
- Rakentaa tekstin generointisovelluksen käyttäen openai-kirjastoa.
- Määrittää sovelluksesi käyttämään enemmän tai vähemmän tokeneita ja myös muuttaa lämpötilaa vaihtelevan tuloksen saamiseksi.

## Mikä on tekstin generointisovellus?

Normaalisti kun rakennat sovelluksen, sillä on jokin käyttöliittymä kuten seuraava:

- Komentorivipohjainen. Konsolisovellukset ovat tyypillisiä sovelluksia, joissa kirjoitat komennon ja sovellus suorittaa tehtävän. Esimerkiksi `git` on komentorivipohjainen sovellus.
- Käyttöliittymä (UI). Joissakin sovelluksissa on graafinen käyttöliittymä (GUI), jossa napsautat painikkeita, syötät tekstiä, valitset vaihtoehtoja ja muuta.

### Konsoli- ja käyttöliittymäsovelluksilla on rajoitukset

Vertaa komentorivipohjaiseen sovellukseen, jossa kirjoitat komennon:

- **Se on rajoitettu**. Et voi kirjoittaa mitä tahansa komentoa, vain ne, joita sovellus tukee.
- **Kielikohtainen**. Jotkin sovellukset tukevat monia kieliä, mutta oletuksena sovellus on rakennettu tietylle kielelle, vaikka voitkin lisätä tuki useammille kielille.

### Tekstin generointisovellusten edut

Mikä sitten tekee tekstin generointisovelluksesta erilaisen?

Tekstin generointisovelluksessa sinulla on enemmän joustavuutta, et ole sidottu joukkoon komentoja tai tiettyyn syötteen kieleen. Voit käyttää luonnollista kieltä vuorovaikutuksessa sovelluksen kanssa. Toinen etu on, että olet vuorovaikutuksessa tietolähteen kanssa, joka on koulutettu laajalla tietoaineistolla, kun taas perinteinen sovellus saattaa olla rajattu tietokannan sisältöön.

### Mitä voin rakentaa tekstin generointisovelluksella?

Voit rakentaa monenlaisia asioita. Esimerkiksi:

- **Chatbotin**. Chatbot, joka vastaa kysymyksiin aiheista, kuten yrityksestäsi ja sen tuotteista, voisi olla hyvä ratkaisu.
- **Avustajan**. LLM-mallit soveltuvat erinomaisesti tekstin tiivistämiseen, tekstistä saatavien oivallusten hankkimiseen, tekstin tuottamiseen kuten ansioluettelot ja paljon muuta.
- **Koodiavustajan**. Riippuen käyttämästäsi kielimallista, voit rakentaa koodiavustajan, joka auttaa sinua kirjoittamaan koodia. Voit käyttää esimerkiksi GitHub Copilot-tuotetta sekä ChatGPT:tä koodin kirjoittamisen apuna.

## Kuinka voin aloittaa?

Sinun täytyy löytää tapa integroitua LLM:ään, mikä yleensä tarkoittaa kahta lähestymistapaa:

- Käyttää API:a. Tässä muodostat verkkopyyntöjä kehotteellasi ja saat takaisin tuotetun tekstin.
- Käyttää kirjastoa. Kirjastot kapseloivat API-kutsut ja tekevät niiden käytöstä helpompaa.

## Kirjastot/SDK:t

On muutamia hyvin tunnettuja kirjastoja LLM:ien kanssa työskentelyyn kuten:

- **openai**, tämä kirjasto tekee malliin yhdistämisestä ja kehotteiden lähettämisestä helppoa.

Sitten on kirjastoja, jotka toimivat korkeammalla tasolla, kuten:

- **Langchain**. Langchain on hyvin tunnettu ja tukee Pythonia.
- **Semantic Kernel**. Semantic Kernel on Microsoftin kirjasto, joka tukee kieliä C#, Python ja Java.

## Ensimmäinen sovellus käyttäen openai

Katsotaan, kuinka voimme rakentaa ensimmäisen sovelluksemme, mitä kirjastoja tarvitsemme, kuinka paljon on tarpeen ja niin edelleen.

### Asenna openai

On olemassa monia kirjastoja OpenAI:n tai Azure OpenAI:n kanssa vuorovaikutukseen. On mahdollista käyttää myös useita ohjelmointikieliä kuten C#, Python, JavaScript, Java ja muuta. Olemme valinneet käyttää `openai` Python-kirjastoa, joten asennamme sen käyttäen `pip`.

```bash
pip install openai
```

### Luo resurssi

Sinun tulee suorittaa seuraavat vaiheet:

- Luo tili Azureen [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Hanki pääsy Azure OpenAI:iin. Mene osoitteeseen [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ja pyydä pääsy.

  > [!NOTE]
  > Kirjoitushetkellä sinun täytyy hakea pääsy Azure OpenAI:hin.

- Asenna Python <https://www.python.org/>
- Luo Azure OpenAI Service -resurssi. Katso tästä ohje, kuinka [luoda resurssi](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Sijainnin API-avain ja päätepiste

Tässä vaiheessa sinun täytyy kertoa `openai` -kirjastollesi, mitä API-avainta käyttää. Löytääksesi API-avaimesi, mene Azure OpenAI -resurssisi "Keys and Endpoint" -osioon ja kopioi "Key 1" arvo.

![API-avaimet ja päätepiste Azure-portaalissa](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Kun sinulla on tämä tieto kopioituna, ohjataan kirjastot käyttämään sitä.

> [!NOTE]
> On suositeltavaa erottaa API-avain koodistasi. Voit tehdä tämän käyttämällä ympäristömuuttujia.
>
> - Aseta ympäristömuuttuja `OPENAI_API_KEY` API-avaimeksesi.
>   `export OPENAI_API_KEY='sk-...'`

### Azure-konfiguraation asetukset

Jos käytät Azure OpenAI:ta (nyt osa Microsoft Foundry -palvelua), tässä on kuinka määrität konfiguraation. Käytämme vakiintunutta `OpenAI`-asiakasta, joka osoittaa Azure OpenAI `/openai/v1/` -päätepisteeseen, joka toimii Responses API:n kanssa eikä vaadi `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Yllä asetamme seuraavat:

- `api_key`, tämä on API-avaimesi, joka löytyy Azure-portaalista tai Microsoft Foundryn portaalista.
- `base_url`, tämä on Foundry-resurssisi päätepiste, johon on lisätty `/openai/v1/`. Vakaa v1-päätepiste toimii sekä OpenAI:n että Azure OpenAI:n kanssa ilman `api_version` -hallintaa.

> [!NOTE] > `os.environ` lukee ympäristömuuttujia. Voit käyttää sitä lukemaan ympäristömuuttujia kuten `AZURE_OPENAI_API_KEY` ja `AZURE_OPENAI_ENDPOINT`. Aseta nämä ympäristömuuttujat terminaalissasi tai käyttäen kirjastoa kuten `dotenv`.

## Tekstin generointi

Tekstin generointitapa on käyttää Responses API:a `responses.create` -menetelmän kautta. Tässä esimerkki:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Yllä olevassa koodissa luomme vastauksen määrittämällä mallin, jota haluamme käyttää ja kehotteen. Tulostamme sitten generoidun tekstin käyttäen `response.output_text`.

### Monivuoroinen keskustelu

Responses API soveltuu hyvin sekä yksinkertaiseen tekstin generointiin että monivuoroisiin chatbotteihin - toimitat viestilistan `input` rakentaaksesi keskustelua:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Lisätietoja tästä ominaisuudesta tulevassa luvussa.

## Harjoitus - ensimmäinen tekstin generointisovelluksesi

Nyt kun olemme oppineet määrittämään ja konfiguroimaan openai:n, on aika rakentaa ensimmäinen tekstin generointisovelluksesi. Rakentaaksesi sovelluksen, seuraa näitä vaiheita:

1. Luo virtuaaliympäristö ja asenna openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jos käytät Windowsia, kirjoita `venv\Scripts\activate` `source venv/bin/activate` sijasta.

   > [!NOTE]
   > Löydä Azure OpenAI -avaimesi menemällä osoitteeseen [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ja etsi `Open AI` ja valitse `Open AI resource` ja sitten `Keys and Endpoint` ja kopioi `Key 1` arvo.

1. Luo tiedosto _app.py_ ja laita siihen seuraava koodi:

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
   > Jos käytät tavallista OpenAI:ta (ei Azurea), käytä `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (ei `base_url`) ja anna mallin nimi, kuten `gpt-5-mini` sijasta käyttöönoton nimeä.

   Näet jonkin seuraavan kaltaisen tulosteen:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Erilaisia kehotteita eri tarkoituksiin

Nyt olet nähnyt, kuinka generoida tekstiä käyttäen kehotetta. Sinulla on jo toimiva ohjelma, jota voit muokata ja vaihtaa erilaisten tekstityyppien generoimiseksi.

Kehotteita voidaan käyttää kaikenlaisiin tehtäviin. Esimerkiksi:

- **Generoi tietyn tyyppistä tekstiä**. Voit generoida esimerkiksi runon, kysymyksiä tietovisaan jne.
- **Hae tietoa**. Voit käyttää kehotteita tiedon etsimiseen, kuten seuraava esimerkki 'Mitä CORS tarkoittaa web-kehityksessä?'.
- **Generoi koodia**. Voit käyttää kehotteita koodin genereeraamiseen, esimerkiksi kehittää säännöllisen lausekkeen sähköpostiosoitteiden validointiin tai miksi ei generoida kokonainen ohjelma, kuten verkkosovellus?

## Käytännöllisempi esimerkki: reseptigeneraattori

Kuvittele, että sinulla on kotona aineksia ja haluat kokata jotain. Tarvitset reseptin siihen. Reseptien löytäminen voi tapahtua hakukoneella tai voit käyttää LLM:ää.

Voisit kirjoittaa kehotteen seuraavasti:

> "Näytä minulle 5 reseptiä ruoalle, jossa on seuraavat raaka-aineet: kana, perunat ja porkkanat. Luettele kutakin reseptiä varten kaikki käytetyt ainekset"

Edellä mainitulla kehotteella saatat saada vastauksen, joka on samanlainen kuin:

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

Tämä lopputulos on erinomainen, tiedän mitä kokata. Tässä vaiheessa hyödyllisiä parannuksia voisivat olla:

- Suodattaa pois ainekset, joita en pidä tai joille olen allerginen.
- Tuottaa ostoslista, jos minulla ei ole kaikkia aineksia kotona.

Yllä olevissa tapauksissa lisätään lisäkysely:

> "Poista resepteistä valkosipuli, koska olen allerginen, ja korvaa se jollain muulla. Lisäksi tuota ostoslista reseptejä varten ottaen huomioon, että minulla on jo kanaa, perunoita ja porkkanoita kotona."

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

Tässä on viisi reseptiä, joissa ei mainita valkosipulia, ja sinulla on myös ostoslista ottaen huomioon kotona jo olevat ainekset.

## Harjoitus - rakenna reseptigeneraattori

Nyt kun olemme käyneet skenaarion läpi, kirjoitetaan koodi vastaamaan sitä. Noudata seuraavia ohjeita:

1. Käytä olemassa olevaa _app.py_-tiedostoa lähtökohtana
1. Etsi `prompt` muuttuja ja vaihda sen koodi seuraavaan:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jos suoritat nyt koodin, sinun pitäisi nähdä seuraavan kaltainen tuloste:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > HUOM: LLM-mallisi on epädeterministinen, joten saatat saada erilaisia tuloksia joka kerta kun suoritat ohjelman.

   Hienoa, katsotaan kuinka voimme parantaa asioita. Parantaaksemme haluamme tehdä koodista joustavan, jotta annoksia ja raaka-aineita voi muuttaa ja parantaa.

1. Muutetaan koodia seuraavasti:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testiajolla koodi voisi näyttää tältä:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Paranna lisäämällä suodatin ja ostoslista

Meillä on nyt toimiva sovellus, joka pystyy tuottamaan reseptejä ja se on joustava, koska riippuu käyttäjän antamista tiedoista, sekä annosten määrästä että käytetyistä aineksista.

Parantaaksemme sitä entisestään haluamme lisätä seuraavat ominaisuudet:

- **Suodata pois aineksia**. Haluamme pystyä suodattamaan pois aineksia, joita emme pidä tai joille olemme allergisia. Tämän muutoksen saavuttamiseksi voimme muokata olemassa olevaa kehotetta ja lisätä suodatinlauseen sen loppuun näin:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Yllä lisäämme `{filter}` kehotteen loppuun ja myös otamme suodatinarvon käyttäjältä.

  Esimerkki ohjelman ajosta voisi nyt näyttää tältä:

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

  Kuten näet, kaikki reseptit, joissa on maitoa, on suodatettu pois. Mutta jos olet laktoosi-intolerantti, saatat haluta suodattaa myös reseptit, joissa on juustoa, joten tästä täytyy olla selkeä.

- **Tuota ostoslista**. Haluamme tuottaa ostoslistan, ottaen huomioon mitä meillä jo on kotona.

  Tätä ominaisuutta varten voimme joko yrittää tehdä kaiken yhdellä kehotteella tai voimme jakaa sen kahteen kehotteeseen. Kokeillaan jälkimmäistä lähestymistapaa. Tässä ehdotamme lisäkehotteen lisäämistä, mutta sen toimimiseksi pitää lisätä ensimmäisen kehotteen tulos kontekstina toiseen kehotteeseen.

  Etsi koodista kohta, joka tulostaa ensimmäisen kehotteen tuloksen ja lisää seuraava koodi alle:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Huomaa seuraava:

  1. Rakennamme uuden kehotteen lisäämällä ensimmäisen kehotteen tuloksen uuteen kehotteeseen:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Teemme uuden pyynnön, ottaen huomioon ensimmäisellä kehotteella pyytämämme tokenimäärän, joten tällä kertaa asetamme `max_output_tokens` arvoksi 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Kun ajat tätä koodia, päädymme seuraavaan tulokseen:

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

Se, mitä meillä on tähän mennessä, on toimivaa koodia, mutta joitakin säätöjä pitäisi tehdä parantaaksemme asioita edelleen. Jotkin asiat, jotka meidän pitäisi tehdä, ovat:

- **Erottele salaisuudet koodista**, kuten API-avain. Salaisuudet eivät kuulu koodiin ja ne pitäisi säilyttää turvallisessa paikassa. Erotellaksemme salaisuudet koodista, voimme käyttää ympäristömuuttujia ja kirjastoja kuten `python-dotenv` ladataksemme ne tiedostosta. Näin se näyttäisi koodissa:

  1. Luo `.env` tiedosto seuraavalla sisällöllä:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Huomaa, että Azure OpenAI:ssa Microsoft Foundryssä sinun tulee asettaa sen sijaan seuraavat ympäristömuuttujat:

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

- **Sana token-pituudesta**. Meidän pitäisi miettiä, kuinka monta tokenia tarvitsemme haluamamme tekstin luomiseen. Tokenit maksavat, joten mahdollisuuksien mukaan meidän tulisi olla taloudellisia käyttämämme tokenien määrän kanssa. Voisimmeko esimerkiksi muotoilla kehotteen niin, että voimme käyttää vähemmän tokeneita?

  Muuttaaksesi käytettyjen tokenien määrää, voit käyttää parametria `max_output_tokens`. Esimerkiksi, jos haluat käyttää 100 tokenia, tekisit näin:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Kokeilu lämpötilalla**. Lämpötila on jotain, mitä emme ole tähän mennessä maininneet, mutta se on tärkeä konteksti sille, miten ohjelmamme käyttäytyy. Mitä korkeampi lämpötilan arvo on, sitä satunnaisempi tulos on. Vastaavasti mitä matalampi lämpötilan arvo on, sitä ennustettavampi tulos on. Mieti, haluatko vaihtelua lopputuloksessasi vai et.

  Muuttaaksesi lämpötilaa, voit käyttää parametria `temperature`. Esimerkiksi, jos haluat käyttää lämpötilaa 0.5, tekisit näin:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Huomaa, että mitä lähempänä arvo on 1.0, sitä vaihtelevampi tulos on.

- **Päättelymalleissa ei käytetä `temperature`**. Tämä on tärkeä muutos vuodelle 2026. Tällä hetkellä käytettävissä olevat, ei vanhentuneet mallit Microsoft Foundryssa ovat **päättelymalleja** (GPT-5 -perhe, o-sarja) - ja ne **eivät tue `temperature` tai `top_p`** (eivät myöskään `max_tokens`; käytä `max_output_tokens`). Jos lähetät `temperature` osoitteeseen `gpt-5-mini`, saat "parametri ei ole tuettu" -virheen. Joten kokeillaksesi yllä olevaa lämpötilaesimerkkiä, osoita se mallille, joka tukee vielä otannan säätimiä – esimerkiksi avoimelle **Llama**-mallille, kuten `Llama-3.3-70B-Instruct` Microsoft Foundryn malliluettelosta [Microsoft Foundry model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), kutsuttuna Foundry Models / Azure AI Inference -päätepisteestä (sama tapa kuin `githubmodels-*` esimerkeissä). GPT-5:n kaltaisissa päättelymalleissa ohjaat lopputulosta eri tavalla:
  - **Promptin suunnittelu** – selkeät ohjeet, esimerkit ja jäsennelty lopputulos (katso oppitunti [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) hoitavat sen, mitä otannan säätimet aiemmin tekivät.
  - **Päättelyn ohjaus** – parametrit kuten päättelyponnistus/pitkäpiimäisyys vaihtavat päättelyn syvyyden viiveen ja kustannusten kanssa.

  Lyhyesti sanottuna: `temperature`/`top_p` ovat edelleen voimassa monissa malleissa (Llama, Mistral, Phi ja GPT-4.x -perhe – vaikka GPT-4.x on vanhentumassa), mutta suunta on promptin suunnittelu + päättelyn ohjaus päättelymalleissa kuten GPT-5.

## Tehtävä

Tässä tehtävässä voit valita, mitä rakennat.

Tässä muutama ehdotus:

- Säädä reseptigeneraattori -sovellusta entistä paremmaksi. Kokeile lämpötila-arvoja ja kehotteita nähdäksesi, mitä saat aikaiseksi.
- Rakenna "opiskelukaveri". Tämän sovelluksen pitäisi osata vastata kysymyksiin aiheesta, esimerkiksi Pythonista; voit käyttää kehotteita kuten "Mikä on tietty aihe Pythonissa?" tai kehotetta, joka pyytää näyttämään koodin tietystä aiheesta.
- Historia-botti, tee historiasta elävää, ohjaa bottia esittämään tietty historiallinen hahmo ja kysy siitä kysymyksiä sen elämästä ja ajoista.

## Ratkaisu

### Opiskelukaveri

Alla on aloituskehotteita, katso miten voit käyttää niitä ja muokata mieleiseksesi.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historia-botti

Tässä joitakin kehotteita, joita voit käyttää:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Tietotarkistus

Mitä käsite lämpötila tekee?

1. Se säätelee, kuinka satunnainen lopputulos on.
1. Se säätelee, kuinka suuri vastaus on.
1. Se säätelee, kuinka monta tokenia käytetään.

## 🚀 Haaste

Kun työskentelet tehtävän parissa, kokeile vaihdella lämpötilaa asettamalla se arvoihin 0, 0.5 ja 1. Muista, että 0 on vähiten vaihteleva ja 1 eniten. Mikä arvo toimii parhaiten sovelluksessasi?

## Hienoa työtä! Jatka oppimista

Tehtyäsi tämän oppitunnin, tarkista [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi Generative AI -tietämyksesi kehittämistä!

Siirry oppitunnille 7, jossa tarkastelemme, miten [rakentaa chat-sovelluksia](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->