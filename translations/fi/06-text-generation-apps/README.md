# Tekstintuotantosovellusten rakentaminen

[![Tekstintuotantosovellusten rakentaminen](../../../translated_images/fi/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Olet tähän mennessä nähnyt tämän opintokokonaisuuden kautta, että on olemassa ydinkäsitteitä, kuten kehotteet, ja jopa kokonainen ala nimeltään "kehoteinsinööritaito". Monet työkalut, joiden kanssa voit olla vuorovaikutuksessa, kuten ChatGPT, Office 365, Microsoft Power Platform ja muut, tukevat sinua käyttämällä kehotteita jonkin tavoitteen saavuttamiseksi.

Jotta voit lisätä tällaisen kokemuksen sovellukseen, sinun täytyy ymmärtää käsitteitä kuten kehotteet, täydennykset ja valita kirjasto, jota käytät. Juuri tämän opit tässä luvussa.

## Johdanto

Tässä luvussa:

- Opit openai-kirjastosta ja sen ydinkäsitteistä.
- Rakennat tekstintuotantosovelluksen openai-kirjastoja käyttäen.
- Ymmärrät, miten käyttää käsitteitä kuten kehote, lämpötila ja tokenit tekstintuotantosovelluksen rakentamisessa.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Selittää, mitä tekstintuotantosovellus on.
- Rakentaa tekstintuotantosovelluksen openai-kirjastoa käyttäen.
- Määrittää sovelluksesi käyttämään enemmän tai vähemmän tokeneita ja myös muuttaa lämpötilaa monipuolisemman tuloksen saamiseksi.

## Mitä on tekstintuotantosovellus?

Tavallisesti kun rakennat sovelluksen, siinä on jokin käyttöliittymä, kuten seuraava:

- Komentorivipohjainen. Konsolisovellukset ovat tyypillisiä sovelluksia, joissa kirjoitat komennon ja se suorittaa tehtävän. Esimerkiksi `git` on komentorivipohjainen sovellus.
- Käyttöliittymä (UI). Joissain sovelluksissa on graafinen käyttöliittymä (GUI), jossa napsautat painikkeita, syötät tekstiä, valitset vaihtoehtoja ja muuta.

### Konsoli- ja käyttöliittymäsovellukset ovat rajallisia

Vertaa sitä komentorivisovellukseen, johon kirjoitat komennon:

- **Se on rajallinen**. Et voi vain kirjoittaa mitä tahansa komentoa, vain niitä, joita sovellus tukee.
- **Kielikohtainen**. Jotkin sovellukset tukevat useita kieliä, mutta oletuksena sovellus on rakennettu tietylle kielelle, vaikka voit lisätä lisää kielitukea.

### Tekstintuotantosovellusten edut

Miten sitten tekstintuotantosovellus eroaa?

Tekstintuotantosovelluksessa sinulla on enemmän joustavuutta, et ole rajoitettu joukkoon komentoja tai tiettyyn syöttökieleen. Sen sijaan voit käyttää luonnollista kieltä sovelluksen kanssa vuorovaikutukseen. Toinen etu on, että olet jo vuorovaikutuksessa tietolähteen kanssa, joka on koulutettu valtavalla tiedon korpuksella, kun taas perinteinen sovellus saattaa olla rajoittunut tietokannan sisältöön.

### Mitä voin rakentaa tekstintuotantosovelluksella?

Voit rakentaa monenlaisia asioita. Esimerkiksi:

- **Chatbotin**. Chatbot, joka vastaa kysymyksiin aiheista kuten yrityksestäsi ja sen tuotteista, voisi olla sopiva.
- **Avustajan**. LLM:t ovat erinomaisia asioissa kuten tekstin tiivistäminen, tekstistä oivallusten saaminen, tekstin tuottaminen kuten ansioluettelot ja muuta.
- **Koodiavustajan**. Riippuen käyttämästäsi kielimallista, voit rakentaa koodiavustajan, joka auttaa sinua kirjoittamaan koodia. Esimerkiksi voit käyttää GitHub Copilot -tuotetta sekä ChatGPT:tä koodin kirjoittamisen apuna.

## Miten pääsen alkuun?

Tarvitset tavan integroitua LLM:ään, joka tavallisesti sisältää seuraavat kaksi lähestymistapaa:

- Käytä APIa. Täällä muodostat verkkopyyntöjä kehotteellasi ja saat takaisin generoitu tekstin.
- Käytä kirjastoa. Kirjastot auttavat kapseloimaan API-kutsut ja tekevät niistä helpompia käyttää.

## Kirjastot/SDK:t

On muutamia tunnettuja kirjastoja LLM:ien kanssa työskentelyyn kuten:

- **openai**, tämä kirjasto tekee helppoa yhdistää malliin ja lähettää kehotteita.

Sitten on kirjastoja, jotka toimivat korkeammalla tasolla, kuten:

- **Langchain**. Langchain on tunnettu ja tukee Pythonia.
- **Semantic Kernel**. Semantic Kernel on Microsoftin kirjasto, joka tukee kieliä C#, Python ja Java.

## Ensimmäinen sovellus openai-kirjastolla

Katsotaanpa, miten voimme rakentaa ensimmäisen sovelluksemme, mitä kirjastoja tarvitsemme, kuinka paljon vaaditaan ja niin edelleen.

### Asenna openai

On monia kirjastoja, joita voi käyttää OpenAI:n tai Azure OpenAI:n kanssa. On mahdollista käyttää lukuisia ohjelmointikieliä kuten C#, Python, JavaScript, Java ja muuta. Olemme valinneet käyttää `openai` Python-kirjastoa, joten käytämme `pip` asennukseen.

```bash
pip install openai
```

### Luo resurssi

Sinun tulee suorittaa seuraavat vaiheet:

- Luo tili Azureen [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Hanki pääsy Azure OpenAI:hin. Mene osoitteeseen [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ja hae pääsyä.

  > [!NOTE]
  > Kirjoitushetkellä sinun täytyy hakea pääsyä Azure OpenAI:hin.

- Asenna Python <https://www.python.org/>
- Luo Azure OpenAI Service -resurssi. Katso tämä opas siitä, miten [luoda resurssi](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Sijainnin API-avain ja päätepiste

Tässä vaiheessa sinun täytyy kertoa `openai`-kirjastollesi, mitä API-avainta käyttää. Löytääksesi API-avaimesi, mene Azure OpenAI -resurssisi "Keys and Endpoint" -osioon ja kopioi arvo "Key 1".

![Avaimet ja päätepiste Azure Portalissa](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Nyt kun sinulla on tämä tieto kopioituna, ohjataan kirjastot käyttämään sitä.

> [!NOTE]
> On suositeltavaa pitää API-avaimesi erillään koodistasi. Voit tehdä sen käyttämällä ympäristömuuttujia.
>
> - Aseta ympäristömuuttuja `OPENAI_API_KEY` API-avaimeksesi.
>   `export OPENAI_API_KEY='sk-...'`

### Azure-konfiguraation asetus

Jos käytät Azure OpenAI:ta (nyt osa Microsoft Foundrya), näin asetat konfiguraation. Käytämme standardia `OpenAI`-asiakasta osoitettuna Azure OpenAI:n `/openai/v1/` -päätepisteeseen, joka toimii Responses API:n kanssa eikä vaadi `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Yllä asetamme seuraavat:

- `api_key`, tämä on Azure Portalin tai Microsoft Foundryn portaalin API-avain.
- `base_url`, tämä on Foundryn resurssipäätepiste, johon on lisätty `/openai/v1/`. Vakaa v1-päätepiste toimii sekä OpenAI:n että Azure OpenAI:n kanssa ilman `api_version`-hallintaa.

> [!NOTE] > `os.environ` lukee ympäristömuuttujia. Voit käyttää sitä lukemaan ympäristömuuttujia kuten `AZURE_OPENAI_API_KEY` ja `AZURE_OPENAI_ENDPOINT`. Aseta nämä muuttujat terminaalissasi tai käytä kirjastoa kuten `dotenv`.

## Tekstin generointi

Tekstin generointitapa on käyttää Responses APIa metodin `responses.create` kautta. Tässä esimerkki:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Yllä olevassa koodissa luomme vastauksen, annamme käytettävän mallin ja kehotteen. Sitten tulostamme generoitu teksti `response.output_text` kautta.

### Moni-vuoropuhelut

Responses API soveltuu sekä yksittäisen tekstin generointiin että moni-vuoropuheludra chatbotteihin - annat listan viestejä `input` muodossa käydäksesi keskustelua:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Lisätietoa tästä toiminnallisuudesta seuraavassa luvussa.

## Harjoitus - ensimmäinen tekstintuotantosovelluksesi

Nyt kun olemme oppineet, miten asettaa ja konfiguroida openai, on aika rakentaa ensimmäinen tekstintuotantosovelluksesi. Rakenna sovelluksesi noudattamalla näitä vaiheita:

1. Luo virtuaaliympäristö ja asenna openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jos käytät Windowsia, kirjoita `venv\Scripts\activate` komennon `source venv/bin/activate` sijaan.

   > [!NOTE]
   > Löydä Azure OpenAI -avaimesi menemällä osoitteeseen [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ja etsi `Open AI`, valitse sitten `Open AI resource` ja sitten `Keys and Endpoint` ja kopioi `Key 1` -arvo.

1. Luo _app.py_ -tiedosto ja lisää siihen seuraava koodi:

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
   > Jos käytät pelkkää OpenAI:ta (ei Azurea), käytä `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (ei `base_url`) ja anna mallin nimi kuten `gpt-5-mini` käyttämisen sijaan käyttöönotolle.

   Näet ulostulon, joka on tämän kaltainen:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Erilaiset kehotteet eri tarkoituksiin

Nyt olet nähnyt, miten generoida tekstiä kehotetta käyttäen. Sinulla on jopa käynnissä oleva ohjelma, jota voit muokata ja muuttaa tuottamaan erilaisia tekstityyppejä.

Kehotteita voidaan käyttää monenlaisiin tehtäviin. Esimerkiksi:

- **Tuottaa tyyppistä tekstiä**. Esimerkiksi voit tuottaa runon, kysymyksiä visaan jne.
- **Hakea tietoa**. Voit käyttää kehotteita etsimään tietoa kuten seuraavassa esimerkissä 'Mitä CORS tarkoittaa web-kehityksessä?'.
- **Tuottaa koodia**. Voit käyttää kehotteita tuottamaan koodia, esimerkiksi kehittää säännöllisen lausekkeen sähköpostien validoimiseksi tai mikset tuottaisi koko ohjelmaa, kuten web-sovellusta?

## Käytännöllisempi käyttötapaus: reseptigeneraattori

Kuvittele, että sinulla on ainekset kotona ja haluat kokata jotain. Tarvitset siihen reseptin. Reseptien etsimiseen voit käyttää hakukonetta tai LLM:ää.

Voisit kirjoittaa kehotteen näin:

> "Näytä minulle 5 reseptiä, jotka käyttävät seuraavia aineksia: kana, perunat ja porkkanat. Listaa jokaisen reseptin ainekset."

Annat yllä olevan kehotteen, saatat saada vastaavan vastauksen:

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

Tämä tulos on erinomainen, tiedän mitä kokkaan. Tässä vaiheessa hyödyllisiä parannuksia voivat olla:

- Suodattaa pois aineksia, joista en pidä tai joille olen allerginen.
- Tuottaa ostoslista, jos minulla ei ole kaikkia aineksia kotona.

Seuraavissa tapauksissa lisätään toinen kehotte stimuloimaan näitä tarpeita:

> "Poista resepteistä valkosipuli, koska olen sille allerginen, ja korvaa muulla. Lisäksi laadi ostoslista resepteille, ottaen huomioon että minulla on jo kanaa, perunoita ja porkkanoita kotona."

Nyt sinulla on uusi vastaus, nimittäin:

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

Nämä ovat viisi reseptiäsi ilman valkosipulia ja sinulla on myös ostoslista ottaen huomioon mitä sinulla on jo kotona.

## Harjoitus - rakenna reseptigeneraattori

Nyt kun olemme esittäneet esimerkin, kirjoitetaan koodi, joka vastaa tätä tilannetta. Toimi seuraavasti:

1. Käytä olemassa olevaa _app.py_-tiedostoa lähtökohtana
1. Etsi `prompt`-muuttuja ja muuta sen koodi seuraavaan:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jos suoritat nyt koodin, näet tuloksen, joka on samankaltainen kuin:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > HUOMAUTUS: LLM:si on epädeterministinen, joten saatat saada erilaisia tuloksia joka kerta kun ajat ohjelman.

   Hienoa, katsotaan miten voimme parantaa asioita. Parantaaksemme haluamme varmistaa, että koodi on joustava, joten voidaan vaihtaa ainesosia ja reseptien määrää.

1. Muutetaan koodia seuraavasti:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Koodin testaus voisi näyttää tältä:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Paranna lisäämällä suodatin ja ostoslista

Meillä on nyt toimiva sovellus, joka tuottaa reseptejä ja on joustava, koska se perustuu käyttäjän antamiin tietoihin, sekä reseptien lukumäärä että käytetyt ainekset.

Lisätäksemme parannuksia haluamme lisätä seuraavat:

- **Suodata aineksia pois**. Haluamme voida suodattaa pois aineksia, joista emme pidä tai joille olemme allergisia. Toteuttaaksemme tämän muutoksen voimme muokata olemassa olevaa kehoteamme ja lisätä suodatusehdon sen loppuun näin:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Yllä lisäämme `{filter}` kehotteen loppuun ja otamme vastaan suodatusarvon käyttäjältä.

  Esimerkkinä ohjelman suorittamisesta voi nyt olla:

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

  Kuten näet, kaikki reseptit, joissa on maitoa, on suodatettu pois. Mutta jos olet laktoosi-intolerantti, saatat haluta suodattaa myös juustoa sisältävät reseptit pois, joten tarpeen on olla tarkka.

- **Tuottaa ostoslista**. Haluamme luoda ostoslistan ottaen huomioon, mitä meillä jo on kotona.

  Tämän toiminnallisuuden voisimme ratkaista yhdellä kehotteella tai jakaa kahteen osaan. Kokeillaan jälkimmäistä lähestymistapaa. Lisätään toinen kehotte, mutta sen toimimiseksi meidän täytyy liittää edellisen kehotteen tulos kontekstiksi uudelle kehotteelle.

  Etsi koodista kohta, jossa tulostetaan ensimmäisen kehotteen tulos, ja lisää sen alle seuraava koodi:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Huomaa seuraavat asiat:

  1. Rakennamme uuden kehotteen lisäämällä edellisen kehotteen tuloksen uuteen kehoteeseen:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Teemme uuden pyynnön, mutta otamme myös huomioon ensimmäisestä kehotteesta pyydetyn token-määrän, joten tällä kertaa sanomme `max_output_tokens` olevan 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Ajaessamme tätä koodia saamme nyt seuraavan tuloksen:

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

Tämä, mitä meillä on tähän mennessä, on toimiva koodi, mutta on joitakin säätöjä, joita meidän tulisi tehdä parantaaksemme asioita edelleen. Joitakin asioita, jotka meidän tulisi tehdä, ovat:

- **Erottele salaisuudet koodista**, kuten API-avain. Salaisuudet eivät kuulu koodiin ja ne tulisi säilyttää turvallisessa paikassa. Erotellaksemme salaisuudet koodista, voimme käyttää ympäristömuuttujia ja kirjastoja kuten `python-dotenv` ladataksemme ne tiedostosta. Näin se näyttäisi koodissa:

  1. Luo `.env` tiedosto seuraavalla sisällöllä:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Huomio, Azure OpenAI:lle Microsoft Foundryssa sinun tulee asettaa seuraavat ympäristömuuttujat:

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

- **Sana token-pituudesta**. Meidän tulisi harkita, kuinka monta tokenia tarvitsemme halutun tekstin tuottamiseen. Tokenit maksavat rahaa, joten missä mahdollista, meidän tulisi olla taloudellisia käyttämämme tokenien määrän suhteen. Voimmeko esimerkiksi muotoilla kehotteen siten, että voimme käyttää vähemmän tokeneita?

  Muuttaaksesi käytettyjä tokeneita, voit käyttää `max_output_tokens` parametria. Esimerkiksi jos haluat käyttää 100 tokenia, tekisit näin:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Kokeile lämpötilaa**. Lämpötila on asia, josta emme ole vielä puhuneet, mutta se on tärkeä yhteys ohjelmamme suoritukseen. Mitä korkeampi lämpötilan arvo, sitä satunnaisempi lopputulos on. Vastaavasti mitä matalampi lämpötilan arvo, sitä ennustettavampi lopputulos on. Pohdi haluatko vaihtelua lopputuloksessasi vai et.

  Muuttaaksesi lämpötilaa, voit käyttää `temperature` parametria. Esimerkiksi jos haluat käyttää lämpötilaa 0.5, tekisit näin:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Huomioi, mitä lähempänä 1.0, sitä monipuolisempi lopputulos.

- **Päättelymalleissa ei käytetä `temperature`**. Tämä on tärkeä muutos vuodelle 2026. Nykyiset, ei-vanhentuneet mallit Microsoft Foundryssa ovat **päättelymalleja** (GPT-5 perhe, o-sarja) - ja ne **eivät tue `temperature` tai `top_p`** (eikä `max_tokens`; käytä `max_output_tokens`). Jos lähetät `temperature` osoitteeseen `gpt-5-mini` saat virheilmoituksen "parametri ei ole tuettu". Jotta voisit kokeilla edellä mainittua lämpötilaesimerkkiä, osoita se mallille, joka edelleen tukee otantasäätöjä - esimerkiksi avoimelle **Llama** mallille kuten `Llama-3.3-70B-Instruct` [Microsoft Foundry mallikatalogista](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), jota kutsutaan Foundry Models / Azure AI Inference -päätepisteen kautta (sama tapa kuin `githubmodels-*` esimerkeissä). GPT-5 kaltaisissa päättelymalleissa ohjaat lopputulosta eri tavalla:
  - **Kehoteinsinöörityö** - selkeät ohjeet, esimerkit ja rakenteellinen tulos (katso oppitunti [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) tekevät sen työn, mitä otanta-asetukset tekivät aiemmin.
  - **Päättelysäätimet** - parametrit kuten päättelyponnistelu/pitkäpiirteisyys tasapainottavat päättelyn syvyyden latenssia ja kustannuksia vastaan.

  Lyhyesti: `temperature`/`top_p` ovat edelleen voimassa monissa malleissa (Llama, Mistral, Phi ja GPT-4.x perhe - vaikka GPT-4.x on vanhentumassa), mutta suunta on kohti kehoteinsinöörityötä + päättelysäätimiä päättelymalleissa kuten GPT-5.

## Tehtävä

Tässä tehtävässä voit valita, mitä rakennat.

Tässä muutamia ehdotuksia:

- Säädä reseptigeneraattori-sovellusta parantaaksesi sitä edelleen. Kokeile lämpötila-arvoja ja kehotteita nähdäksesi, mitä saat aikaan.
- Rakenna "opiskelukaveri". Tämän sovelluksen tulisi pystyä vastaamaan kysymyksiin aiheesta, esimerkiksi Pythonista. Voit käyttää kehotteita, kuten "Mikä on tietty aihe Pythonissa?", tai kehotetta, joka sanoo, näytä minulle koodi tietystä aiheesta jne.
- Historia-botti, saa historia elämään, käskytä bottia esittämään tiettyä historiallista hahmoa ja kysy sille kysymyksiä sen elämästä ja ajoista.

## Ratkaisu

### Opiskelukaveri

Alla on aloituskehote, kokeile miten voit käyttää sitä ja säätää sitä mieleiseksesi.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historia-botti

Tässä joitakin kehotteita, joita voisit käyttää:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Tiedontarkistus

Mitä käsite lämpötila tekee?

1. Se säätelee, kuinka satunnainen lopputulos on.
1. Se säätelee, kuinka suuri vastaus on.
1. Se säätelee, kuinka monta tokenia käytetään.

## 🚀 Haaste

Työskennellessäsi tehtävän parissa, kokeile vaihdella lämpötilaa, kokeile asettaa se arvoihin 0, 0.5 ja 1. Muista, että 0 on vähiten vaihteleva ja 1 eniten. Mikä arvo toimii parhaiten sovelluksessasi?

## Hienoa työtä! Jatka oppimista

Tämän oppitunnin jälkeen tutustu [Generatiivisen tekoälyn oppimiskokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) jatkaaksesi generatiivisen tekoälyn osaamisesi kehittämistä!

Siirry oppitunnille 7, jossa katsomme miten [rakentaa keskustelusovelluksia](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->