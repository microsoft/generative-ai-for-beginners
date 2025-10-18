<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-17T22:36:41+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "fr"
}
-->
# Construire des applications de génération de texte

[![Construire des applications de génération de texte](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.fr.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

Vous avez vu jusqu'à présent dans ce programme que des concepts fondamentaux comme les invites et même une discipline entière appelée "ingénierie des invites" sont essentiels. De nombreux outils avec lesquels vous pouvez interagir, comme ChatGPT, Office 365, Microsoft Power Platform et bien d'autres, vous permettent d'utiliser des invites pour accomplir des tâches.

Pour ajouter une telle expérience à une application, vous devez comprendre des concepts comme les invites, les complétions et choisir une bibliothèque avec laquelle travailler. C'est exactement ce que vous apprendrez dans ce chapitre.

## Introduction

Dans ce chapitre, vous allez :

- Découvrir la bibliothèque openai et ses concepts fondamentaux.
- Construire une application de génération de texte en utilisant openai.
- Comprendre comment utiliser des concepts comme les invites, la température et les tokens pour créer une application de génération de texte.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Expliquer ce qu'est une application de génération de texte.
- Construire une application de génération de texte en utilisant openai.
- Configurer votre application pour utiliser plus ou moins de tokens et également modifier la température, pour obtenir des résultats variés.

## Qu'est-ce qu'une application de génération de texte ?

En général, lorsque vous créez une application, elle dispose d'une interface de type suivant :

- Basée sur des commandes. Les applications de console sont des applications typiques où vous tapez une commande et elle exécute une tâche. Par exemple, `git` est une application basée sur des commandes.
- Interface utilisateur (UI). Certaines applications ont des interfaces graphiques (GUI) où vous cliquez sur des boutons, saisissez du texte, sélectionnez des options, etc.

### Les applications de console et UI sont limitées

Comparez cela à une application basée sur des commandes où vous tapez une commande :

- **C'est limité**. Vous ne pouvez pas taper n'importe quelle commande, seulement celles que l'application prend en charge.
- **Spécifique à une langue**. Certaines applications prennent en charge plusieurs langues, mais par défaut, l'application est conçue pour une langue spécifique, même si vous pouvez ajouter la prise en charge d'autres langues.

### Avantages des applications de génération de texte

Alors, en quoi une application de génération de texte est-elle différente ?

Dans une application de génération de texte, vous avez plus de flexibilité, vous n'êtes pas limité à un ensemble de commandes ou à une langue d'entrée spécifique. Au lieu de cela, vous pouvez utiliser le langage naturel pour interagir avec l'application. Un autre avantage est que vous interagissez déjà avec une source de données qui a été formée sur un vaste corpus d'informations, alors qu'une application traditionnelle pourrait être limitée à ce qui se trouve dans une base de données.

### Que puis-je construire avec une application de génération de texte ?

Il y a de nombreuses choses que vous pouvez construire. Par exemple :

- **Un chatbot**. Un chatbot répondant à des questions sur des sujets, comme votre entreprise et ses produits, pourrait être une bonne idée.
- **Assistant**. Les LLM sont excellents pour des tâches comme résumer des textes, obtenir des informations à partir de textes, produire des textes comme des CV et bien plus encore.
- **Assistant de codage**. Selon le modèle linguistique que vous utilisez, vous pouvez créer un assistant de codage qui vous aide à écrire du code. Par exemple, vous pouvez utiliser un produit comme GitHub Copilot ainsi que ChatGPT pour vous aider à coder.

## Comment puis-je commencer ?

Eh bien, vous devez trouver un moyen d'intégrer un LLM, ce qui implique généralement les deux approches suivantes :

- Utiliser une API. Ici, vous construisez des requêtes web avec votre invite et obtenez du texte généré en retour.
- Utiliser une bibliothèque. Les bibliothèques aident à encapsuler les appels API et à les rendre plus faciles à utiliser.

## Bibliothèques/SDK

Il existe quelques bibliothèques bien connues pour travailler avec les LLM comme :

- **openai**, cette bibliothèque facilite la connexion à votre modèle et l'envoi d'invites.

Ensuite, il y a des bibliothèques qui fonctionnent à un niveau supérieur comme :

- **Langchain**. Langchain est bien connu et prend en charge Python.
- **Semantic Kernel**. Semantic Kernel est une bibliothèque de Microsoft prenant en charge les langages C#, Python et Java.

## Première application avec openai

Voyons comment nous pouvons créer notre première application, quelles bibliothèques nous avons besoin, ce qui est nécessaire, etc.

### Installer openai

Il existe de nombreuses bibliothèques pour interagir avec OpenAI ou Azure OpenAI. Il est possible d'utiliser de nombreux langages de programmation comme C#, Python, JavaScript, Java et bien d'autres. Nous avons choisi d'utiliser la bibliothèque Python `openai`, donc nous utiliserons `pip` pour l'installer.

```bash
pip install openai
```

### Créer une ressource

Vous devez effectuer les étapes suivantes :

- Créez un compte sur Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obtenez l'accès à Azure OpenAI. Rendez-vous sur [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) et demandez l'accès.

  > [!NOTE]
  > Au moment de la rédaction, vous devez demander l'accès à Azure OpenAI.

- Installez Python <https://www.python.org/>
- Créez une ressource Azure OpenAI Service. Consultez ce guide pour savoir [comment créer une ressource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Localiser la clé API et le point de terminaison

À ce stade, vous devez indiquer à votre bibliothèque `openai` quelle clé API utiliser. Pour trouver votre clé API, accédez à la section "Keys and Endpoint" de votre ressource Azure OpenAI et copiez la valeur "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Maintenant que vous avez copié ces informations, configurons les bibliothèques pour les utiliser.

> [!NOTE]
> Il est conseillé de séparer votre clé API de votre code. Vous pouvez le faire en utilisant des variables d'environnement.
>
> - Définissez la variable d'environnement `OPENAI_API_KEY` sur votre clé API.
>   `export OPENAI_API_KEY='sk-...'`

### Configurer Azure

Si vous utilisez Azure OpenAI, voici comment configurer la bibliothèque :

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Ci-dessus, nous configurons les éléments suivants :

- `api_type` sur `azure`. Cela indique à la bibliothèque d'utiliser Azure OpenAI et non OpenAI.
- `api_key`, c'est votre clé API trouvée dans le portail Azure.
- `api_version`, c'est la version de l'API que vous souhaitez utiliser. Au moment de la rédaction, la dernière version est `2023-05-15`.
- `api_base`, c'est le point de terminaison de l'API. Vous pouvez le trouver dans le portail Azure à côté de votre clé API.

> [!NOTE] > `os.getenv` est une fonction qui lit les variables d'environnement. Vous pouvez l'utiliser pour lire des variables d'environnement comme `OPENAI_API_KEY` et `API_BASE`. Définissez ces variables d'environnement dans votre terminal ou en utilisant une bibliothèque comme `dotenv`.

## Générer du texte

La manière de générer du texte est d'utiliser la classe `Completion`. Voici un exemple :

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

Dans le code ci-dessus, nous créons un objet de complétion et passons le modèle que nous voulons utiliser ainsi que l'invite. Ensuite, nous affichons le texte généré.

### Complétions de chat

Jusqu'à présent, vous avez vu comment nous avons utilisé `Completion` pour générer du texte. Mais il existe une autre classe appelée `ChatCompletion` qui est plus adaptée aux chatbots. Voici un exemple d'utilisation :

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Nous approfondirons cette fonctionnalité dans un chapitre à venir.

## Exercice - votre première application de génération de texte

Maintenant que nous avons appris à configurer et à utiliser openai, il est temps de créer votre première application de génération de texte. Pour créer votre application, suivez ces étapes :

1. Créez un environnement virtuel et installez openai :

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Si vous utilisez Windows, tapez `venv\Scripts\activate` au lieu de `source venv/bin/activate`.

   > [!NOTE]
   > Localisez votre clé Azure OpenAI en allant sur [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), recherchez `Open AI`, sélectionnez la ressource `Open AI` puis sélectionnez `Keys and Endpoint` et copiez la valeur `Key 1`.

1. Créez un fichier _app.py_ et ajoutez-y le code suivant :

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
   > Si vous utilisez Azure OpenAI, vous devez définir `api_type` sur `azure` et `api_key` sur votre clé Azure OpenAI.

   Vous devriez voir un résultat similaire à ce qui suit :

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Différents types d'invites pour différentes tâches

Vous avez maintenant vu comment générer du texte en utilisant une invite. Vous avez même une application fonctionnelle que vous pouvez modifier et changer pour générer différents types de texte.

Les invites peuvent être utilisées pour toutes sortes de tâches. Par exemple :

- **Générer un type de texte**. Par exemple, vous pouvez générer un poème, des questions pour un quiz, etc.
- **Rechercher des informations**. Vous pouvez utiliser des invites pour rechercher des informations comme l'exemple suivant : "Que signifie CORS en développement web ?".
- **Générer du code**. Vous pouvez utiliser des invites pour générer du code, par exemple développer une expression régulière utilisée pour valider des emails ou même générer un programme entier, comme une application web.

## Un cas d'utilisation plus pratique : un générateur de recettes

Imaginez que vous avez des ingrédients chez vous et que vous voulez cuisiner quelque chose. Pour cela, vous avez besoin d'une recette. Une façon de trouver des recettes est d'utiliser un moteur de recherche ou vous pourriez utiliser un LLM.

Vous pourriez écrire une invite comme celle-ci :

> "Montrez-moi 5 recettes pour un plat avec les ingrédients suivants : poulet, pommes de terre et carottes. Pour chaque recette, listez tous les ingrédients utilisés."

Avec l'invite ci-dessus, vous pourriez obtenir une réponse similaire à :

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

Ce résultat est excellent, je sais quoi cuisiner. À ce stade, ce qui pourrait être utile comme améliorations sont :

- Filtrer les ingrédients que je n'aime pas ou auxquels je suis allergique.
- Produire une liste de courses, au cas où je n'aurais pas tous les ingrédients chez moi.

Pour les cas ci-dessus, ajoutons une invite supplémentaire :

> "Veuillez supprimer les recettes contenant de l'ail car je suis allergique et remplacez-le par autre chose. De plus, veuillez produire une liste de courses pour les recettes, en tenant compte du fait que j'ai déjà du poulet, des pommes de terre et des carottes chez moi."

Vous avez maintenant un nouveau résultat, à savoir :

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

Voici vos cinq recettes, sans mention d'ail, et vous avez également une liste de courses en tenant compte de ce que vous avez déjà chez vous.

## Exercice - construire un générateur de recettes

Maintenant que nous avons exploré un scénario, écrivons du code pour correspondre au scénario démontré. Pour ce faire, suivez ces étapes :

1. Utilisez le fichier _app.py_ existant comme point de départ.
1. Localisez la variable `prompt` et modifiez son code comme suit :

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Si vous exécutez maintenant le code, vous devriez voir un résultat similaire à :

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, votre LLM est non déterministe, donc vous pourriez obtenir des résultats différents à chaque exécution du programme.

   Excellent, voyons comment nous pouvons améliorer les choses. Pour améliorer les choses, nous voulons nous assurer que le code est flexible, afin que les ingrédients et le nombre de recettes puissent être modifiés et ajustés.

1. Modifiez le code de la manière suivante :

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Exécuter le code pourrait ressembler à ceci :

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Améliorer en ajoutant un filtre et une liste de courses

Nous avons maintenant une application fonctionnelle capable de produire des recettes et elle est flexible car elle repose sur les entrées de l'utilisateur, tant sur le nombre de recettes que sur les ingrédients utilisés.

Pour aller plus loin, nous voulons ajouter les éléments suivants :

- **Filtrer les ingrédients**. Nous voulons pouvoir filtrer les ingrédients que nous n'aimons pas ou auxquels nous sommes allergiques. Pour effectuer ce changement, nous pouvons modifier notre invite existante et ajouter une condition de filtre à la fin comme suit :

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ci-dessus, nous ajoutons `{filter}` à la fin de l'invite et nous capturons également la valeur du filtre auprès de l'utilisateur.

  Un exemple d'entrée lors de l'exécution du programme pourrait maintenant ressembler à ceci :

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

  Comme vous pouvez le voir, toutes les recettes contenant du lait ont été filtrées. Mais, si vous êtes intolérant au lactose, vous pourriez également vouloir filtrer les recettes contenant du fromage, donc il est nécessaire d'être précis.

- **Produire une liste de courses**. Nous voulons produire une liste de courses, en tenant compte de ce que nous avons déjà chez nous.

  Pour cette fonctionnalité, nous pourrions soit essayer de tout résoudre dans une seule invite, soit diviser cela en deux invites. Essayons la deuxième approche. Ici, nous suggérons d'ajouter une invite supplémentaire, mais pour que cela fonctionne, nous devons ajouter le résultat de la première invite comme contexte à la deuxième invite.

  Localisez la partie du code qui affiche le résultat de la première invite et ajoutez le code suivant ci-dessous :
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

  Notez les points suivants :

  1. Nous construisons une nouvelle invite en ajoutant le résultat de la première invite à la nouvelle invite :

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Nous faisons une nouvelle requête, tout en prenant en compte le nombre de tokens demandés dans la première invite. Cette fois, nous définissons `max_tokens` à 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     En testant ce code, nous obtenons maintenant le résultat suivant :

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Améliorez votre configuration

Ce que nous avons jusqu'à présent est un code fonctionnel, mais il y a quelques ajustements que nous devrions faire pour améliorer les choses davantage. Voici quelques suggestions :

- **Séparer les secrets du code**, comme la clé API. Les secrets ne doivent pas être inclus dans le code et doivent être stockés dans un endroit sécurisé. Pour séparer les secrets du code, nous pouvons utiliser des variables d'environnement et des bibliothèques comme `python-dotenv` pour les charger depuis un fichier. Voici à quoi cela ressemblerait dans le code :

  1. Créez un fichier `.env` avec le contenu suivant :

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Notez que pour Azure, vous devez définir les variables d'environnement suivantes :

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     Dans le code, vous chargeriez les variables d'environnement comme ceci :

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Un mot sur la longueur des tokens**. Nous devrions réfléchir au nombre de tokens nécessaires pour générer le texte souhaité. Les tokens ont un coût, donc, dans la mesure du possible, nous devrions essayer d'être économes avec le nombre de tokens utilisés. Par exemple, pouvons-nous formuler l'invite de manière à utiliser moins de tokens ?

  Pour modifier le nombre de tokens utilisés, vous pouvez utiliser le paramètre `max_tokens`. Par exemple, si vous souhaitez utiliser 100 tokens, vous feriez :

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Expérimenter avec la température**. La température est un paramètre que nous n'avons pas encore mentionné, mais qui est important pour le fonctionnement de notre programme. Plus la valeur de la température est élevée, plus le résultat sera aléatoire. À l'inverse, plus la température est basse, plus le résultat sera prévisible. Réfléchissez à si vous souhaitez ou non de la variation dans votre résultat.

  Pour modifier la température, vous pouvez utiliser le paramètre `temperature`. Par exemple, si vous souhaitez utiliser une température de 0,5, vous feriez :

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Notez que plus la valeur est proche de 1,0, plus le résultat sera varié.

## Exercice

Pour cet exercice, vous pouvez choisir ce que vous souhaitez créer.

Voici quelques suggestions :

- Améliorez l'application génératrice de recettes. Expérimentez avec les valeurs de température et les invites pour voir ce que vous pouvez obtenir.
- Créez un "compagnon d'étude". Cette application devrait être capable de répondre à des questions sur un sujet, par exemple Python. Vous pourriez avoir des invites comme "Qu'est-ce qu'un certain sujet en Python ?", ou une invite qui dit "Montrez-moi du code pour un certain sujet", etc.
- Bot historique, donnez vie à l'histoire, demandez au bot de jouer un personnage historique particulier et posez-lui des questions sur sa vie et son époque.

## Solution

### Compagnon d'étude

Voici une invite de départ, voyez comment vous pouvez l'utiliser et l'adapter à votre goût.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot historique

Voici quelques invites que vous pourriez utiliser :

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Vérification des connaissances

Que fait le concept de température ?

1. Il contrôle à quel point le résultat est aléatoire.
1. Il contrôle la taille de la réponse.
1. Il contrôle le nombre de tokens utilisés.

## 🚀 Défi

En travaillant sur l'exercice, essayez de varier la température, en la réglant à 0, 0,5 et 1. Rappelez-vous que 0 est le moins varié et 1 est le plus varié. Quelle valeur fonctionne le mieux pour votre application ?

## Excellent travail ! Continuez votre apprentissage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances sur l'IA générative !

Passez à la leçon 7 où nous verrons comment [créer des applications de chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) !

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.