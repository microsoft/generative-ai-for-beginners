<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-17T22:03:45+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ro"
}
-->
# Construirea aplicațiilor de generare de text

[![Construirea aplicațiilor de generare de text](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.ro.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Click pe imaginea de mai sus pentru a viziona videoclipul lecției)_

Până acum, în cadrul acestui curs, ai văzut că există concepte de bază precum prompturile și chiar o întreagă disciplină numită "ingineria prompturilor". Multe instrumente cu care poți interacționa, cum ar fi ChatGPT, Office 365, Microsoft Power Platform și altele, te ajută să folosești prompturi pentru a realiza diverse lucruri.

Pentru a adăuga o astfel de experiență într-o aplicație, trebuie să înțelegi concepte precum prompturi, completări și să alegi o bibliotecă cu care să lucrezi. Exact asta vei învăța în acest capitol.

## Introducere

În acest capitol, vei:

- Afla despre biblioteca openai și conceptele sale de bază.
- Construi o aplicație de generare de text folosind openai.
- Înțelege cum să folosești concepte precum prompt, temperatură și token-uri pentru a construi o aplicație de generare de text.

## Obiective de învățare

La sfârșitul acestei lecții, vei putea:

- Explica ce este o aplicație de generare de text.
- Construi o aplicație de generare de text folosind openai.
- Configura aplicația pentru a folosi mai mulți sau mai puțini token-uri și pentru a modifica temperatura, pentru un rezultat variat.

## Ce este o aplicație de generare de text?

De obicei, atunci când construiești o aplicație, aceasta are un fel de interfață, cum ar fi următoarele:

- Bazată pe comenzi. Aplicațiile de tip consolă sunt aplicații tipice în care tastezi o comandă și aceasta execută o sarcină. De exemplu, `git` este o aplicație bazată pe comenzi.
- Interfață utilizator (UI). Unele aplicații au interfețe grafice (GUI) unde dai click pe butoane, introduci text, selectezi opțiuni și altele.

### Aplicațiile de tip consolă și UI sunt limitate

Compară-le cu o aplicație bazată pe comenzi în care tastezi o comandă:

- **Sunt limitate**. Nu poți tasta orice comandă, doar cele pe care aplicația le suportă.
- **Specifice limbii**. Unele aplicații suportă mai multe limbi, dar implicit aplicația este construită pentru o limbă specifică, chiar dacă poți adăuga suport pentru mai multe limbi.

### Beneficiile aplicațiilor de generare de text

Deci, cum este diferită o aplicație de generare de text?

Într-o aplicație de generare de text, ai mai multă flexibilitate, nu ești limitat la un set de comenzi sau la o limbă de intrare specifică. În schimb, poți folosi limbajul natural pentru a interacționa cu aplicația. Un alt beneficiu este că interacționezi deja cu o sursă de date care a fost antrenată pe un vast corpus de informații, în timp ce o aplicație tradițională ar putea fi limitată la ceea ce se află într-o bază de date.

### Ce pot construi cu o aplicație de generare de text?

Există multe lucruri pe care le poți construi. De exemplu:

- **Un chatbot**. Un chatbot care răspunde la întrebări despre subiecte, cum ar fi compania ta și produsele acesteia, ar putea fi o alegere bună.
- **Ajutor**. LLM-urile sunt excelente la lucruri precum rezumarea textului, obținerea de informații din text, producerea de texte precum CV-uri și altele.
- **Asistent de cod**. În funcție de modelul lingvistic pe care îl folosești, poți construi un asistent de cod care te ajută să scrii cod. De exemplu, poți folosi un produs precum GitHub Copilot, precum și ChatGPT, pentru a te ajuta să scrii cod.

## Cum pot începe?

Ei bine, trebuie să găsești o modalitate de a te integra cu un LLM, ceea ce implică de obicei următoarele două abordări:

- Folosește un API. Aici construiești cereri web cu promptul tău și primești text generat înapoi.
- Folosește o bibliotecă. Bibliotecile ajută la encapsularea apelurilor API și le fac mai ușor de utilizat.

## Biblioteci/SDK-uri

Există câteva biblioteci bine cunoscute pentru lucrul cu LLM-uri, cum ar fi:

- **openai**, această bibliotecă face ușoară conectarea la modelul tău și trimiterea de prompturi.

Apoi, există biblioteci care operează la un nivel mai înalt, cum ar fi:

- **Langchain**. Langchain este bine cunoscut și suportă Python.
- **Semantic Kernel**. Semantic Kernel este o bibliotecă dezvoltată de Microsoft care suportă limbajele C#, Python și Java.

## Prima aplicație folosind openai

Să vedem cum putem construi prima noastră aplicație, ce biblioteci avem nevoie, cât de mult este necesar și așa mai departe.

### Instalarea openai

Există multe biblioteci pentru interacționarea cu OpenAI sau Azure OpenAI. Este posibil să folosești numeroase limbaje de programare, cum ar fi C#, Python, JavaScript, Java și altele. Am ales să folosim biblioteca Python `openai`, așa că vom folosi `pip` pentru a o instala.

```bash
pip install openai
```

### Crearea unei resurse

Trebuie să urmezi pașii următori:

- Creează un cont pe Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obține acces la Azure OpenAI. Accesează [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) și solicită acces.

  > [!NOTE]
  > La momentul redactării, trebuie să aplici pentru acces la Azure OpenAI.

- Instalează Python <https://www.python.org/>
- Creează o resursă Azure OpenAI Service. Vezi acest ghid pentru cum să [creezi o resursă](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Localizarea cheii API și a punctului de acces

În acest moment, trebuie să îi spui bibliotecii `openai` ce cheie API să folosească. Pentru a găsi cheia API, accesează secțiunea "Keys and Endpoint" din resursa ta Azure OpenAI și copiază valoarea "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Acum că ai copiat aceste informații, să instruim bibliotecile să le folosească.

> [!NOTE]
> Este recomandat să separi cheia API de codul tău. Poți face acest lucru folosind variabile de mediu.
>
> - Setează variabila de mediu `OPENAI_API_KEY` la cheia ta API.
>   `export OPENAI_API_KEY='sk-...'`

### Configurarea Azure

Dacă folosești Azure OpenAI, iată cum configurezi setările:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Mai sus setăm următoarele:

- `api_type` la `azure`. Acest lucru spune bibliotecii să folosească Azure OpenAI și nu OpenAI.
- `api_key`, aceasta este cheia ta API găsită în Azure Portal.
- `api_version`, aceasta este versiunea API pe care vrei să o folosești. La momentul redactării, cea mai recentă versiune este `2023-05-15`.
- `api_base`, acesta este punctul de acces al API-ului. Poți găsi acest lucru în Azure Portal lângă cheia ta API.

> [!NOTE] > `os.getenv` este o funcție care citește variabilele de mediu. O poți folosi pentru a citi variabilele de mediu precum `OPENAI_API_KEY` și `API_BASE`. Setează aceste variabile de mediu în terminalul tău sau folosind o bibliotecă precum `dotenv`.

## Generarea textului

Modalitatea de a genera text este să folosești clasa `Completion`. Iată un exemplu:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

În codul de mai sus, creăm un obiect de completare și transmitem modelul pe care dorim să-l folosim și promptul. Apoi, afișăm textul generat.

### Completări de chat

Până acum, ai văzut cum am folosit `Completion` pentru a genera text. Dar există o altă clasă numită `ChatCompletion`, care este mai potrivită pentru chatbots. Iată un exemplu de utilizare:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Mai multe despre această funcționalitate într-un capitol viitor.

## Exercițiu - prima ta aplicație de generare de text

Acum că am învățat cum să configurăm și să utilizăm openai, este timpul să construim prima ta aplicație de generare de text. Pentru a construi aplicația, urmează acești pași:

1. Creează un mediu virtual și instalează openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Dacă folosești Windows, tastează `venv\Scripts\activate` în loc de `source venv/bin/activate`.

   > [!NOTE]
   > Localizează cheia ta Azure OpenAI accesând [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), caută `Open AI`, selectează resursa `Open AI` și apoi selectează `Keys and Endpoint` și copiază valoarea `Key 1`.

1. Creează un fișier _app.py_ și adaugă următorul cod:

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
   > Dacă folosești Azure OpenAI, trebuie să setezi `api_type` la `azure` și să setezi `api_key` la cheia ta Azure OpenAI.

   Ar trebui să vezi un rezultat similar cu următorul:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Diferite tipuri de prompturi pentru diferite lucruri

Acum ai văzut cum să generezi text folosind un prompt. Ai chiar și un program funcțional pe care îl poți modifica și schimba pentru a genera diferite tipuri de text.

Prompturile pot fi utilizate pentru diverse sarcini. De exemplu:

- **Generarea unui tip de text**. De exemplu, poți genera o poezie, întrebări pentru un test etc.
- **Căutarea informațiilor**. Poți folosi prompturi pentru a căuta informații, cum ar fi exemplul următor: "Ce înseamnă CORS în dezvoltarea web?".
- **Generarea de cod**. Poți folosi prompturi pentru a genera cod, de exemplu, dezvoltarea unei expresii regulate utilizate pentru validarea emailurilor sau chiar generarea unui program întreg, cum ar fi o aplicație web.

## Un caz practic: generator de rețete

Imaginează-ți că ai ingrediente acasă și vrei să gătești ceva. Pentru asta, ai nevoie de o rețetă. O modalitate de a găsi rețete este să folosești un motor de căutare sau ai putea folosi un LLM pentru asta.

Ai putea scrie un prompt astfel:

> "Arată-mi 5 rețete pentru un fel de mâncare cu următoarele ingrediente: pui, cartofi și morcovi. Pentru fiecare rețetă, listează toate ingredientele utilizate."

Având promptul de mai sus, ai putea obține un răspuns similar cu:

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

Acest rezultat este grozav, știu ce să gătesc. În acest punct, ce ar putea fi îmbunătățit este:

- Excluderea ingredientelor care nu îmi plac sau la care sunt alergic.
- Generarea unei liste de cumpărături, în cazul în care nu am toate ingredientele acasă.

Pentru cazurile de mai sus, să adăugăm un prompt suplimentar:

> "Te rog să elimini rețetele cu usturoi deoarece sunt alergic și să îl înlocuiești cu altceva. De asemenea, te rog să generezi o listă de cumpărături pentru rețete, având în vedere că deja am pui, cartofi și morcovi acasă."

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

Acestea sunt cele cinci rețete, fără usturoi menționat și ai, de asemenea, o listă de cumpărături având în vedere ce ai deja acasă.

## Exercițiu - construiește un generator de rețete

Acum că am explorat un scenariu, să scriem codul pentru a se potrivi cu scenariul demonstrat. Pentru a face acest lucru, urmează acești pași:

1. Folosește fișierul existent _app.py_ ca punct de plecare.
1. Localizează variabila `prompt` și schimbă codul acesteia cu următorul:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Dacă rulezi acum codul, ar trebui să vezi un rezultat similar cu:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, LLM-ul tău este nedeterminist, așa că s-ar putea să obții rezultate diferite de fiecare dată când rulezi programul.

   Grozav, să vedem cum putem îmbunătăți lucrurile. Pentru a îmbunătăți lucrurile, vrem să ne asigurăm că codul este flexibil, astfel încât ingredientele și numărul de rețete să poată fi îmbunătățite și modificate.

1. Să schimbăm codul în următorul mod:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testarea codului ar putea arăta astfel:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Îmbunătățire prin adăugarea filtrului și a listei de cumpărături

Acum avem o aplicație funcțională capabilă să producă rețete și este flexibilă, deoarece se bazează pe intrările utilizatorului, atât în ceea ce privește numărul de rețete, cât și ingredientele utilizate.

Pentru a o îmbunătăți, vrem să adăugăm următoarele:

- **Filtrarea ingredientelor**. Vrem să putem filtra ingredientele care nu ne plac sau la care suntem alergici. Pentru a realiza această schimbare, putem edita promptul existent și să adăugăm o condiție de filtrare la sfârșitul acestuia astfel:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Mai sus, adăugăm `{filter}` la sfârșitul promptului și capturăm, de asemenea, valoarea filtrului de la utilizator.

  Un exemplu de intrare pentru rularea programului poate arăta astfel:

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

  După cum poți vedea, orice rețete cu lapte au fost filtrate. Dar, dacă ești intolerant la lactoză, s-ar putea să vrei să filtrezi și rețetele cu brânză, așa că este nevoie să fii clar.

- **Generarea unei liste de cumpărături**. Vrem să generăm o listă de cumpărături, având în vedere ce avem deja acasă.

  Pentru această funcționalitate, am putea încerca să rezolvăm totul într-un singur prompt sau am putea să o împărțim în două prompturi. Să încercăm a doua abordare. Aici sugerăm adăugarea unui prompt suplimentar, dar pentru ca acesta să funcționeze, trebuie să adăugăm rezultatul primului prompt ca context pentru al doilea prompt.

  Localizează partea din cod care afișează rezultatul primului prompt și adaugă următorul cod dedesubt:
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

  Observați următoarele:

  1. Construim un nou prompt adăugând rezultatul de la primul prompt la noul prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Facem o nouă cerere, dar luăm în considerare și numărul de tokeni pe care i-am cerut în primul prompt, așa că de data aceasta spunem că `max_tokens` este 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Testând acest cod, ajungem acum la următorul rezultat:

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

Ceea ce avem până acum este un cod funcțional, dar există câteva ajustări pe care ar trebui să le facem pentru a îmbunătăți lucrurile. Unele lucruri pe care ar trebui să le facem sunt:

- **Separarea secretelor de cod**, cum ar fi cheia API. Secretele nu ar trebui să fie incluse în cod și ar trebui să fie stocate într-un loc sigur. Pentru a separa secretele de cod, putem folosi variabile de mediu și biblioteci precum `python-dotenv` pentru a le încărca dintr-un fișier. Iată cum ar arăta acest lucru în cod:

  1. Creează un fișier `.env` cu următorul conținut:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Notă, pentru Azure, trebuie să setați următoarele variabile de mediu:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     În cod, ați încărca variabilele de mediu astfel:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Un cuvânt despre lungimea tokenilor**. Ar trebui să luăm în considerare câți tokeni avem nevoie pentru a genera textul dorit. Tokenii costă bani, așa că, acolo unde este posibil, ar trebui să încercăm să fim economi cu numărul de tokeni pe care îi folosim. De exemplu, putem formula promptul astfel încât să folosim mai puțini tokeni?

  Pentru a schimba numărul de tokeni utilizați, puteți folosi parametrul `max_tokens`. De exemplu, dacă doriți să folosiți 100 de tokeni, ați face:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Experimentarea cu temperatura**. Temperatura este ceva ce nu am menționat până acum, dar este un context important pentru modul în care programul nostru funcționează. Cu cât valoarea temperaturii este mai mare, cu atât rezultatul va fi mai aleatoriu. În schimb, cu cât valoarea temperaturii este mai mică, cu atât rezultatul va fi mai previzibil. Luați în considerare dacă doriți variație în rezultatul dvs. sau nu.

  Pentru a modifica temperatura, puteți folosi parametrul `temperature`. De exemplu, dacă doriți să folosiți o temperatură de 0.5, ați face:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Notă, cu cât valoarea este mai aproape de 1.0, cu atât rezultatul va fi mai variat.

## Temă

Pentru această temă, puteți alege ce să construiți.

Iată câteva sugestii:

- Ajustați aplicația de generare de rețete pentru a o îmbunătăți și mai mult. Experimentați cu valorile temperaturii și cu prompturile pentru a vedea ce puteți obține.
- Construiți un "coleg de studiu". Această aplicație ar trebui să poată răspunde la întrebări despre un subiect, de exemplu Python. Ați putea avea prompturi precum "Ce este un anumit subiect în Python?" sau ați putea avea un prompt care spune "arată-mi codul pentru un anumit subiect" etc.
- Bot de istorie, faceți istoria să prindă viață, instruiți botul să joace rolul unui anumit personaj istoric și puneți-i întrebări despre viața și vremurile sale.

## Soluție

### Coleg de studiu

Mai jos este un prompt de început, vedeți cum îl puteți folosi și ajusta după preferințele voastre.

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

## Verificarea cunoștințelor

Ce face conceptul de temperatură?

1. Controlează cât de aleatoriu este rezultatul.
1. Controlează cât de mare este răspunsul.
1. Controlează câți tokeni sunt utilizați.

## 🚀 Provocare

Când lucrați la temă, încercați să variați temperatura, încercați să o setați la 0, 0.5 și 1. Amintiți-vă că 0 este cel mai puțin variat și 1 este cel mai variat. Ce valoare funcționează cel mai bine pentru aplicația voastră?

## Felicitări! Continuă să înveți

După ce ai finalizat această lecție, verifică [Colecția de Învățare AI Generativă](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pentru a continua să îți dezvolți cunoștințele despre AI Generativă!

Accesează Lecția 7 unde vom analiza cum să [construim aplicații de chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.