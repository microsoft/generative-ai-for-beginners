# Construirea aplicațiilor de generare text

[![Construirea aplicațiilor de generare text](../../../translated_images/ro/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

Ați văzut până acum în cadrul acestui curriculum că există concepte de bază precum prompturile și chiar o disciplină întreagă numită „ingineria prompturilor”. Multe instrumente cu care puteți interacționa, cum ar fi ChatGPT, Office 365, Microsoft Power Platform și altele, vă susțin folosind prompturi pentru a realiza ceva.

Pentru a adăuga o astfel de experiență într-o aplicație, trebuie să înțelegeți concepte precum prompturile, completările și să alegeți o bibliotecă cu care să lucrați. Exact asta veți învăța în acest capitol.

## Introducere

În acest capitol, veți:

- Înțelege biblioteca openai și conceptele sale de bază.
- Construi o aplicație de generare text folosind openai.
- Înțelege cum să folosești concepte precum prompt, temperatura și token-urile pentru a construi o aplicație de generare text.

## Obiective de învățare

La finalul acestei lecții, veți putea:

- Explica ce este o aplicație de generare text.
- Construi o aplicație de generare text folosind openai.
- Configura aplicația pentru a folosi mai multe sau mai puține token-uri și, de asemenea, pentru a schimba temperatura, pentru un rezultat variat.

## Ce este o aplicație de generare text?

De obicei, când construiești o aplicație, aceasta are un fel de interfață, cum ar fi următoarele:

- Bazată pe comandă. Aplicațiile console sunt aplicații tipice în care tastezi o comandă și aceasta execută o sarcină. De exemplu, `git` este o aplicație bazată pe comandă.
- Interfață de utilizator (UI). Unele aplicații au interfețe grafice de utilizator (GUI) unde apeși butoane, introduci text, selectezi opțiuni și altele.

### Aplicațiile console și UI sunt limitate

Compară cu o aplicație bazată pe comandă în care tastezi o comandă:

- **Este limitată**. Nu poți să tastezi orice comandă, ci doar pe cele pe care aplicația le suportă.
- **Specifică limbajului**. Unele aplicații suportă multe limbi, dar implicit aplicația este construită pentru un limbaj specific, chiar dacă poți adăuga suport pentru mai multe limbi.

### Beneficiile aplicațiilor de generare text

Deci, cum este o aplicație de generare text diferită?

Într-o aplicație de generare text, ai mai multă flexibilitate, nu ești limitat la un set de comenzi sau un limbaj de intrare specific. În schimb, poți folosi limbajul natural pentru a interacționa cu aplicația. Un alt beneficiu este că deja interacționezi cu o sursă de date care a fost antrenată pe un vast corpus de informații, pe când o aplicație tradițională poate fi limitată la ceea ce conține o bază de date.

### Ce pot construi cu o aplicație de generare text?

Sunt multe lucruri pe care le poți construi. De exemplu:

- **Un chatbot**. Un chatbot care răspunde la întrebări despre subiecte, cum ar fi compania ta și produsele sale, ar putea fi o alegere bună.
- **Asistent**. Modelele LLM sunt excelente la lucruri precum rezumarea textului, obținerea de informații din text, generarea de texte precum CV-uri și altele.
- **Asistent de cod**. În funcție de modelul de limbaj utilizat, poți construi un asistent care te ajută să scrii cod. De exemplu, poți folosi un produs precum GitHub Copilot, precum și ChatGPT, pentru a te ajuta să scrii cod.

## Cum pot începe?

Ei bine, trebuie să găsești o modalitate de a te integra cu un LLM, ceea ce implică de obicei următoarele două abordări:

- Folosește un API. Aici construiești cereri web cu promptul tău și primești text generat înapoi.
- Folosește o bibliotecă. Bibliotecile ajută la încapsularea apelurilor API și le fac mai ușor de utilizat.

## Biblioteci/SDK-uri

Există câteva biblioteci cunoscute pentru lucrul cu LLM-uri, cum ar fi:

- **openai**, această bibliotecă face ușoară conectarea la modelul tău și trimiterea de prompturi.

Apoi există biblioteci care operează la un nivel mai înalt, precum:

- **Langchain**. Langchain este bine cunoscut și suportă Python.
- **Semantic Kernel**. Semantic Kernel este o bibliotecă Microsoft care suportă limbajele C#, Python și Java.

## Prima aplicație folosind openai

Să vedem cum putem construi prima noastră aplicație, ce biblioteci avem nevoie, cât este necesar și așa mai departe.

### Instalează openai

Există multe biblioteci pentru interacționarea cu OpenAI sau Azure OpenAI. Este posibil să folosești diverse limbaje de programare precum C#, Python, JavaScript, Java și altele. Am ales să folosim biblioteca Python `openai`, așa că vom folosi `pip` pentru instalare.

```bash
pip install openai
```

### Creează un resource

Trebuie să parcurgi următorii pași:

- Creează un cont pe Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obține acces la Azure OpenAI. Mergi la [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) și solicită acces.

  > [!NOTE]
  > La momentul scrierii, trebuie să aplici pentru accesul la Azure OpenAI.

- Instalează Python <https://www.python.org/>
- Creează un resource Azure OpenAI Service. Vezi acest ghid pentru [cum să creezi un resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Găsește cheia API și endpoint-ul

În acest moment, trebuie să spui bibliotecii tale `openai` ce cheie API să folosească. Pentru a găsi cheia API, mergi la secțiunea „Keys and Endpoint” a resursei tale Azure OpenAI și copiază valoarea „Key 1”.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Acum că ai această informație copiată, să instruim bibliotecile să o folosească.

> [!NOTE]
> Merită să separi cheia ta API de codul tău. Poți face asta folosind variabile de mediu.
>
> - Setează variabila de mediu `OPENAI_API_KEY` la cheia ta API.
>   `export OPENAI_API_KEY='sk-...'`

### Configurează Azure

Dacă folosești Azure OpenAI (acum parte din Microsoft Foundry), iată cum configurezi setarea. Folosim clientul standard `OpenAI` orientat către endpoint-ul Azure OpenAI `/openai/v1/`, care funcționează cu Responses API și nu necesită `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Mai sus setăm următoarele:

- `api_key`, aceasta este cheia ta API găsită în Azure Portal sau portalul Microsoft Foundry.
- `base_url`, aceasta este endpoint-ul resursei tale Foundry cu `/openai/v1/` adăugat. Endpoint-ul stabil v1 funcționează atât pentru OpenAI cât și pentru Azure OpenAI fără management de `api_version`.

> [!NOTE] > `os.environ` citește variabilele de mediu. Poți folosi această funcție pentru a citi variabile de mediu ca `AZURE_OPENAI_API_KEY` și `AZURE_OPENAI_ENDPOINT`. Setează aceste variabile în terminalul tău sau folosind o bibliotecă precum `dotenv`.

## Generează text

Modalitatea de a genera text este să folosești Responses API prin metoda `responses.create`. Iată un exemplu:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

În codul de mai sus, creăm un răspuns și transmitem modelul dorit și promptul. Apoi afișăm textul generat prin `response.output_text`.

### Conversații cu mai multe tururi

Responses API este potrivit atât pentru generarea textului cu un singur tur, cât și pentru chatbots cu mai multe tururi - oferi o listă de mesaje în `input` pentru a construi o conversație:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Mai multe despre această funcționalitate într-un capitol viitor.

## Exercițiu - prima ta aplicație de generare text

Acum că am învățat cum să configurăm și să folosim openai, e timpul să construiești prima ta aplicație de generare text. Pentru a-ți construi aplicația, urmează acești pași:

1. Creează un mediu virtual și instalează openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Dacă folosești Windows, tastează `venv\Scripts\activate` în loc de `source venv/bin/activate`.

   > [!NOTE]
   > Găsește cheia ta Azure OpenAI mergând la [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), caută `Open AI` și selectează `Open AI resource` apoi selectează `Keys and Endpoint` și copiază valoarea `Key 1`.

1. Creează un fișier _app.py_ și pune următorul cod în el:

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
   > Dacă folosești OpenAI simplu (nu Azure), folosește `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (fără `base_url`) și oferă un nume de model precum `gpt-5-mini` în loc de numele unui deployment.

   Ar trebui să vezi o ieșire similară cu aceasta:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Tipuri diferite de prompt-uri, pentru lucruri diferite

Acum ai văzut cum să generezi text folosind un prompt. Ai chiar și un program funcțional pe care îl poți modifica și schimba pentru a genera tipuri diferite de text.

Prompturile pot fi folosite pentru diverse sarcini. De exemplu:

- **Generează un tip de text**. De exemplu, poți genera o poezie, întrebări pentru un quiz etc.
- **Caută informații**. Poți folosi prompturi pentru a căuta informații precum exemplul „Ce înseamnă CORS în dezvoltarea web?”.
- **Generează cod**. Poți folosi prompturi pentru a genera cod, de exemplu pentru a crea o expresie regulată folosită pentru validarea email-urilor sau de ce nu să generezi un program întreg, cum ar fi o aplicație web?

## Un caz de utilizare mai practic: generator de rețete

Imaginează-ți că ai ingrediente acasă și vrei să gătești ceva. Pentru asta, ai nevoie de o rețetă. Un mod de a găsi rețete este să folosești un motor de căutare sau ai putea folosi un LLM să facă asta.

Ai putea scrie un prompt astfel:

> „Arată-mi 5 rețete pentru un fel de mâncare cu următoarele ingrediente: pui, cartofi și morcovi. Pentru fiecare rețetă, listează toate ingredientele folosite”

Având promptul de mai sus, s-ar putea să primești un răspuns asemănător cu:

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

Acest rezultat este grozav, știu ce să gătesc. În acest punct, ce ar putea fi îmbunătățit util este:

- Filtrarea ingredientelor pe care nu le plac sau la care sunt alergic.
- Generarea unei liste de cumpărături, în cazul în care nu am toate ingredientele acasă.

Pentru cazurile de mai sus, să adăugăm un prompt suplimentar:

> „Te rog elimină rețetele cu usturoi deoarece sunt alergic și înlocuiește-le cu altceva. De asemenea, te rog să produci o listă de cumpărături pentru rețete, tinând cont că am deja pui, cartofi și morcovi acasă.”

Acum ai un rezultat nou, și anume:

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

Aceasta sunt cele cinci rețete, fără nici o mențiune de usturoi și ai și o listă de cumpărături, ținând cont de ce ai deja acasă.

## Exercițiu - construiește un generator de rețete

Acum că am jucat un scenariu, să scriem cod care să se potrivească cu scenariul demonstrat. Pentru asta, urmează acești pași:

1. Folosește fișierul existent _app.py_ ca punct de plecare
1. Localizează variabila `prompt` și schimbă codul ei cu următorul:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Dacă rulezi acum codul, ar trebui să vezi o ieșire similară cu:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTĂ, LLM-ul tău este nedeterminist, deci s-ar putea să obții rezultate diferite de fiecare dată când rulezi programul.

   Grozav, să vedem cum putem îmbunătăți lucrurile. Pentru asta vrem ca codul să fie flexibil, astfel încât ingredientele și numărul de rețete să poată fi îmbunătățite și schimbate.

1. Hai să schimbăm codul în următorul mod:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Rulând codul pentru test, ar putea arăta așa:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Îmbunătățire prin adăugarea filtrului și a listei de cumpărături

Acum avem o aplicație funcțională capabilă să producă rețete și este flexibilă deoarece se bazează pe input-uri de la utilizator, atât privind numărul de rețete, cât și ingredientele folosite.

Pentru a o îmbunătăți, vrem să adăugăm următoarele:

- **Filtrare ingrediente**. Vrem să putem filtra ingredientele pe care nu le plac sau la care suntem alergici. Pentru această modificare, putem edita promptul existent și să adăugăm o condiție de filtrare la final, astfel:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Mai sus, adăugăm `{filter}` la sfârșitul promptului și de asemenea capturăm valoarea filtrului de la utilizator.

  Un exemplu de input la rularea programului poate acum arăta astfel:

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

  După cum vezi, orice rețete cu lapte au fost filtrate. Dar, dacă ești intolerant la lactoză, poate dorești să filtrezi și rețetele cu brânză, așa că este nevoie să fii clar.

- **Produ listă de cumpărături**. Vrem să producem o listă de cumpărături, ținând cont de ceea ce avem deja acasă.

  Pentru această funcționalitate, am putea încerca să rezolvăm totul într-un singur prompt sau să împărțim în două prompturi. Să încercăm a doua abordare. Aici sugerăm să adăugăm un prompt suplimentar, dar pentru ca acesta să funcționeze, trebuie să adăugăm rezultatul primului prompt ca context la promptul următor.

  Localizează partea din cod care afișează rezultatul primului prompt și adaugă următorul cod dedesubt:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Observă următoarele:

  1. Construim un prompt nou adăugând rezultatul primului prompt la promptul nou:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Facem o cerere nouă, dar ținând cont și de numărul de token-uri cerut în primul prompt, deci de această dată spunem că `max_output_tokens` este 1200.

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

## Îmbunătățește-ți configurația

Ceea ce avem până acum este un cod care funcționează, dar există unele ajustări pe care ar trebui să le facem pentru a îmbunătăți lucrurile în continuare. Unele lucruri pe care ar trebui să le facem sunt:

- **Separați secretele de cod**, cum ar fi cheia API. Secretele nu aparțin codului și trebuie stocate într-un loc sigur. Pentru a separa secretele de cod, putem folosi variabile de mediu și biblioteci precum `python-dotenv` pentru a le încărca dintr-un fișier. Iată cum ar arăta asta în cod:

  1. Creați un fișier `.env` cu următorul conținut:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Notă, pentru Azure OpenAI în Microsoft Foundry, trebuie să setați următoarele variabile de mediu în schimb:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     În cod, ați încărca variabilele de mediu astfel:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Un cuvânt despre lungimea token-urilor**. Ar trebui să luăm în considerare câte token-uri avem nevoie pentru a genera textul dorit. Token-urile costă bani, deci, pe cât posibil, ar trebui să încercăm să fim economici cu numărul de token-uri pe care îl folosim. De exemplu, putem formula promptul astfel încât să folosim mai puține token-uri?

  Pentru a schimba numărul de token-uri folosite, puteți utiliza parametrul `max_output_tokens`. De exemplu, dacă doriți să folosiți 100 de token-uri, ați face:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentarea cu temperatura**. Temperatura este ceva despre care nu am menționat până acum, dar este un context important pentru cum performează programul nostru. Cu cât valoarea temperaturii este mai mare, cu atât rezultatul este mai aleatoriu. În schimb, cu cât valoarea temperaturii este mai mică, cu atât rezultatul este mai previzibil. Luați în considerare dacă doriți variație în output sau nu.

  Pentru a modifica temperatura, puteți utiliza parametrul `temperature`. De exemplu, dacă doriți să folosiți o temperatură de 0.5, ați face:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Notă, cu cât este mai aproape de 1.0, cu atât outputul devine mai variat.

- **Modelele de raționament nu folosesc `temperature`**. Aceasta este o schimbare importantă în 2026. Modelele actuale, neînvechite din Microsoft Foundry sunt **modele de raționament** (familia GPT-5, o-series) - și **nu suportă `temperature` sau `top_p`** (nici `max_tokens`; folosiți `max_output_tokens`). Dacă trimiteți `temperature` la `gpt-5-mini` veți primi o eroare "parametru nesuportat". Așadar, pentru a încerca exemplul cu temperatura de mai sus, îndreptați-l spre un model care încă suportă controale de sampling - de exemplu un model deschis **Llama** precum `Llama-3.3-70B-Instruct` din [catalogul de modele Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), apelat prin Foundry Models / Azure AI Inference endpoint (în același mod ca și mostrele `githubmodels-*`). Pentru modelele de raționament precum GPT-5, direcționați outputul altfel:
  - **Prompt engineering** - instrucțiuni clare, exemple și output structurat (vedeți lecția [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) fac munca pe care butoanele de sampling obișnuiau să o facă.
  - **Controale de raționament** - parametri precum efortul/verbositatea raționamentului echilibrează adâncimea raționamentului cu latența și costul.

  Pe scurt: `temperature`/`top_p` sunt încă valide pe multe modele (Llama, Mistral, Phi, și familia GPT-4.x - deși GPT-4.x este în curs de depreciere), dar direcția este prompt engineering + controale de raționament pe modelele de raționament ca GPT-5.

## Tema

Pentru această temă, puteți alege ce să construiți.

Iată câteva sugestii:

- Ajustați aplicația generator de rețete pentru a o îmbunătăți în continuare. Experimentați cu valorile de temperatură și cu prompturile pentru a vedea ce puteți obține.
- Construiți un „asistent de studiu”. Această aplicație ar trebui să poată răspunde la întrebări despre un subiect, de exemplu Python; ați putea avea prompturi precum "Ce este un anumit subiect în Python?", sau un prompt care spune, arată-mi cod pentru un anumit subiect etc.
- Bot de istorie, faceți istoria să prindă viață, instruiți botul să joace rolul unui anumit personaj istoric și întrebați-l despre viața și timpurile sale.

## Soluție

### Asistent de studiu

Mai jos este un prompt de start, vedeți cum îl puteți folosi și ajusta după preferințe.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot de istorie

Iată câteva prompturi pe care le-ați putea folosi:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Verificare de cunoștințe

Ce face conceptul de temperatură?

1. Controlează cât de aleatoriu este outputul.
1. Controlează cât de mare este răspunsul.
1. Controlează câte token-uri sunt folosite.

## 🚀 Provocare

Când lucrați la temă, încercați să variați temperatura, setați-o la 0, 0.5 și 1. Amintiți-vă că 0 este cel mai puțin variat și 1 este cel mai variat. Ce valoare funcționează cel mai bine pentru aplicația dvs.?

## Treabă grozavă! Continuați să învățați

După ce ați terminat această lecție, verificați colecția noastră [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să vă dezvoltați cunoștințele despre AI generativ!

Mergeți la Lecția 7 unde vom vedea cum să [construiți aplicații de chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->