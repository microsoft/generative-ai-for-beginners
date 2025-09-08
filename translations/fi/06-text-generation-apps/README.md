<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T12:01:23+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "fi"
}
-->
# Tekstintuotantosovellusten rakentaminen

[![Tekstintuotantosovellusten rakentaminen](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.fi.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Olet tähän mennessä nähnyt tämän opetussuunnitelman kautta, että on olemassa keskeisiä käsitteitä kuten promptit ja jopa kokonainen ala nimeltä "prompt engineering". Monet työkalut, joiden kanssa voit olla vuorovaikutuksessa, kuten ChatGPT, Office 365, Microsoft Power Platform ja muut, tukevat sinua käyttämään promptteja jonkin saavuttamiseksi.

Jotta voit lisätä tällaisen kokemuksen sovellukseen, sinun täytyy ymmärtää käsitteitä kuten promptit, completions ja valita kirjasto, jonka kanssa työskennellä. Juuri tämän opit tässä luvussa.

## Johdanto

Tässä luvussa sinä:

- Opit openai-kirjastosta ja sen keskeisistä käsitteistä.
- Rakennat tekstintuotantosovelluksen käyttäen openai-kirjastoa.
- Ymmärrät, miten käyttää käsitteitä kuten prompt, temperature ja tokens tekstintuotantosovelluksen rakentamiseen.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Selittää, mitä tekstintuotantosovellus on.
- Rakentaa tekstintuotantosovelluksen käyttäen openai-kirjastoa.
- Määrittää sovelluksesi käyttämään enemmän tai vähemmän tokeneita ja myös muuttaa temperature-arvoa vaihtelevamman tuloksen saamiseksi.

## Mikä on tekstintuotantosovellus?

Normaalisti kun rakennat sovelluksen, siinä on jonkinlainen käyttöliittymä, kuten seuraavat:

- Komentorivipohjainen. Konsolisovellukset ovat tyypillisiä sovelluksia, joissa kirjoitat komennon ja se suorittaa tehtävän. Esimerkiksi `git` on komentorivipohjainen sovellus.
- Käyttöliittymä (UI). Joissakin sovelluksissa on graafinen käyttöliittymä (GUI), jossa klikkaat painikkeita, syötät tekstiä, valitset vaihtoehtoja ja muuta.

### Konsoli- ja UI-sovellukset ovat rajallisia

Vertaa sitä komentorivipohjaiseen sovellukseen, jossa kirjoitat komennon:

- **Se on rajallinen**. Et voi kirjoittaa mitä tahansa komentoa, vain niitä, joita sovellus tukee.
- **Kielikohtainen**. Jotkut sovellukset tukevat monia kieliä, mutta oletuksena sovellus on rakennettu tietylle kielelle, vaikka voit lisätä lisää kielitukea.

### Tekstintuotantosovellusten edut

Miten tekstintuotantosovellus sitten eroaa?

Tekstintuotantosovelluksessa sinulla on enemmän joustavuutta, et ole sidottu tiettyihin komentoihin tai tiettyyn syötekieleen. Sen sijaan voit käyttää luonnollista kieltä vuorovaikutukseen sovelluksen kanssa. Toinen etu on, että koska olet vuorovaikutuksessa tietolähteen kanssa, joka on koulutettu valtavalla tietomäärällä, perinteinen sovellus saattaa olla rajoittunut siihen, mitä tietokannassa on.

### Mitä voin rakentaa tekstintuotantosovelluksella?

Voit rakentaa monenlaisia asioita. Esimerkiksi:

- **Chatbotin**. Chatbot, joka vastaa kysymyksiin aiheista, kuten yrityksestäsi ja sen tuotteista, voisi olla hyvä ratkaisu.
- **Avustajan**. LLM:t ovat erinomaisia esimerkiksi tekstin tiivistämisessä, tekstistä saatavien oivallusten löytämisessä, tekstin tuottamisessa kuten ansioluetteloissa ja muussa.
- **Koodiavustajan**. Käyttämästäsi kielimallista riippuen voit rakentaa koodiavustajan, joka auttaa sinua kirjoittamaan koodia. Esimerkiksi voit käyttää tuotteita kuten GitHub Copilot tai ChatGPT auttamaan koodin kirjoittamisessa.

## Miten pääsen alkuun?

Sinun täytyy löytää tapa integroitua LLM:ään, mikä yleensä tarkoittaa kahta lähestymistapaa:

- Käytä API:a. Tässä rakennat web-pyyntöjä prompttisi kanssa ja saat takaisin generoituja tekstejä.
- Käytä kirjastoa. Kirjastot kapseloivat API-kutsut ja tekevät niistä helpompia käyttää.

## Kirjastot/SDK:t

On muutamia tunnettuja kirjastoja LLM:ien kanssa työskentelyyn, kuten:

- **openai**, tämä kirjasto tekee malliin yhdistämisestä ja prompttien lähettämisestä helppoa.

Sitten on kirjastoja, jotka toimivat korkeammalla tasolla, kuten:

- **Langchain**. Langchain on tunnettu ja tukee Pythonia.
- **Semantic Kernel**. Semantic Kernel on Microsoftin kirjasto, joka tukee kieliä C#, Python ja Java.

## Ensimmäinen sovellus käyttäen openai-kirjastoa

Katsotaan, miten voimme rakentaa ensimmäisen sovelluksemme, mitä kirjastoja tarvitsemme, kuinka paljon vaaditaan ja niin edelleen.

### Asenna openai

On monia kirjastoja OpenAI:n tai Azure OpenAI:n kanssa työskentelyyn. Voit käyttää useita ohjelmointikieliä kuten C#, Python, JavaScript, Java ja muita. Olemme valinneet käyttää `openai` Python-kirjastoa, joten käytämme `pip`-komentoa sen asentamiseen.

```bash
pip install openai
```

### Luo resurssi

Sinun täytyy suorittaa seuraavat vaiheet:

- Luo tili Azureen osoitteessa [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Hanki pääsy Azure OpenAI:hin. Mene osoitteeseen [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ja pyydä pääsyä.

  > [!NOTE]
  > Kirjoitushetkellä sinun täytyy hakea pääsyä Azure OpenAI:hin.

- Asenna Python <https://www.python.org/>
- Luo Azure OpenAI Service -resurssi. Katso ohjeet resurssin [luomiseen](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Etsi API-avain ja päätepiste

Tässä vaiheessa sinun täytyy kertoa `openai`-kirjastolle, mitä API-avainta käyttää. Löytääksesi API-avaimesi, mene Azure OpenAI -resurssisi "Keys and Endpoint" -osioon ja kopioi "Key 1" -arvo.

![Keys and Endpoint -resurssinäkymä Azure-portaalissa](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Kun sinulla on tämä tieto kopioituna, ohjataan kirjastot käyttämään sitä.

> [!NOTE]
> On suositeltavaa erottaa API-avain koodista. Voit tehdä tämän käyttämällä ympäristömuuttujia.
>
> - Aseta ympäristömuuttuja `OPENAI_API_KEY` API-avaimellesi.
>   `export OPENAI_API_KEY='sk-...'`

### Azure-konfiguraation asetus

Jos käytät Azure OpenAI:ta, näin asetat konfiguraation:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Yllä asetamme seuraavat:

- `api_type` arvoksi `azure`. Tämä kertoo kirjastolle, että käytetään Azure OpenAI:ta eikä OpenAI:ta.
- `api_key`, tämä on API-avaimesi, jonka löysit Azure-portaalista.
- `api_version`, tämä on API:n versio, jota haluat käyttää. Kirjoitushetkellä uusin versio on `2023-05-15`.
- `api_base`, tämä on API:n päätepiste. Löydät sen Azure-portaalista API-avaimen vierestä.

> [!NOTE] > `os.getenv` on funktio, joka lukee ympäristömuuttujia. Voit käyttää sitä lukemaan ympäristömuuttujia kuten `OPENAI_API_KEY` ja `API_BASE`. Aseta nämä ympäristömuuttujat terminaalissasi tai käyttämällä kirjastoa kuten `dotenv`.

## Tekstin generointi

Tekstin generointiin käytetään `Completion`-luokkaa. Tässä esimerkki:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

Yllä olevassa koodissa luomme completion-olion ja annamme mallin, jota haluamme käyttää, sekä promptin. Sitten tulostamme generoitu tekstin.

### Chat completionit

Tähän asti olet nähnyt, miten käytämme `Completion`-luokkaa tekstin generointiin. Mutta on olemassa toinen luokka nimeltä `ChatCompletion`, joka sopii paremmin chatbotteihin. Tässä esimerkki sen käytöstä:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Lisää tästä toiminnallisuudesta seuraavassa luvussa.

## Harjoitus – ensimmäinen tekstintuotantosovelluksesi

Nyt kun olemme oppineet, miten openai asetetaan ja konfiguroidaan, on aika rakentaa ensimmäinen tekstintuotantosovelluksesi. Noudata näitä ohjeita:

1. Luo virtuaaliympäristö ja asenna openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jos käytät Windowsia, kirjoita `venv\Scripts\activate` sen sijaan, että käyttäisit `source venv/bin/activate`.

   > [!NOTE]
   > Löydä Azure OpenAI -avaimesi menemällä osoitteeseen [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), hae `Open AI`, valitse `Open AI resource` ja sitten `Keys and Endpoint` ja kopioi `Key 1` -arvo.

1. Luo tiedosto nimeltä _app.py_ ja lisää siihen seuraava koodi:

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
   > Jos käytät Azure OpenAI:ta, sinun täytyy asettaa `api_type` arvoksi `azure` ja `api_key` Azure OpenAI -avaimeksi.

   Näet tulosteen, joka näyttää suunnilleen tältä:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Eri tyyppisiä promptteja eri tarkoituksiin

Nyt olet nähnyt, miten tekstiä generoidaan promptin avulla. Sinulla on jopa ohjelma käynnissä, jota voit muokata ja muuttaa tuottamaan erilaisia tekstityyppejä.

Prompteja voi käyttää monenlaisiin tehtäviin. Esimerkiksi:

- **Tuottaa tietyn tyyppistä tekstiä**. Voit esimerkiksi generoida runon, kysymyksiä tietovisaasi varten jne.
- **Hakea tietoa**. Voit käyttää promptteja tiedon etsimiseen, kuten esimerkissä 'Mitä CORS tarkoittaa web-kehityksessä?'.
- **Generoi koodia**. Voit käyttää promptteja koodin generointiin, esimerkiksi luoda säännöllisen lausekkeen sähköpostien validointiin tai miksei generoida kokonainen ohjelma, kuten web-sovellus?

## Käytännöllisempi esimerkki: reseptigeneraattori

Kuvittele, että sinulla on kotona aineksia ja haluat kokata jotain. Tarvitset siihen reseptin. Reseptien etsimiseen voit käyttää hakukonetta tai voit käyttää LLM:ää.

Voisit kirjoittaa promptin näin:

> "Näytä minulle 5 reseptiä, joissa on seuraavat ainekset: kana, perunat ja porkkanat. Listaa jokaisen reseptin kaikki käytetyt ainekset."

Tämän promptin perusteella saatat saada vastauksen, joka näyttää tältä:

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

- Suodattaa pois ainekset, joista en pidä tai joille olen allerginen.
- Tuottaa ostoslista, jos minulla ei ole kaikkia aineksia kotona.

Edellisiin tapauksiin lisätään lisäpromptti:

> "Poista resepteistä valkosipuli, koska olen allerginen, ja korvaa se jollain muulla. Laadi myös ostoslista resepteille, ottaen huomioon, että minulla on jo kana, perunat ja porkkanat kotona."

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

Siinä ovat viisi reseptiä ilman valkosipulia ja lisäksi sinulla on ostoslista ottaen huomioon, mitä sinulla jo on kotona.

## Harjoitus – rakenna reseptigeneraattori

Nyt kun olemme käyneet läpi esimerkin, kirjoitetaan koodi vastaamaan tätä tilannetta. Toimi seuraavasti:

1. Käytä olemassa olevaa _app.py_-tiedostoa lähtökohtana.
1. Etsi `prompt`-muuttuja ja muuta sen koodi seuraavaksi:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jos ajat nyt koodin, näet tuloksen, joka näyttää suunnilleen tältä:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, LLM:si on epädeterministinen, joten saatat saada eri tuloksia joka kerta, kun ajat ohjelman.

   Hienoa, katsotaan miten voimme parantaa asioita. Parantaaksemme haluamme varmistaa, että koodi on joustava, jotta ainesosat ja reseptien määrä voidaan muuttaa ja parantaa.

1. Muutetaan koodia seuraavasti:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testiajo voisi näyttää tältä:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Paranna lisäämällä suodatin ja ostoslista

Meillä on nyt toimiva sovellus, joka pystyy tuottamaan reseptejä ja on joustava, koska se perustuu käyttäjän syötteisiin, sekä reseptien määrään että käytettyihin aineksiin.

Parantaaksemme sitä haluamme lisätä seuraavat:

- **Suodata pois ainekset**. Haluamme pystyä suodattamaan pois aineksia, joista emme pidä tai joille olemme allergisia. Tämän muutoksen tekemiseksi voimme muokata olemassa olevaa prompttia ja lisätä suodatusehdon sen loppuun näin:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Yllä lisäämme `{filter}` promptin loppuun ja otamme myös käyttäjän antaman suodatusarvon talteen.

  Esimerkkisyöte ohjelman ajosta voisi nyt näyttää tältä:

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

  Kuten näet, kaikki reseptit, joissa on maitoa, on suodatettu pois. Mutta jos olet laktoosi-intolerantti, saatat haluta suodattaa myös juustoa sisältävät reseptit, joten on tärkeää olla selkeä.

- **Tuota ostoslista**. Haluamme tuottaa ostoslistan ottaen huomioon, mitä meillä jo on kotona.

  Tätä toimintoa varten voisimme yrittää ratkaista kaiken yhdellä promptilla tai jakaa sen kahteen promptiin. Kokeillaan jälkimmäistä lähestymistapaa. Tässä ehdotamme lisäpromptin lisäämistä, mutta sen toimimiseksi meidän täytyy lisätä edellisen promptin tulos kontekstiksi seuraavaan promptiin.

  Etsi koodista kohta, jossa tulostetaan ensimmäisen promptin tulos, ja lisää seuraava koodi sen alle:

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

  Huomioi seuraavat:

  1. Rakennamme uuden promptin lisäämällä ensimmäisen promptin tuloksen uuteen promptiin:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
  1. Teemme uuden pyynnön, mutta otamme myös huomioon ensimmäisessä kehotteessa pyytämämme tokenien määrän, joten tällä kertaa asetamme `max_tokens` arvoksi 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Kun kokeilemme tätä koodia, saamme seuraavan tuloksen:

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

Tähän mennessä meillä on toimiva koodi, mutta on joitakin säätöjä, joilla voimme parantaa sitä entisestään. Joitakin asioita, jotka meidän tulisi tehdä, ovat:

- **Erottele salaisuudet koodista**, kuten API-avain. Salaisuudet eivät kuulu koodiin, vaan ne tulisi säilyttää turvallisessa paikassa. Erotellaksemme salaisuudet koodista, voimme käyttää ympäristömuuttujia ja kirjastoja kuten `python-dotenv` lataamaan ne tiedostosta. Näin se näyttäisi koodissa:

  1. Luo `.env`-tiedosto, jonka sisältö on seuraava:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> Huomaa, että Azuren kanssa sinun täytyy asettaa seuraavat ympäristömuuttujat:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     Koodissa lataat ympäristömuuttujat näin:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Sana token-pituudesta**. Meidän tulisi miettiä, kuinka monta tokenia tarvitsemme halutun tekstin tuottamiseen. Tokenit maksavat, joten missä mahdollista, meidän kannattaa olla taloudellisia tokenien käytössä. Voisimmeko esimerkiksi muotoilla kehotteen niin, että voimme käyttää vähemmän tokeneita?

  Tokenien määrää voit muuttaa `max_tokens`-parametrilla. Esimerkiksi, jos haluat käyttää 100 tokenia, teet näin:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Kokeile lämpötilaa**. Lämpötila on asia, jota emme ole vielä maininneet, mutta se on tärkeä konteksti ohjelmamme toiminnalle. Mitä korkeampi lämpötila-arvo, sitä satunnaisempi tulos on. Vastaavasti mitä matalampi lämpötila-arvo, sitä ennustettavampi tulos on. Mieti haluatko vaihtelua tulokseesi vai et.

  Lämpötilaa voit muuttaa `temperature`-parametrilla. Esimerkiksi, jos haluat käyttää lämpötilaa 0.5, teet näin:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Huomaa, mitä lähempänä arvo on 1.0, sitä monipuolisempi tulos on.

## Tehtävä

Tässä tehtävässä voit valita, mitä rakennat.

Tässä muutama ehdotus:

- Säädä reseptigeneraattori-sovellusta parantaaksesi sitä entisestään. Kokeile lämpötila-arvoja ja kehotteita nähdäksesi, mitä saat aikaan.
- Rakenna "opiskelukaveri". Tämän sovelluksen tulisi pystyä vastaamaan kysymyksiin esimerkiksi Python-aiheesta. Voisit käyttää kehotteita kuten "Mikä on tietty aihe Pythonissa?" tai kehotetta, joka pyytää näyttämään koodia tietystä aiheesta.
- Historia-botti, tuo historia eloon, ohjeista bottia esittämään tietty historiallinen hahmo ja kysy siltä kysymyksiä sen elämästä ja ajasta.

## Ratkaisu

### Opiskelukaveri

Alla on aloituskehotus, katso miten voit käyttää sitä ja muokata sitä mieleiseksesi.

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

## Tietovisa

Mitä lämpötila-käsite tekee?

1. Se säätelee, kuinka satunnainen tulos on.
1. Se säätelee, kuinka suuri vastaus on.
1. Se säätelee, kuinka monta tokenia käytetään.

## 🚀 Haaste

Tehtävää tehdessäsi kokeile vaihdella lämpötilaa, aseta se arvoihin 0, 0.5 ja 1. Muista, että 0 on vähiten vaihteleva ja 1 eniten. Mikä arvo toimii parhaiten sovelluksessasi?

## Hienoa työtä! Jatka oppimista

Kun olet suorittanut tämän oppitunnin, tutustu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) -kokoelmaamme jatkaaksesi Generative AI -osaamisesi kehittämistä!

Siirry oppitunnille 7, jossa tarkastelemme, miten [rakentaa chat-sovelluksia](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.