# Costruire Applicazioni di Generazione di Testo

[![Costruire Applicazioni di Generazione di Testo](../../../translated_images/it/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

Hai visto finora attraverso questo curriculum che ci sono concetti fondamentali come i prompt e persino un'intera disciplina chiamata "prompt engineering". Molti strumenti con cui puoi interagire come ChatGPT, Office 365, Microsoft Power Platform e altri, ti supportano utilizzando i prompt per realizzare qualcosa.

Per aggiungere tale esperienza a un'app, devi comprendere concetti come prompt, completamenti e scegliere una libreria con cui lavorare. È esattamente ciò che imparerai in questo capitolo.

## Introduzione

In questo capitolo, imparerai a:

- Conoscere la libreria openai e i suoi concetti fondamentali.
- Costruire un'app di generazione di testo usando openai.
- Capire come usare concetti come prompt, temperature e token per costruire un'app di generazione di testo.

## Obiettivi di apprendimento

Al termine di questa lezione, sarai in grado di:

- Spiegare cos'è un'app di generazione di testo.
- Costruire un'app di generazione di testo usando openai.
- Configurare la tua app per usare più o meno token e anche cambiare la temperatura, per un output vario.

## Cos'è un'app di generazione di testo?

Normalmente, quando costruisci un'app, ha qualche tipo di interfaccia come la seguente:

- Basata su comandi. Le app da console sono app tipiche in cui digiti un comando ed esegue un compito. Per esempio, `git` è un'app basata su comandi.
- Interfaccia utente (UI). Alcune app hanno interfacce grafiche (GUI) dove clicchi pulsanti, inserisci testo, selezioni opzioni e altro.

### Le app console e UI sono limitate

Confrontale con un'app basata su comando dove digiti un comando:

- **È limitata**. Non puoi digitare un comando qualsiasi, solo quelli supportati dall'app.
- **Specifico di una lingua**. Alcune app supportano molte lingue, ma per default l'app è costruita per una lingua specifica, anche se puoi aggiungere il supporto ad altre lingue.

### Vantaggi delle app di generazione di testo

Allora in cosa una app di generazione testo è diversa?

In una app di generazione di testo hai più flessibilità, non sei limitato a un set di comandi o a una lingua di input specifica. Invece, puoi usare il linguaggio naturale per interagire con l'app. Un altro beneficio è che stai già interagendo con una fonte di dati che è stata addestrata su un vasto corpus di informazioni, mentre una app tradizionale potrebbe essere limitata a ciò che è in un database.

### Cosa posso costruire con un'app di generazione di testo?

Ci sono molte cose che puoi costruire. Per esempio:

- **Un chatbot**. Un chatbot che risponde a domande su argomenti come la tua azienda e i suoi prodotti potrebbe essere una buona soluzione.
- **Assistente**. I LLM sono ottimi per cose come riassumere testo, ottenere intuizioni dal testo, produrre testo come curriculum e altro.
- **Assistente di codice**. A seconda del modello linguistico che usi, puoi costruire un assistente di codice che ti aiuta a scrivere codice. Per esempio, puoi usare un prodotto come GitHub Copilot così come ChatGPT per aiutarti a scrivere codice.

## Come posso iniziare?

Bene, devi trovare un modo per integrare con un LLM che solitamente comporta i seguenti due approcci:

- Usare un'API. Qui costruisci richieste web con il tuo prompt e ricevi un testo generato in risposta.
- Usare una libreria. Le librerie aiutano a incapsulare le chiamate API e renderle più facili da usare.

## Librerie/SDK

Ci sono alcune librerie ben note per lavorare con LLM come:

- **openai**, questa libreria rende facile connettersi al tuo modello e inviare prompt.

Poi ci sono librerie che operano a un livello più alto come:

- **Langchain**. Langchain è ben noto e supporta Python.
- **Semantic Kernel**. Semantic Kernel è una libreria di Microsoft che supporta i linguaggi C#, Python e Java.

## Prima app usando openai

Vediamo come possiamo costruire la nostra prima app, quali librerie servono, quanto è richiesto e così via.

### Installa openai

Ci sono molte librerie per interagire con OpenAI o Azure OpenAI. È possibile usare numerosi linguaggi di programmazione come C#, Python, JavaScript, Java e altri. Abbiamo scelto di usare la libreria Python `openai`, quindi useremo `pip` per installarla.

```bash
pip install openai
```

### Crea una risorsa

Devi eseguire i seguenti passaggi:

- Crea un account su Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Ottieni accesso ad Azure OpenAI. Vai su [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) e richiedi accesso.

  > [!NOTE]
  > Al momento della scrittura, è necessario fare richiesta di accesso ad Azure OpenAI.

- Installa Python <https://www.python.org/>
- Crea una risorsa Azure OpenAI Service. Consulta questa guida per sapere come [creare una risorsa](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Trova chiave API e endpoint

A questo punto, devi dire alla libreria `openai` quale chiave API usare. Per trovare la tua chiave API, vai alla sezione "Keys and Endpoint" della tua risorsa Azure OpenAI e copia il valore "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Ora che hai copiato queste informazioni, istruiamo le librerie a usarle.

> [!NOTE]
> Vale la pena separare la chiave API dal tuo codice. Puoi farlo usando variabili d'ambiente.
>
> - Imposta la variabile d'ambiente `OPENAI_API_KEY` con la tua chiave API.
>   `export OPENAI_API_KEY='sk-...'`

### Configurazione Azure

Se usi Azure OpenAI (ora parte di Microsoft Foundry), ecco come configurare. Usiamo il client standard `OpenAI` puntato all'endpoint Azure OpenAI `/openai/v1/`, che funziona con l'API Responses e non richiede `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Qui stiamo impostando il seguente:

- `api_key`, questa è la tua chiave API trovata nel portal Azure o Microsoft Foundry.
- `base_url`, questo è l'endpoint della tua risorsa Foundry con `/openai/v1/` aggiunto. L'endpoint stabile v1 funziona sia per OpenAI che Azure OpenAI senza gestione di `api_version`.

> [!NOTE] > `os.environ` legge variabili d'ambiente. Puoi usarlo per leggere variabili come `AZURE_OPENAI_API_KEY` e `AZURE_OPENAI_ENDPOINT`. Imposta queste variabili nel terminale o usando una libreria come `dotenv`.

## Generare testo

Il modo per generare testo è usare l'API Responses tramite il metodo `responses.create`. Ecco un esempio:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # questo è il nome del tuo modello di distribuzione
    input=prompt,
    store=False,
)
print(response.output_text)
```

Nel codice sopra, creiamo una risposta e passiamo il modello che vogliamo usare e il prompt. Poi stampiamo il testo generato via `response.output_text`.

### Conversazioni multi-turno

L'API Responses è adatta sia per generazione di testo a turno singolo che per chatbot multi-turno - fornisci una lista di messaggi in `input` per costruire una conversazione:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Maggiori dettagli su questa funzionalità in un capitolo successivo.

## Esercizio - la tua prima app di generazione di testo

Ora che abbiamo imparato a configurare openai, è il momento di costruire la tua prima app di generazione di testo. Per costruire la tua app, segui questi passaggi:

1. Crea un ambiente virtuale e installa openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Se usi Windows digita `venv\Scripts\activate` invece di `source venv/bin/activate`.

   > [!NOTE]
   > Trova la tua chiave Azure OpenAI andando su [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) e cerca `Open AI` e seleziona la `risorsa Open AI` quindi seleziona `Keys and Endpoint` e copia il valore `Key 1`.

1. Crea un file _app.py_ e inserisci il seguente codice:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # aggiungi il tuo codice di completamento
   prompt = "Complete the following: Once upon a time there was a"

   # fai una richiesta usando l'API Responses
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # stampa la risposta
   print(response.output_text)
   ```

   > [!NOTE]
   > Se usi OpenAI semplice (non Azure), usa `client = OpenAI(api_key="<sostituisci questo valore con la tua chiave OpenAI>")` (senza `base_url`) e passa un nome modello come `gpt-4o-mini` invece di un nome di deployment.

   Vedrai un output simile al seguente:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Diversi tipi di prompt, per cose diverse

Ora hai visto come generare testo usando un prompt. Hai persino un programma in esecuzione che puoi modificare per generare diversi tipi di testo.

I prompt possono essere usati per tutti i tipi di compiti. Per esempio:

- **Generare un tipo di testo**. Per esempio, puoi generare una poesia, domande per un quiz ecc.
- **Ricercare informazioni**. Puoi usare prompt per cercare informazioni come il seguente esempio: 'Cosa significa CORS nello sviluppo web?'.
- **Generare codice**. Puoi usare prompt per generare codice, per esempio sviluppare una espressione regolare per validare email o perché no generare un programma intero, come una app web?

## Un caso d'uso più pratico: un generatore di ricette

Immagina di avere ingredienti a casa e vuoi cucinare qualcosa. Per questo, ti serve una ricetta. Un modo per trovare ricette è usare un motore di ricerca oppure puoi usare un LLM per farlo.

Potresti scrivere un prompt così:

> "Mostrami 5 ricette per un piatto con i seguenti ingredienti: pollo, patate e carote. Per ogni ricetta, elenca tutti gli ingredienti usati"

Dato il prompt sopra, potresti ottenere una risposta simile a:

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

Questo risultato è ottimo, so cosa cucinare. A questo punto, miglioramenti utili potrebbero essere:

- Filtrare gli ingredienti che non mi piacciono o a cui sono allergico.
- Produrre una lista della spesa, nel caso non abbia tutti gli ingredienti a casa.

Per questi casi, aggiungiamo un prompt aggiuntivo:

> "Per favore rimuovi le ricette con aglio perché sono allergico e sostituiscilo con qualcos'altro. Inoltre, per favore produci una lista della spesa per le ricette, considerando che ho già pollo, patate e carote a casa."

Ora hai un nuovo risultato, cioè:

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

Ecco le tue cinque ricette, senza aglio menzionato e hai anche una lista della spesa considerando ciò che hai già a casa.

## Esercizio - costruisci un generatore di ricette

Ora che abbiamo simulato uno scenario, scriviamo codice che corrisponda allo scenario dimostrato. Per farlo, segui questi passaggi:

1. Usa il file _app.py_ esistente come punto di partenza
1. Trova la variabile `prompt` e cambia il suo codice così:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Se ora esegui il codice, dovresti vedere un output simile a:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTA, il tuo LLM è nondeterministico, quindi potresti ottenere risultati diversi ogni volta che esegui il programma.

   Ottimo, vediamo come possiamo migliorare le cose. Per migliorare vogliamo rendere il codice flessibile, così ingredienti e numero di ricette possono essere migliorati e modificati.

1. Cambiamo il codice nel seguente modo:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolare il numero di ricette nel prompt e negli ingredienti
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Eseguendo un test, potrebbe apparire così:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Migliorare aggiungendo filtro e lista della spesa

Ora abbiamo un'app funzionante capace di produrre ricette ed è flessibile perché si basa sugli input dell'utente, sia sul numero di ricette che sugli ingredienti usati.

Per migliorarla ulteriormente, vogliamo aggiungere quanto segue:

- **Filtrare gli ingredienti**. Vogliamo poter filtrare gli ingredienti che non ci piacciono o a cui siamo allergici. Per realizzare questo cambiamento, possiamo modificare il nostro prompt esistente aggiungendo una condizione di filtro alla fine come segue:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Qui, aggiungiamo `{filter}` alla fine del prompt e raccogliamo anche il valore del filtro dall'utente.

  Un esempio di input eseguendo il programma può ora apparire così:

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

  Come puoi vedere, tutte le ricette con latte sono state filtrate. Ma, se sei intollerante al lattosio, potresti voler filtrare anche ricette con formaggio, quindi c'è bisogno di essere chiari.


- **Produrre una lista della spesa**. Vogliamo produrre una lista della spesa, considerando cosa abbiamo già a casa.

  Per questa funzionalità, potremmo provare a risolvere tutto in un solo prompt oppure potremmo dividerlo in due prompt. Proviamo quest'ultimo approccio. Qui suggeriamo di aggiungere un prompt aggiuntivo, ma perché funzioni, dobbiamo aggiungere il risultato del prompt precedente come contesto al prompt successivo.

  Individua la parte nel codice che stampa il risultato del primo prompt e aggiungi il seguente codice sotto:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # stampa risposta
  print("Shopping list:")
  print(response.output_text)
  ```

  Nota quanto segue:

  1. Stiamo costruendo un nuovo prompt aggiungendo il risultato del primo prompt al nuovo prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Facciamo una nuova richiesta, tenendo anche conto del numero di token richiesti nel primo prompt, quindi questa volta diciamo che `max_output_tokens` è 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Provando questo codice, arriviamo ora al seguente output:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Migliora la tua configurazione

Quello che abbiamo finora è un codice funzionante, ma ci sono alcune modifiche che dovremmo fare per migliorare ulteriormente. Alcune cose che dovremmo fare sono:

- **Separare i segreti dal codice**, come la chiave API. I segreti non devono stare nel codice e dovrebbero essere conservati in un luogo sicuro. Per separare i segreti dal codice, possiamo usare variabili d'ambiente e librerie come `python-dotenv` per caricarle da un file. Ecco come sarebbe in codice:

  1. Crea un file `.env` con il seguente contenuto:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Nota, per Azure OpenAI in Microsoft Foundry, devi impostare le seguenti variabili d'ambiente invece:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Nel codice, caricheresti le variabili d'ambiente così:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Una parola sulla lunghezza dei token**. Dovremmo considerare quanti token sono necessari per generare il testo desiderato. I token costano, quindi, dove possibile, dovremmo cercare di essere economici con il numero di token usati. Per esempio, possiamo formulare il prompt in modo da usare meno token?

  Per modificare i token usati, puoi usare il parametro `max_output_tokens`. Per esempio, se vuoi usare 100 token, faresti:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Sperimentare con la temperatura**. La temperatura è qualcosa che finora non abbiamo menzionato ma è un contesto importante per come si comporta il nostro programma. Più alto è il valore della temperatura, più casuale sarà l'output. Al contrario, più basso è il valore della temperatura, più prevedibile sarà l'output. Considera se vuoi variazione nel tuo output o no.

  Per modificare la temperatura, puoi usare il parametro `temperature`. Per esempio, se vuoi usare una temperatura di 0.5, faresti:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Nota, più ti avvicini a 1.0, più variegato sarà l'output.

## Compito

Per questo compito, puoi scegliere cosa costruire.

Ecco alcuni suggerimenti:

- Modifica l'app generatrice di ricette per migliorarla ulteriormente. Gioca con i valori di temperatura e con i prompt per vedere cosa riesci a creare.
- Costruisci un "compagno di studio". Questa app dovrebbe essere in grado di rispondere a domande su un argomento, per esempio Python, potresti avere prompt come "Che cos'è un certo argomento in Python?", oppure potresti avere un prompt che dice, mostrami codice per un certo argomento ecc.
- Bot storico, fai rivivere la storia, istruisci il bot a impersonare un certo personaggio storico e fargli domande sulla sua vita e tempi.

## Soluzione

### Compagno di studio

Di seguito un prompt iniziale, vedi come puoi usarlo e modificarlo a tuo piacimento.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot storico

Ecco alcuni prompt che potresti usare:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Verifica delle conoscenze

Cosa fa il concetto di temperatura?

1. Controlla quanto casuale è l'output.
1. Controlla quanto è grande la risposta.
1. Controlla quanti token vengono usati.

## 🚀 Sfida

Mentre lavori al compito, cerca di variare la temperatura, prova a impostarla a 0, 0.5 e 1. Ricorda che 0 è la variazione minima e 1 è la massima. Quale valore funziona meglio per la tua app?

## Ottimo lavoro! Continua a imparare

Dopo aver completato questa lezione, dai un'occhiata alla nostra [collezione di apprendimento sull'IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) per continuare a migliorare le tue conoscenze sull'IA generativa!

Vai alla Lezione 7 dove vedremo come [costruire applicazioni di chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->