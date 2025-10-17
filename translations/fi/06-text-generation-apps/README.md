<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-17T19:38:28+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "fi"
}
-->
# Tekstintuotantosovellusten rakentaminen

[![Tekstintuotantosovellusten rakentaminen](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.fi.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Tässä oppimateriaalissa olet jo tutustunut keskeisiin käsitteisiin, kuten kehotteisiin, ja jopa kokonaan uuteen alaan nimeltä "kehotteiden suunnittelu". Monet työkalut, kuten ChatGPT, Office 365, Microsoft Power Platform ja muut, tukevat kehotteiden käyttöä jonkin tehtävän suorittamiseksi.

Jos haluat lisätä tällaisen kokemuksen sovellukseesi, sinun täytyy ymmärtää käsitteet, kuten kehotteet, tuotokset ja valita sopiva kirjasto työhön. Juuri näitä asioita opit tässä luvussa.

## Johdanto

Tässä luvussa opit:

- openai-kirjastosta ja sen keskeisistä käsitteistä.
- Tekstintuotantosovelluksen rakentamisesta openai-kirjaston avulla.
- Kuinka käyttää käsitteitä, kuten kehotteet, lämpötila ja tokenit, tekstintuotantosovelluksen rakentamiseen.

## Oppimistavoitteet

Tämän oppitunnin lopussa osaat:

- Selittää, mikä tekstintuotantosovellus on.
- Rakentaa tekstintuotantosovelluksen openai-kirjaston avulla.
- Konfiguroida sovelluksesi käyttämään enemmän tai vähemmän tokeneita ja muuttaa lämpötilaa vaihtelevan lopputuloksen saavuttamiseksi.

## Mikä on tekstintuotantosovellus?

Yleensä sovelluksella on jonkinlainen käyttöliittymä, kuten seuraavat:

- Komentopohjainen. Konsolisovellukset ovat tyypillisiä sovelluksia, joissa kirjoitat komennon ja se suorittaa tehtävän. Esimerkiksi `git` on komentopohjainen sovellus.
- Käyttöliittymä (UI). Joillakin sovelluksilla on graafinen käyttöliittymä (GUI), jossa voit klikata painikkeita, syöttää tekstiä, valita vaihtoehtoja ja paljon muuta.

### Konsoli- ja käyttöliittymäsovellusten rajoitukset

Vertaa komentopohjaiseen sovellukseen, jossa kirjoitat komennon:

- **Se on rajoitettu**. Et voi kirjoittaa mitä tahansa komentoa, vain ne, joita sovellus tukee.
- **Kielikohtainen**. Jotkut sovellukset tukevat monia kieliä, mutta oletuksena sovellus on rakennettu tietylle kielelle, vaikka voit lisätä kielitukea.

### Tekstintuotantosovellusten edut

Miten tekstintuotantosovellus eroaa?

Tekstintuotantosovelluksessa sinulla on enemmän joustavuutta, et ole rajoitettu tiettyihin komentoihin tai syöttökieleen. Sen sijaan voit käyttää luonnollista kieltä vuorovaikutukseen sovelluksen kanssa. Toinen etu on, että olet jo vuorovaikutuksessa tietolähteen kanssa, joka on koulutettu laajalla tietokorpuksella, kun taas perinteinen sovellus saattaa olla rajoitettu tietokannan sisältöön.

### Mitä voin rakentaa tekstintuotantosovelluksella?

Voit rakentaa monenlaisia asioita. Esimerkiksi:

- **Chatbot**. Chatbot, joka vastaa kysymyksiin aiheista, kuten yrityksesi ja sen tuotteet, voisi olla hyvä valinta.
- **Avustaja**. LLM:t ovat erinomaisia tekstin tiivistämisessä, tekstistä oivallusten saamisessa, tekstin tuottamisessa, kuten ansioluetteloiden luomisessa, ja paljon muussa.
- **Koodiavustaja**. Riippuen käyttämästäsi kielimallista, voit rakentaa koodiavustajan, joka auttaa sinua kirjoittamaan koodia. Esimerkiksi voit käyttää tuotetta, kuten GitHub Copilotia, sekä ChatGPT:tä koodin kirjoittamiseen.

## Kuinka pääsen alkuun?

Sinun täytyy löytää tapa integroitua LLM:ään, mikä yleensä sisältää seuraavat kaksi lähestymistapaa:

- Käytä API:a. Tässä rakennat verkkopyyntöjä kehotteesi kanssa ja saat takaisin tuotetun tekstin.
- Käytä kirjastoa. Kirjastot auttavat kapseloimaan API-kutsut ja tekevät niiden käytöstä helpompaa.

## Kirjastot/SDK:t

On olemassa muutamia tunnettuja kirjastoja LLM:ien kanssa työskentelyyn, kuten:

- **openai**, tämä kirjasto tekee mallisi yhdistämisen ja kehotteiden lähettämisen helpoksi.

Sitten on kirjastoja, jotka toimivat korkeammalla tasolla, kuten:

- **Langchain**. Langchain on hyvin tunnettu ja tukee Pythonia.
- **Semantic Kernel**. Semantic Kernel on Microsoftin kirjasto, joka tukee kieliä C#, Python ja Java.

## Ensimmäinen sovellus openai-kirjastolla

Katsotaan, kuinka voimme rakentaa ensimmäisen sovelluksemme, mitä kirjastoja tarvitsemme, kuinka paljon vaaditaan ja niin edelleen.

### Asenna openai

On olemassa monia kirjastoja OpenAI:n tai Azure OpenAI:n kanssa työskentelyyn. On mahdollista käyttää myös lukuisia ohjelmointikieliä, kuten C#, Python, JavaScript, Java ja muita. Olemme valinneet käyttää `openai` Python-kirjastoa, joten käytämme `pip`-työkalua sen asentamiseen.

```bash
pip install openai
```

### Luo resurssi

Sinun täytyy suorittaa seuraavat vaiheet:

- Luo tili Azuren sivustolla [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Hanki pääsy Azure OpenAI:hin. Siirry [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ja pyydä pääsyä.

  > [!NOTE]
  > Kirjoitushetkellä sinun täytyy hakea pääsyä Azure OpenAI:hin.

- Asenna Python <https://www.python.org/>
- Luo Azure OpenAI Service -resurssi. Katso tämä opas [resurssin luomiseen](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Etsi API-avain ja päätepiste

Tässä vaiheessa sinun täytyy kertoa `openai`-kirjastolle, mitä API-avainta käyttää. Löytääksesi API-avaimesi, siirry Azure OpenAI -resurssisi "Keys and Endpoint" -osioon ja kopioi "Key 1" -arvo.

![Keys and Endpoint -resurssinäkymä Azure-portaalissa](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Kun olet kopioinut nämä tiedot, ohjeistetaan kirjastot käyttämään niitä.

> [!NOTE]
> On suositeltavaa erottaa API-avain koodistasi. Voit tehdä tämän käyttämällä ympäristömuuttujia.
>
> - Aseta ympäristömuuttuja `OPENAI_API_KEY` API-avaimeesi.
>   `export OPENAI_API_KEY='sk-...'`

### Konfiguroi Azure-asetukset

Jos käytät Azure OpenAI:ta, tässä on ohjeet konfigurointiin:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Yllä asetamme seuraavat:

- `api_type` arvoksi `azure`. Tämä kertoo kirjastolle, että käytetään Azure OpenAI:ta eikä OpenAI:ta.
- `api_key`, tämä on API-avaimesi, joka löytyy Azure-portaalista.
- `api_version`, tämä on API:n versio, jota haluat käyttää. Kirjoitushetkellä uusin versio on `2023-05-15`.
- `api_base`, tämä on API:n päätepiste. Löydät sen Azure-portaalista API-avaimesi vierestä.

> [!NOTE] > `os.getenv` on funktio, joka lukee ympäristömuuttujia. Voit käyttää sitä lukemaan ympäristömuuttujia, kuten `OPENAI_API_KEY` ja `API_BASE`. Aseta nämä ympäristömuuttujat terminaalissasi tai käyttämällä kirjastoa, kuten `dotenv`.

## Tekstin tuottaminen

Tekstiä tuotetaan käyttämällä `Completion`-luokkaa. Tässä esimerkki:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

Yllä olevassa koodissa luomme tuotoksen ja annamme mallin, jota haluamme käyttää, sekä kehotteen. Sitten tulostamme tuotetun tekstin.

### Chat-tuotokset

Tähän mennessä olemme käyttäneet `Completion`-luokkaa tekstin tuottamiseen. Mutta on olemassa toinen luokka nimeltä `ChatCompletion`, joka sopii paremmin chatbotteihin. Tässä esimerkki sen käytöstä:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Lisää tästä toiminnallisuudesta tulevassa luvussa.

## Harjoitus - ensimmäinen tekstintuotantosovellus

Nyt kun olemme oppineet, kuinka openai-kirjasto asetetaan ja konfiguroidaan, on aika rakentaa ensimmäinen tekstintuotantosovellus. Rakentaaksesi sovelluksen, seuraa näitä vaiheita:

1. Luo virtuaaliympäristö ja asenna openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Jos käytät Windowsia, kirjoita `venv\Scripts\activate` sen sijaan, että käyttäisit `source venv/bin/activate`.

   > [!NOTE]
   > Etsi Azure OpenAI -avaimesi siirtymällä [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ja etsimällä `Open AI` ja valitse `Open AI resource`, sitten valitse `Keys and Endpoint` ja kopioi `Key 1` -arvo.

1. Luo _app.py_-tiedosto ja lisää siihen seuraava koodi:

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
   > Jos käytät Azure OpenAI:ta, sinun täytyy asettaa `api_type` arvoksi `azure` ja asettaa `api_key` Azure OpenAI -avaimeesi.

   Sinun pitäisi nähdä seuraavanlainen tulos:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Erilaisia kehotteita eri tarkoituksiin

Nyt olet nähnyt, kuinka tekstiä voidaan tuottaa kehotteen avulla. Sinulla on jopa toimiva ohjelma, jota voit muokata ja muuttaa tuottamaan erilaista tekstiä.

Kehotteita voidaan käyttää monenlaisiin tehtäviin. Esimerkiksi:

- **Tuota tietyn tyyppistä tekstiä**. Voit esimerkiksi tuottaa runon, kysymyksiä tietovisaan jne.
- **Hae tietoa**. Voit käyttää kehotteita tiedon hakemiseen, kuten seuraavassa esimerkissä: 'Mitä CORS tarkoittaa web-kehityksessä?'.
- **Tuota koodia**. Voit käyttää kehotteita koodin tuottamiseen, esimerkiksi kehittääksesi sähköpostiosoitteiden validointiin käytettävän säännöllisen lausekkeen tai miksei tuottaaksesi kokonaisen ohjelman, kuten web-sovelluksen?

## Käytännöllisempi esimerkki: reseptigeneraattori

Kuvittele, että sinulla on kotona aineksia ja haluat valmistaa jotain. Tarvitset reseptin. Yksi tapa löytää reseptejä on käyttää hakukonetta, tai voit käyttää LLM:ää tähän.

Voisit kirjoittaa kehotteen seuraavasti:

> "Näytä 5 reseptiä ruokalajille, jossa käytetään seuraavia aineksia: kana, perunat ja porkkanat. Per resepti, listaa kaikki käytetyt ainekset."

Yllä olevan kehotteen perusteella saatat saada vastauksen, joka näyttää tältä:

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

Tämä lopputulos on loistava, tiedän mitä kokata. Tässä vaiheessa hyödyllisiä parannuksia voisivat olla:

- Poistaa ainekset, joista en pidä tai joille olen allerginen.
- Laatia ostoslista, jos minulla ei ole kaikkia aineksia kotona.

Näitä tapauksia varten voimme lisätä lisäkehotteen:

> "Poista reseptit, joissa on valkosipulia, koska olen allerginen, ja korvaa se jollain muulla. Laadi myös ostoslista resepteille, ottaen huomioon, että minulla on jo kanaa, perunoita ja porkkanoita kotona."

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

Siinä ovat viisi reseptiä, joissa ei mainita valkosipulia, ja sinulla on myös ostoslista, joka huomioi kotona jo olevat ainekset.

## Harjoitus - rakenna reseptigeneraattori

Nyt kun olemme käyneet läpi skenaarion, kirjoitetaan koodi, joka vastaa esitettyä skenaariota. Seuraa näitä vaiheita:

1. Käytä olemassa olevaa _app.py_-tiedostoa lähtökohtana.
1. Etsi `prompt`-muuttuja ja muuta sen koodi seuraavaksi:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Jos nyt suoritat koodin, sinun pitäisi nähdä tulos, joka näyttää tältä:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > HUOMIO, LLM on ei-deterministinen, joten saatat saada erilaisia tuloksia joka kerta, kun suoritat ohjelman.

   Hienoa, katsotaan, kuinka voimme parantaa asioita. Parantaaksemme asioita haluamme varmistaa, että koodi on joustava, jotta ainekset ja reseptien määrä voidaan muuttaa ja parantaa.

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

Meillä on nyt toimiva sovellus, joka pystyy tuottamaan reseptejä, ja se on joustava, koska se perustuu käyttäjän syötteisiin, sekä reseptien määrään että käytettyihin aineksiin.

Jotta voimme parantaa sitä, haluamme lisätä seuraavat:

- **Poista ainekset**. Haluamme pystyä poistamaan aineksia, joista emme pidä tai joille olemme allergisia. Tämän muutoksen saavuttamiseksi voimme muokata olemassa olevaa kehotetta ja lisätä suodatin ehdon sen loppuun, kuten seuraavasti:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Yllä lisäämme `{filter}` kehotteen loppuun ja otamme myös suodatinarvon käyttäjältä.

  Esimerkki ohjelman suorittamisesta voisi nyt näyttää tältä:

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

  Kuten näet, kaikki reseptit, joissa on maitoa, on suodatettu pois. Mutta jos olet laktoosi-intolerantti, saatat haluta suodattaa pois reseptit, joissa on juustoa, joten on tarpeen olla selkeä.

- **Laadi ostoslista**. Haluamme laatia ostoslistan, ottaen huomioon, mitä meillä jo on kotona.

  Tämän toiminnallisuuden osalta voisimme joko yrittää ratkaista kaiken yhdessä kehotteessa tai jakaa sen kahteen kehotteeseen. Kokeillaan jälkimmäistä lähestymistapaa. Tässä ehdotamme lisäkehotteen lisäämistä, mutta jotta se toimisi, meidän täytyy lisätä ensimmäisen kehotteen tulos kontekstiksi toiselle kehotteelle.

  Etsi koodista kohta, jossa ensimmäisen kehotteen tulos tulostetaan, ja lisää seuraava koodi sen alle:
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

  1. Rakennamme uuden kehotteen lisäämällä ensimmäisen kehotteen tuloksen uuteen kehotteeseen:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Teemme uuden pyynnön, mutta otamme myös huomioon ensimmäisessä kehotteessa pyydettyjen tokenien määrän, joten tällä kertaa asetamme `max_tokens` arvoksi 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Kun kokeilemme tätä koodia, päädymme seuraavaan tulokseen:

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

Tähän mennessä meillä on toimiva koodi, mutta on joitakin parannuksia, joita voisimme tehdä asioiden kehittämiseksi edelleen. Joitakin asioita, joita meidän tulisi tehdä, ovat:

- **Erottele salaisuudet koodista**, kuten API-avain. Salaisuudet eivät kuulu koodiin ja ne tulisi säilyttää turvallisessa paikassa. Salaisuuksien erottamiseksi koodista voimme käyttää ympäristömuuttujia ja kirjastoja, kuten `python-dotenv`, lataamaan ne tiedostosta. Näin se näyttäisi koodissa:

  1. Luo `.env`-tiedosto seuraavalla sisällöllä:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Huomaa, että Azurea varten sinun täytyy asettaa seuraavat ympäristömuuttujat:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     Koodissa lataisit ympäristömuuttujat seuraavasti:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Sana tokenien pituudesta**. Meidän tulisi harkita, kuinka monta tokenia tarvitsemme tekstin tuottamiseen. Tokenit maksavat rahaa, joten missä mahdollista, meidän tulisi pyrkiä käyttämään niitä taloudellisesti. Esimerkiksi, voimmeko muotoilla kehotteen niin, että voimme käyttää vähemmän tokeneita?

  Tokenien määrää voi muuttaa käyttämällä `max_tokens`-parametria. Esimerkiksi, jos haluat käyttää 100 tokenia, tekisit näin:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Kokeile lämpötilan säätämistä**. Lämpötila on asia, jota emme ole vielä maininneet, mutta se on tärkeä konteksti ohjelmamme toiminnalle. Mitä korkeampi lämpötila-arvo, sitä satunnaisempi tulos on. Vastaavasti mitä matalampi lämpötila-arvo, sitä ennustettavampi tulos on. Mieti, haluatko vaihtelua tuloksissasi vai et.

  Lämpötilaa voi muuttaa käyttämällä `temperature`-parametria. Esimerkiksi, jos haluat käyttää lämpötilaa 0.5, tekisit näin:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Huomaa, mitä lähempänä 1.0, sitä vaihtelevampi tulos.

## Tehtävä

Tässä tehtävässä voit valita, mitä haluat rakentaa.

Tässä joitakin ehdotuksia:

- Paranna reseptigeneraattorisovellusta edelleen. Kokeile lämpötila-arvoja ja kehotteita nähdäksesi, mitä saat aikaan.
- Rakenna "opiskelukaveri". Tämän sovelluksen tulisi pystyä vastaamaan kysymyksiin jostakin aiheesta, esimerkiksi Pythonista. Voit käyttää kehotteita, kuten "Mikä on tietty aihe Pythonissa?" tai "Näytä minulle koodi tietystä aiheesta" jne.
- Historia-botti, herätä historia eloon, ohjeista bottia esittämään tiettyä historiallista hahmoa ja kysy siltä kysymyksiä hänen elämästään ja ajastaan.

## Ratkaisu

### Opiskelukaveri

Alla on aloituskehotus, katso, miten voit käyttää sitä ja muokata sitä mieleiseksesi.

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

## Tietojen tarkistus

Mitä lämpötilan käsite tekee?

1. Se ohjaa, kuinka satunnainen tulos on.
1. Se ohjaa, kuinka suuri vastaus on.
1. Se ohjaa, kuinka monta tokenia käytetään.

## 🚀 Haaste

Työskennellessäsi tehtävän parissa, kokeile vaihdella lämpötilaa, kokeile asettaa se arvoihin 0, 0.5 ja 1. Muista, että 0 on vähiten vaihteleva ja 1 on eniten. Mikä arvo toimii parhaiten sovelluksessasi?

## Hienoa työtä! Jatka oppimista

Kun olet suorittanut tämän oppitunnin, tutustu [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) -kokoelmaan jatkaaksesi Generative AI -tietämyksesi kehittämistä!

Siirry oppituntiin 7, jossa tarkastelemme, kuinka [rakentaa chat-sovelluksia](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi katsoa ensisijaiseksi lähteeksi. Tärkeää tietoa varten suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.