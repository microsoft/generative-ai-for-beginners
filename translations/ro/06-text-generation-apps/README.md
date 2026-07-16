# Construirea Aplicațiilor de Generare a Textului

[![Construirea Aplicațiilor de Generare a Textului](../../../translated_images/ro/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Click pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

Până acum, ai văzut în cadrul acestui curriculum că există concepte de bază precum prompturile și chiar o disciplină întreagă numită „prompt engineering”. Multe instrumente cu care poți interacționa, cum ar fi ChatGPT, Office 365, Microsoft Power Platform și altele, te sprijină folosind prompturi pentru a realiza ceva.

Pentru a adăuga o astfel de experiență într-o aplicație, trebuie să înțelegi concepte precum prompturi, completări și să alegi o bibliotecă cu care să lucrezi. Exact asta vei învăța în acest capitol.

## Introducere

În acest capitol, vei:

- Învață despre biblioteca openai și conceptele sale de bază.
- Construiește o aplicație de generare a textului folosind openai.
- Înțelege cum să folosești concepte precum prompt, temperature și tokens pentru a construi o aplicație de generare a textului.

## Obiectivele de învățare

La finalul acestei lecții, vei putea:

- Explică ce este o aplicație de generare a textului.
- Construiește o aplicație de generare a textului folosind openai.
- Configurează-ți aplicația să folosească mai mulți sau mai puțini tokens și, de asemenea, să schimbe temperatura, pentru un rezultat variat.

## Ce este o aplicație de generare a textului?

De obicei, când construiești o aplicație, aceasta are un fel de interfață precum următoarea:

- Bazată pe comenzi. Aplicațiile de consolă sunt aplicații tipice unde tastezi o comandă și aceasta execută o sarcină. De exemplu, `git` este o aplicație bazată pe comandă.
- Interfața utilizator (UI). Unele aplicații au interfețe grafice (GUI) unde apeși butoane, introduci text, selectezi opțiuni și altele.

### Aplicațiile de consolă și UI sunt limitate

Compară cu o aplicație bazată pe comandă în care tastezi o comandă:

- **Este limitată**. Nu poți tasta orice comandă, ci doar pe cele suportate de aplicație.
- **Specifică limbajului**. Unele aplicații suportă multe limbi, dar în mod implicit aplicația este construită pentru un limbaj specific, chiar dacă poți adăuga suport pentru altele.

### Avantajele aplicațiilor de generare a textului

Deci, cu ce se diferențiază o aplicație de generare a textului?

Într-o aplicație de generare a textului, ai mai multă flexibilitate, nu ești limitat la un set de comenzi sau la un limbaj de intrare specific. În schimb, poți folosi limbaj natural pentru a interacționa cu aplicația. Un alt avantaj este că deja interacționezi cu o sursă de date care a fost antrenată pe un vast corpus de informații, pe când o aplicație tradițională poate fi limitată la ceea ce este în baza de date.

### Ce pot construi cu o aplicație de generare a textului?

Sunt multe lucruri pe care le poți construi. De exemplu:

- **Un chatbot**. Un chatbot care răspunde la întrebări despre subiecte precum compania ta și produsele sale ar putea fi o alegere bună.
- **Asistent**. Modelele LLM sunt grozave la lucruri precum rezumarea textului, obținerea de insight-uri din text, generarea de texte precum CV-uri și altele.
- **Asistent pentru cod**. În funcție de modelul de limbaj pe care îl folosești, poți construi un asistent care să te ajute să scrii cod. De exemplu, poți folosi un produs ca GitHub Copilot, precum și ChatGPT, pentru a te ajuta să scrii cod.

## Cum pot începe?

Ei bine, trebuie să găsești o cale să integrezi cu un LLM, ceea ce de obicei implică următoarele două abordări:

- Folosește o API. Aici construiești cereri web cu promptul tău și primești text generat înapoi.
- Folosește o bibliotecă. Bibliotecile ajută la încorporarea apelurilor API și fac utilizarea mai ușoară.

## Biblioteci/SDK-uri

Există câteva biblioteci cunoscute pentru lucrul cu LLM-uri, cum ar fi:

- **openai**, această bibliotecă face ușoară conectarea la modelul tău și trimiterea prompturilor.

Mai există biblioteci care operează la un nivel mai înalt, cum ar fi:

- **Langchain**. Langchain este bine cunoscut și suportă Python.
- **Semantic Kernel**. Semantic Kernel este o bibliotecă de la Microsoft ce suportă limbajele C#, Python și Java.

## Prima aplicație folosind openai

Să vedem cum putem construi prima noastră aplicație, ce biblioteci sunt necesare, cât e nevoie și așa mai departe.

### Instalează openai

Există multe biblioteci disponibile pentru interacțiunea cu OpenAI sau Azure OpenAI. Este posibil să folosești numeroase limbaje de programare precum C#, Python, JavaScript, Java și altele. Am ales să folosim biblioteca Python `openai`, deci vom folosi `pip` pentru instalare.

```bash
pip install openai
```

### Creează un resource

Trebuie să parcurgi următorii pași:

- Creează un cont pe Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obține acces la Azure OpenAI. Mergi la [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) și solicită acces.

  > [!NOTE]
  > La momentul scrierii, trebuie să aplici pentru acces la Azure OpenAI.

- Instalează Python <https://www.python.org/>
- Ai creat un resource Azure OpenAI Service. Vezi acest ghid pentru cum să [creezi un resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Găsește cheia API și endpoint-ul

În acest punct, trebuie să spui bibliotecii `openai` ce cheie API să folosească. Pentru a găsi cheia API, mergi în secțiunea „Keys and Endpoint” a resource-ului tău Azure OpenAI și copiază valoarea „Key 1”.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Acum că ai copiat această informație, să instruim bibliotecile să o folosească.

> [!NOTE]
> Merită să separi cheia API de codul tău. Poți face asta folosind variabile de mediu.
>
> - Setează variabila de mediu `OPENAI_API_KEY` la cheia ta API.
>   `export OPENAI_API_KEY='sk-...'`

### Configurare Azure

Dacă folosești Azure OpenAI (acum parte din Microsoft Foundry), iată cum faci configurarea. Folosim clientul standard `OpenAI` indicat către endpoint-ul Azure OpenAI `/openai/v1/`, care funcționează cu Responses API și nu necesită `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Mai sus setăm următoarele:

- `api_key`, care este cheia API găsită în portalul Azure sau portalul Microsoft Foundry.
- `base_url`, care este endpoint-ul resource-ului Foundry cu `/openai/v1/` adăugat la final. Endpoint-ul stabil v1 funcționează atât cu OpenAI cât și Azure OpenAI fără gestionarea `api_version`.

> [!NOTE] > `os.environ` citește variabilele de mediu. Poți să-l folosești pentru a citi variabile de mediu precum `AZURE_OPENAI_API_KEY` și `AZURE_OPENAI_ENDPOINT`. Setează aceste variabile în terminalul tău sau folosind o bibliotecă precum `dotenv`.

## Generare text

Modalitatea de a genera text este să folosești Responses API prin metoda `responses.create`. Iată un exemplu:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # acesta este numele implementării modelului tău
    input=prompt,
    store=False,
)
print(response.output_text)
```

În codul de mai sus, creăm un răspuns și trimitem modelul pe care vrem să-l folosim și promptul. Apoi afișăm textul generat prin `response.output_text`.

### Conversații multi-turn

Responses API este potrivit atât pentru generare de text cu un singur tur cât și pentru chatboți cu mai multe tururi – oferi o listă de mesaje în `input` pentru a construi o conversație:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Mai multe despre această funcționalitate într-un capitol viitor.

## Exercițiu - prima ta aplicație de generare a textului

Acum că am învățat cum să configurăm openai, e timpul să construim prima ta aplicație de generare a textului. Pentru a construi aplicația, urmează pașii:

1. Creează un mediu virtual și instalează openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Dacă folosești Windows, tastează `venv\Scripts\activate` în loc de `source venv/bin/activate`.

   > [!NOTE]
   > Găsește cheia ta Azure OpenAI mergând la [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), caută `Open AI`, selectează resource-ul `Open AI`, apoi alege `Keys and Endpoint` și copiază valoarea `Key 1`.

1. Creează un fișier _app.py_ și pune următorul cod:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # adaugă codul tău de completare
   prompt = "Complete the following: Once upon a time there was a"

   # fă o cerere folosind API-ul Responses
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # afișează răspunsul
   print(response.output_text)
   ```

   > [!NOTE]
   > Dacă folosești OpenAI simplu (nu Azure), folosește `client = OpenAI(api_key="<înlocuiește această valoare cu cheia ta OpenAI>")` (fără `base_url`) și trimite un nume de model precum `gpt-4o-mini` în loc de un nume de deployment.

   Ar trebui să vezi o ieșire asemănătoare cu următoarea:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Diferite tipuri de prompturi, pentru lucruri diferite

Acum ai văzut cum să generezi text folosind un prompt. Ai chiar un program funcțional pe care îl poți modifica pentru a genera diferite tipuri de text.

Prompturile pot fi folosite pentru tot felul de sarcini. De exemplu:

- **Generarea unui tip de text**. De exemplu, poți genera o poezie, întrebări pentru un test etc.
- **Căutarea de informații**. Poți folosi prompturi pentru a căuta informații precum exemplul „Ce înseamnă CORS în dezvoltarea web?”.
- **Generarea de cod**. Poți folosi prompturi pentru a genera cod, de exemplu dezvoltând o expresie regulată folosită pentru validarea emailurilor sau, de ce nu, generând un program întreg, cum ar fi o aplicație web?

## Un caz de utilizare mai practic: un generator de rețete

Imaginează-ți că ai ingrediente acasă și vrei să gătești ceva. Pentru asta, ai nevoie de o rețetă. O modalitate de a găsi rețete este să folosești un motor de căutare sau poți folosi un LLM pentru asta.

Ai putea scrie un prompt astfel:

> „Arată-mi 5 rețete pentru un fel de mâncare cu următoarele ingrediente: pui, cartofi și morcovi. Pentru fiecare rețetă, listează toate ingredientele folosite”

Având promptul de mai sus, s-ar putea să obții un răspuns similar cu:

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

Acest rezultat este grozav, știu ce să gătesc. În acest punct, ce ar putea fi îmbunătățiri utile sunt:

- Eliminarea ingredientelor care nu-mi plac sau la care sunt alergic.
- Generarea unei liste de cumpărături, în cazul în care nu am toate ingredientele acasă.

Pentru cazurile de mai sus, să adăugăm un prompt suplimentar:

> „Te rog elimină rețetele cu usturoi deoarece sunt alergic și înlocuiește cu altceva. De asemenea, te rog generează o listă de cumpărături pentru rețete, având în vedere că am deja acasă pui, cartofi și morcovi.”

Acum ai un nou rezultat, și anume:

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

Aceasta sunt cele cinci rețete, fără niciun usturoi menționat și ai, de asemenea, o listă de cumpărături ținând cont de ce ai deja acasă.

## Exercițiu - construiește un generator de rețete

Acum că am prezentat un scenariu, să scriem cod care să corespundă scenariului demonstrat. Pentru asta, urmează pașii:

1. Folosește fișierul existent _app.py_ ca punct de plecare
1. Găsește variabila `prompt` și schimbă codul ei cu următorul:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Dacă rulezi acum codul, ar trebui să vezi o ieșire asemănătoare cu:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTĂ, LLM-ul tău este nedomnirestic, deci s-ar putea să obții rezultate diferite la fiecare rulare.

   Grozav, să vedem cum putem îmbunătăți lucrurile. Pentru a le îmbunătăți, vrem să ne asigurăm că codul este flexibil, astfel încât ingredientele și numărul de rețete să poată fi modificate și schimbate.

1. Să schimbăm codul astfel:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolați numărul de rețete în prompt și ingrediente
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Un exemplu de rulare a codului ar putea arăta așa:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Îmbunătățire prin adăugarea filtrului și a listei de cumpărături

Acum avem o aplicație funcțională capabilă să genereze rețete și este flexibilă deoarece se bazează pe inputurile utilizatorului, atât în privința numărului de rețete, cât și a ingredientelor folosite.

Pentru a o îmbunătăți și mai mult, vrem să adăugăm următoarele:

- **Filtrarea ingredientelor**. Vrem să putem filtra ingredientele care nu ne plac sau la care suntem alergici. Pentru această modificare, putem edita promptul nostru existent și adăuga o condiție de filtrare la final, astfel:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Mai sus, adăugăm `{filter}` la finalul promptului și, de asemenea, capturăm valoarea filtrului de la utilizator.

  Un exemplu de input la rularea programului poate arăta acum astfel:

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

  După cum vezi, orice rețetă cu lapte a fost filtrată. Dar, dacă ești intolerant la lactoză, s-ar putea să vrei să filtrezi și rețetele cu brânză, deci e nevoie să fii clar.


- **Produce o listă de cumpărături**. Vrem să producem o listă de cumpărături, luând în considerare ceea ce avem deja acasă.

  Pentru această funcționalitate, am putea încerca fie să rezolvăm totul într-un singur prompt, fie să împărțim în două prompturi. Să încercăm a doua abordare. Aici sugerăm să adăugăm un prompt suplimentar, dar pentru ca asta să funcționeze, trebuie să adăugăm rezultatul primului prompt ca context celui de-al doilea prompt.

  Găsește partea din cod care afișează rezultatul primului prompt și adaugă următorul cod dedesubt:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # afișează răspunsul
  print("Shopping list:")
  print(response.output_text)
  ```

  Notează următoarele:

  1. Construim un prompt nou adăugând rezultatul primului prompt la noul prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Facem o cerere nouă, dar ținând cont de numărul de tokeni ceruți în primul prompt, astfel de data aceasta spunem că `max_output_tokens` este 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Rulând acest cod, ajungem acum la următorul rezultat:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Îmbunătățește configurarea ta

Ceea ce avem până acum este un cod care funcționează, dar există unele ajustări pe care ar trebui să le facem pentru a îmbunătăți și mai mult lucrurile. Câteva lucruri pe care ar trebui să le facem sunt:

- **Separă secretele de cod**, cum ar fi cheia API. Secretele nu au ce căuta în cod și ar trebui stocate într-o locație sigură. Pentru a separa secretele de cod, putem folosi variabile de mediu și biblioteci precum `python-dotenv` pentru a le încărca dintr-un fișier. Iată cum ar arăta asta în cod:

  1. Creează un fișier `.env` cu următorul conținut:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Atenție, pentru Azure OpenAI în Microsoft Foundry, trebuie să setezi următoarele variabile de mediu în schimb:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     În cod, ai încărca variabilele de mediu astfel:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Un cuvânt despre lungimea tokenilor**. Ar trebui să luăm în considerare câți tokeni sunt necesari pentru a genera textul dorit. Tokenii costă bani, așa că, pe cât posibil, ar trebui să fim economici cu numărul de tokeni folosiți. De exemplu, putem formula promptul astfel încât să folosim mai puțini tokeni?

  Pentru a schimba tokenii folosiți, poți utiliza parametrul `max_output_tokens`. De exemplu, dacă vrei să folosești 100 tokeni, ai face:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentarea cu temperatura**. Temperatura este ceva despre care nu am menționat până acum, dar este un context important pentru performanța programului nostru. Cu cât valoarea temperaturii este mai mare, cu atât ieșirea va fi mai aleatorie. În schimb, cu cât valoarea temperaturii este mai mică, cu atât ieșirea va fi mai previzibilă. Ia în considerare dacă dorești variație în ieșirea ta sau nu.

  Pentru a modifica temperatura, poți folosi parametrul `temperature`. De exemplu, dacă vrei să folosești o temperatură de 0.5, ai face:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Atenție, cu cât ne apropiem de 1.0, cu atât ieșirea este mai variată.

## Tema

Pentru această temă, poți alege ce să construiești.

Iată câteva sugestii:

- Ajustează aplicația generator de rețete pentru a o îmbunătăți și mai mult. Experimentează cu valorile temperaturii și cu prompturile pentru a vedea ce poți realiza.
- Construiește un "partener de studiu". Această aplicație ar trebui să poată răspunde la întrebări despre un subiect, de exemplu Python, poți avea prompturi de genul "Ce este un anumit subiect în Python?", sau un prompt care spune, arată-mi cod pentru un anumit subiect etc.
- Bot de istorie, fă istoria să prindă viață, instrucționează botul să joace rolul unui personaj istoric și pune-i întrebări despre viața și epoca sa.

## Soluție

### Partener de studiu

Mai jos este un prompt de început, vezi cum îl poți folosi și ajusta după cum dorești.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot de istorie

Iată câteva prompturi pe care le-ai putea folosi:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Verificare a cunoștințelor

Ce face conceptul de temperatură?

1. Controlează cât de aleatorie este ieșirea.
1. Controlează cât de mare este răspunsul.
1. Controlează câți tokeni sunt folosiți.

## 🚀 Provocare

Când lucrezi la temă, încearcă să variez temperatura, seteaz-o la 0, 0.5 și 1. Amintește-ți că 0 este cel mai puțin variat iar 1 este cel mai variat. Ce valoare funcționează cel mai bine pentru aplicația ta?

## Excelentă muncă! Continuă să înveți

După ce termini această lecție, consultă colecția noastră [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să-ți dezvolți cunoștințele despre Generative AI!

Mergi mai departe la Lecția 7 unde vom vedea cum să [construim aplicații de chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->