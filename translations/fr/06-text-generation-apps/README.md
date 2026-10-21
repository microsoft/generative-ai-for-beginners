# Création d'applications de génération de texte

[![Création d'applications de génération de texte](../../../translated_images/fr/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

Vous avez vu jusqu'à présent au cours de ce programme qu'il existe des concepts fondamentaux comme les prompts et même toute une discipline appelée "ingénierie des prompts". De nombreux outils avec lesquels vous pouvez interagir comme ChatGPT, Office 365, Microsoft Power Platform et plus encore, vous permettent d’utiliser des prompts pour accomplir quelque chose.

Pour ajouter une telle expérience à une application, vous devez comprendre des concepts comme les prompts, les complétions et choisir une bibliothèque avec laquelle travailler. C'est exactement ce que vous apprendrez dans ce chapitre.

## Introduction

Dans ce chapitre, vous allez :

- Découvrir la bibliothèque openai et ses concepts fondamentaux.
- Construire une application de génération de texte en utilisant openai.
- Comprendre comment utiliser des concepts tels que le prompt, la température, et les tokens pour construire une application de génération de texte.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Expliquer ce qu’est une application de génération de texte.
- Construire une application de génération de texte en utilisant openai.
- Configurer votre application pour utiliser plus ou moins de tokens et aussi modifier la température, afin d’obtenir un résultat varié.

## Qu'est-ce qu'une application de génération de texte ?

Normalement, lorsque vous créez une application, elle dispose d'une sorte d'interface comme les suivantes :

- Basée sur des commandes. Les applications console sont des applications typiques où vous tapez une commande et elle exécute une tâche. Par exemple, `git` est une application basée sur des commandes.
- Interface utilisateur (UI). Certaines applications disposent d’interfaces graphiques (GUI) où vous cliquez sur des boutons, saisissez du texte, sélectionnez des options et plus encore.

### Les applications Console et UI sont limitées

Comparez cela à une application basée sur des commandes où vous tapez une commande :

- **C'est limité**. Vous ne pouvez pas simplement taper n’importe quelle commande, seulement celles que l’application supporte.
- **Spécifique à une langue**. Certaines applications prennent en charge plusieurs langues, mais par défaut l’application est conçue pour une langue spécifique, même si vous pouvez ajouter plus de support linguistique.

### Avantages des applications de génération de texte

Alors, en quoi une application de génération de texte est-elle différente ?

Dans une application de génération de texte, vous avez plus de flexibilité, vous n’êtes pas limité à un ensemble de commandes ou à une langue d’entrée spécifique. Au lieu de cela, vous pouvez utiliser le langage naturel pour interagir avec l’application. Un autre avantage est que vous interagissez déjà avec une source de données qui a été entraînée sur un vaste corpus d’informations, alors qu’une application traditionnelle pourrait être limitée au contenu d’une base de données.

### Que puis-je construire avec une application de génération de texte ?

Vous pouvez créer beaucoup de choses. Par exemple :

- **Un chatbot**. Un chatbot répondant à des questions sur des sujets, comme votre entreprise et ses produits pourrait être un bon choix.
- **Assistant**. Les LLM sont excellents pour des taches telles que résumer du texte, obtenir des insights à partir de texte, produire du texte comme des CV et plus encore.
- **Assistant de code**. En fonction du modèle linguistique utilisé, vous pouvez créer un assistant de code qui vous aide à écrire du code. Par exemple, vous pouvez utiliser un produit comme GitHub Copilot ainsi que ChatGPT pour vous aider à coder.

## Comment démarrer ?

Eh bien, vous devez trouver un moyen d’intégrer un LLM, ce qui implique généralement deux approches principales :

- Utiliser une API. Ici, vous construisez des requêtes web avec votre prompt et récupérez le texte généré en retour.
- Utiliser une bibliothèque. Les bibliothèques aident à encapsuler les appels API et les rendent plus faciles à utiliser.

## Bibliothèques/SDKs

Il y a quelques bibliothèques bien connues pour travailler avec des LLM comme :

- **openai**, cette bibliothèque facilite la connexion à votre modèle et l’envoi de prompts.

Ensuite, il y a des bibliothèques qui opèrent à un niveau plus élevé comme :

- **Langchain**. Langchain est bien connu et supporte Python.
- **Semantic Kernel**. Semantic Kernel est une bibliothèque de Microsoft supportant les langages C#, Python, et Java.

## Première application utilisant openai

Voyons comment construire notre première application, quelles bibliothèques sont nécessaires, combien c’est requis et ainsi de suite.

### Installer openai

De nombreuses bibliothèques existent pour interagir avec OpenAI ou Azure OpenAI. Il est possible d’utiliser de nombreux langages de programmation aussi comme C#, Python, JavaScript, Java et plus. Nous avons choisi d’utiliser la bibliothèque Python `openai`, donc nous utiliserons `pip` pour l’installer.

```bash
pip install openai
```

### Créer une ressource

Vous devez réaliser les étapes suivantes :

- Créez un compte sur Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obtenez l’accès à Azure OpenAI. Rendez-vous sur [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) et demandez un accès.

  > [!NOTE]
  > Au moment de la rédaction, vous devez demander l’accès à Azure OpenAI.

- Installez Python <https://www.python.org/>
- Ayez créé une ressource Azure OpenAI Service. Consultez ce guide pour savoir comment [créer une ressource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Localiser la clé API et le point de terminaison

À ce stade, vous devez indiquer à votre bibliothèque `openai` quelle clé API utiliser. Pour trouver votre clé API, allez dans la section « Clés et point de terminaison » de votre ressource Azure OpenAI et copiez la valeur « Clé 1 ».

![Clés et panneau de ressource du point de terminaison dans Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Maintenant que vous avez copié ces informations, indiquons aux bibliothèques de l’utiliser.

> [!NOTE]
> Il est judicieux de séparer votre clé API de votre code. Vous pouvez le faire en utilisant des variables d’environnement.
>
> - Configurez la variable d’environnement `OPENAI_API_KEY` avec votre clé API.
>   `export OPENAI_API_KEY='sk-...'`

### Configuration pour Azure

Si vous utilisez Azure OpenAI (maintenant partie de Microsoft Foundry), voici comment configurer. Nous utilisons le client standard `OpenAI` pointé vers le point de terminaison Azure OpenAI `/openai/v1/`, qui fonctionne avec l’API Responses et ne nécessite pas de `api_version` :

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Ci-dessus, nous configurons les éléments suivants :

- `api_key`, c’est votre clé API trouvée dans le portail Azure ou Microsoft Foundry.
- `base_url`, c’est votre point de terminaison Foundry avec `/openai/v1/` ajouté. Le point de terminaison stable v1 fonctionne à la fois pour OpenAI et Azure OpenAI sans gestion de `api_version`.

> [!NOTE] > `os.environ` lit les variables d’environnement. Vous pouvez l’utiliser pour lire les variables d’environnement comme `AZURE_OPENAI_API_KEY` et `AZURE_OPENAI_ENDPOINT`. Configurez ces variables d’environnement dans votre terminal ou utilisez une bibliothèque comme `dotenv`.

## Génération de texte

La manière de générer du texte est d’utiliser l’API Responses via la méthode `responses.create`. Voici un exemple :

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Dans le code ci-dessus, nous créons une réponse et passons le modèle que nous voulons utiliser ainsi que le prompt. Ensuite, nous affichons le texte généré via `response.output_text`.

### Conversations à plusieurs tours

L'API Responses convient aussi bien pour la génération de texte à tour unique que pour les chatbots à plusieurs tours - vous fournissez une liste de messages dans `input` pour construire une conversation :

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Plus d’informations sur cette fonctionnalité dans un chapitre à venir.

## Exercice - votre première application de génération de texte

Maintenant que nous avons appris à configurer et configurer openai, il est temps de construire votre première application de génération de texte. Pour construire votre application, suivez les étapes suivantes :

1. Créez un environnement virtuel et installez openai :

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Si vous utilisez Windows, tapez `venv\Scripts\activate` au lieu de `source venv/bin/activate`.

   > [!NOTE]
   > Localisez votre clé Azure OpenAI en vous rendant sur [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), recherchez `Open AI`, sélectionnez `Open AI resource`, puis sélectionnez `Keys and Endpoint` et copiez la valeur `Key 1`.

1. Créez un fichier _app.py_ et donnez-lui le code suivant :

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
   > Si vous utilisez OpenAI pur (pas Azure), utilisez `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (pas de `base_url`) et passez un nom de modèle comme `gpt-5-mini` au lieu d’un nom de déploiement.

   Vous devriez voir une sortie comme la suivante :

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Différents types de prompts pour différentes choses

Maintenant que vous avez vu comment générer du texte en utilisant un prompt. Vous avez même un programme opérationnel que vous pouvez modifier et changer pour générer différents types de texte.

Les prompts peuvent être utilisés pour toutes sortes de tâches. Par exemple :

- **Générer un type de texte**. Par exemple, vous pouvez générer un poème, des questions pour un quiz, etc.
- **Consulter des informations**. Vous pouvez utiliser des prompts pour chercher des informations comme dans cet exemple : 'Que signifie CORS en développement web ?'.
- **Générer du code**. Vous pouvez utiliser des prompts pour générer du code, par exemple développer une expression régulière pour valider des emails ou pourquoi pas générer un programme complet, comme une application web ?

## Un cas d’utilisation plus pratique : un générateur de recettes

Imaginez que vous avez des ingrédients chez vous et que vous voulez cuisiner quelque chose. Pour cela, vous avez besoin d’une recette. Une manière de trouver des recettes est d’utiliser un moteur de recherche ou vous pourriez utiliser un LLM pour cela.

Vous pourriez écrire un prompt comme celui-ci :

> "Montre-moi 5 recettes pour un plat avec les ingrédients suivants : poulet, pommes de terre, et carottes. Par recette, liste tous les ingrédients utilisés."

Avec le prompt ci-dessus, vous pourriez obtenir une réponse similaire à :

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

Ce résultat est excellent, je sais quoi cuisiner. À ce stade, ce qui pourrait être des améliorations utiles sont :

- Filtrer les ingrédients que je n’aime pas ou auxquels je suis allergique.
- Produire une liste de courses, au cas où je n’aurais pas tous les ingrédients à la maison.

Pour les cas ci-dessus, ajoutons un prompt supplémentaire :

> "Veuillez retirer les recettes avec de l’ail car j’y suis allergique et remplacez-le par autre chose. Aussi, veuillez produire une liste de courses pour les recettes, en considérant que j’ai déjà du poulet, des pommes de terre et des carottes chez moi."

Maintenant, vous avez un nouveau résultat, à savoir :

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

Ce sont vos cinq recettes, sans mention d’ail et vous avez aussi une liste de courses tenant compte de ce que vous avez déjà à la maison.

## Exercice - créez un générateur de recettes

Maintenant que nous avons joué un scénario, écrivons du code correspondant au scénario démontré. Pour ce faire, suivez les étapes suivantes :

1. Utilisez le fichier _app.py_ existant comme point de départ
1. Localisez la variable `prompt` et changez son code pour ce qui suit :

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Si vous exécutez maintenant ce code, vous devriez voir une sortie similaire à :

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, votre LLM est non déterministe, donc vous pourriez obtenir des résultats différents chaque fois que vous exécutez le programme.

   Parfait, voyons comment nous pouvons améliorer les choses. Pour améliorer, nous voulons que le code soit flexible, donc les ingrédients et le nombre de recettes peuvent être améliorés et modifiés.

1. Changeons le code de la manière suivante :

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Prendre ce code pour un essai pourrait ressembler à ceci :

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Améliorer en ajoutant filtre et liste de courses

Nous avons maintenant une application fonctionnelle capable de produire des recettes et elle est flexible car elle s’appuie sur des entrées utilisateur, tant sur le nombre de recettes que sur les ingrédients utilisés.

Pour l'améliorer davantage, nous voulons ajouter ce qui suit :

- **Filtrer les ingrédients**. Nous voulons être capables de filtrer les ingrédients que nous n’aimons pas ou auxquels nous sommes allergiques. Pour réaliser ce changement, nous pouvons modifier notre prompt existant et ajouter une condition de filtre à la fin comme ceci :

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ci-dessus, nous ajoutons `{filter}` à la fin du prompt et nous capturons aussi la valeur du filtre donnée par l’utilisateur.

  Un exemple de saisie lors de l’exécution du programme pourrait ressembler à ceci :

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

  Comme vous pouvez le voir, toutes les recettes avec du lait ont été filtrées. Mais, si vous êtes intolérant au lactose, vous pourriez vouloir filtrer aussi les recettes avec du fromage, donc il faut être clair.

- **Produire une liste de courses**. Nous voulons générer une liste de courses, en tenant compte de ce que nous avons déjà à la maison.

  Pour cette fonctionnalité, nous pourrions soit essayer de tout résoudre dans un seul prompt, soit le diviser en deux prompts. Essayons la seconde approche. Ici, nous suggérons d’ajouter un prompt supplémentaire, mais pour que cela fonctionne, nous devons ajouter le résultat du premier prompt comme contexte au second prompt.

  Localisez la partie du code qui affiche le résultat du premier prompt et ajoutez le code suivant en dessous :

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Notez ce qui suit :

  1. Nous construisons un nouveau prompt en ajoutant le résultat du premier prompt au nouveau prompt :

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Nous faisons une nouvelle requête, mais en tenant compte aussi du nombre de tokens demandés dans le premier prompt, donc cette fois nous disons que `max_output_tokens` est 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     En testant ce code, nous obtenons maintenant la sortie suivante :

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

Ce que nous avons jusqu'à présent est un code qui fonctionne, mais il y a quelques ajustements que nous devrions faire pour améliorer davantage les choses. Certaines choses que nous devrions faire sont :

- **Séparer les secrets du code**, comme la clé API. Les secrets ne doivent pas se trouver dans le code et doivent être stockés dans un endroit sécurisé. Pour séparer les secrets du code, nous pouvons utiliser des variables d'environnement et des bibliothèques comme `python-dotenv` pour les charger à partir d'un fichier. Voici à quoi cela ressemblerait en code :

  1. Créez un fichier `.env` avec le contenu suivant :

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Notez que, pour Azure OpenAI dans Microsoft Foundry, vous devez définir les variables d'environnement suivantes à la place :

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     En code, vous chargeriez les variables d'environnement comme ceci :

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Un mot sur la longueur des tokens**. Nous devrions considérer combien de tokens nous avons besoin pour générer le texte souhaité. Les tokens coûtent de l'argent, donc lorsque cela est possible, nous devrions essayer d'être économiques avec le nombre de tokens utilisés. Par exemple, pouvons-nous formuler la requête de manière à utiliser moins de tokens ?

  Pour modifier le nombre de tokens utilisés, vous pouvez utiliser le paramètre `max_output_tokens`. Par exemple, si vous voulez utiliser 100 tokens, vous feriez :

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Expérimenter avec la température**. La température est quelque chose que nous n'avons pas encore mentionné, mais c'est un contexte important pour la performance de notre programme. Plus la valeur de température est élevée, plus la sortie sera aléatoire. À l'inverse, plus la température est basse, plus la sortie sera prévisible. Réfléchissez à la variation que vous souhaitez dans votre sortie.

  Pour modifier la température, vous pouvez utiliser le paramètre `temperature`. Par exemple, si vous voulez utiliser une température de 0,5, vous feriez :

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Notez, plus la valeur est proche de 1.0, plus la sortie est variée.

- **Les modèles de raisonnement n'utilisent pas `temperature`**. C'est un changement important en 2026. Les modèles actuels non dépréciés sur Microsoft Foundry sont des **modèles de raisonnement** (la famille GPT-5, série o) - et ils **ne prennent pas en charge `temperature` ni `top_p`** (ni `max_tokens` ; utilisez `max_output_tokens`). Si vous envoyez `temperature` à `gpt-5-mini`, vous obtiendrez une erreur "paramètre non supporté". Donc, pour essayer l'exemple de température ci-dessus, souvenez-vous de le pointer vers un modèle qui supporte encore les contrôles d'échantillonnage - par exemple un modèle ouvert **Llama** comme `Llama-3.3-70B-Instruct` du [catalogue des modèles Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), appelé via le point de terminaison Foundry Models / Azure AI Inference (de la même manière que les exemples `githubmodels-*`). Pour les modèles de raisonnement comme GPT-5, vous orientez la sortie différemment :
  - **Ingénierie des invites** - des instructions claires, des exemples et une sortie structurée (voir la leçon [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) font le travail que les réglages d'échantillonnage faisaient auparavant.
  - **Contrôles de raisonnement** - des paramètres comme l'effort de raisonnement/la verbosité échangent la profondeur du raisonnement contre la latence et le coût.

  En résumé : `temperature`/`top_p` sont encore valides sur beaucoup de modèles (Llama, Mistral, Phi, et la famille GPT-4.x - bien que GPT-4.x soit en dépréciation), mais la direction est l'ingénierie des invites + contrôles de raisonnement sur les modèles de raisonnement comme GPT-5.

## Exercice

Pour cet exercice, vous pouvez choisir ce que vous voulez construire.

Voici quelques suggestions :

- Améliorez davantage l'application génératrice de recettes. Testez différentes valeurs de température et modifiez les invites pour voir ce que vous pouvez créer.
- Construisez un "compagnon d'étude". Cette application doit pouvoir répondre à des questions sur un sujet, par exemple Python, vous pourriez avoir des invites comme "Qu'est-ce qu'un certain sujet en Python ?", ou une invite qui dit, montre-moi du code pour un certain sujet, etc.
- Bot historique, faites revivre l'histoire, demandez au bot d'incarner un certain personnage historique et posez-lui des questions sur sa vie et son époque.

## Solution

### Compagnon d'étude

Ci-dessous une invite de départ, voyez comment vous pouvez l’utiliser et la modifier à votre goût.

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

1. Il contrôle à quel point la sortie est aléatoire.
1. Il contrôle la taille de la réponse.
1. Il contrôle combien de tokens sont utilisés.

## 🚀 Défi

Lorsque vous travaillez sur l'exercice, essayez de varier la température, essayez de la définir à 0, 0,5 et 1. Rappelez-vous que 0 est le moins varié et 1 le plus. Quelle valeur fonctionne le mieux pour votre application ?

## Excellent travail ! Continuez votre apprentissage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à améliorer vos connaissances en IA générative !

Rendez-vous à la leçon 7 où nous verrons comment [construire des applications de chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) !

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->