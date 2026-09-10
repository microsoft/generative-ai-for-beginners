# Création d'applications de génération de texte

[![Création d'applications de génération de texte](../../../translated_images/fr/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

Vous avez déjà vu dans ce programme qu'il existe des concepts fondamentaux comme les invites et même une discipline entière appelée « ingénierie des invites ». De nombreux outils avec lesquels vous pouvez interagir comme ChatGPT, Office 365, Microsoft Power Platform et d'autres, vous assistent en utilisant des invites pour accomplir quelque chose.

Pour ajouter une telle expérience à une application, vous devez comprendre des concepts comme les invites, les complétions et choisir une bibliothèque avec laquelle travailler. C'est exactement ce que vous apprendrez dans ce chapitre.

## Introduction

Dans ce chapitre, vous allez :

- Découvrir la bibliothèque openai et ses concepts clés.
- Créer une application de génération de texte en utilisant openai.
- Comprendre comment utiliser des concepts tels que prompt, température, et tokens pour construire une application de génération de texte.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Expliquer ce qu'est une application de génération de texte.
- Créer une application de génération de texte en utilisant openai.
- Configurer votre application pour utiliser plus ou moins de tokens et aussi changer la température, pour un rendu varié.

## Qu'est-ce qu'une application de génération de texte ?

Normalement, lorsque vous créez une application, elle dispose d'une sorte d'interface comme suit :

- Basée sur des commandes. Les applications console sont des applications typiques où vous tapez une commande et elle effectue une tâche. Par exemple, `git` est une application basée sur des commandes.
- Interface utilisateur (IU). Certaines applications possèdent une interface utilisateur graphique (GUI) où vous cliquez sur des boutons, saisissez du texte, sélectionnez des options, etc.

### Les applications console et IU sont limitées

Comparez cela à une application basée sur des commandes où vous tapez une commande :

- **C'est limité**. Vous ne pouvez pas simplement taper n'importe quelle commande, seulement celles que l'application supporte.
- **Spécifique à une langue**. Certaines applications supportent plusieurs langues, mais par défaut l'application est construite pour une langue spécifique, même si vous pouvez ajouter un support pour d'autres langues.

### Avantages des applications de génération de texte

Alors, comment une application de génération de texte est-elle différente ?

Dans une application de génération de texte, vous avez plus de flexibilité, vous n'êtes pas limité à un ensemble de commandes ou à une langue d'entrée spécifique. À la place, vous pouvez utiliser le langage naturel pour interagir avec l'application. Un autre avantage est que vous interagissez déjà avec une source de données qui a été entraînée sur un vaste corpus d’informations, alors qu'une application traditionnelle pourrait être limitée à ce qui se trouve dans une base de données.

### Que puis-je créer avec une application de génération de texte ?

Il y a beaucoup de choses que vous pouvez construire. Par exemple :

- **Un chatbot**. Un chatbot répondant aux questions sur des sujets, comme votre entreprise et ses produits, pourrait bien convenir.
- **Assistant**. Les grands modèles de langage (LLM) sont excellents pour des tâches comme résumer du texte, obtenir des insights à partir du texte, produire du texte comme des CV, et plus encore.
- **Assistant de code**. Selon le modèle de langage que vous utilisez, vous pouvez créer un assistant de code qui vous aide à écrire du code. Par exemple, vous pouvez utiliser un produit comme GitHub Copilot ainsi que ChatGPT pour vous aider à coder.

## Comment puis-je commencer ?

Eh bien, vous devez trouver un moyen d'intégrer un LLM, ce qui implique généralement deux approches :

- Utiliser une API. Ici, vous construisez des requêtes web avec votre invite et recevez du texte généré en retour.
- Utiliser une bibliothèque. Les bibliothèques aident à encapsuler les appels API et les rendent plus faciles à utiliser.

## Bibliothèques/SDK

Il existe quelques bibliothèques bien connues pour travailler avec des LLM comme :

- **openai**, cette bibliothèque facilite la connexion à votre modèle et l'envoi d'invites.

Ensuite, il y a des bibliothèques qui opèrent à un niveau supérieur comme :

- **Langchain**. Langchain est bien connu et supporte Python.
- **Semantic Kernel**. Semantic Kernel est une bibliothèque de Microsoft supportant les langages C#, Python et Java.

## Première application avec openai

Voyons comment construire notre première application, quelles bibliothèques nous devons utiliser, ce qui est requis, etc.

### Installer openai

Il existe de nombreuses bibliothèques pour interagir avec OpenAI ou Azure OpenAI. Il est également possible d’utiliser plusieurs langages de programmation comme C#, Python, JavaScript, Java et d’autres. Nous avons choisi d’utiliser la bibliothèque Python `openai`, donc nous utiliserons `pip` pour l’installer.

```bash
pip install openai
```

### Créer une ressource

Vous devez effectuer les étapes suivantes :

- Créez un compte sur Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obtenez l’accès à Azure OpenAI. Rendez-vous sur [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) et demandez l’accès.

  > [!NOTE]
  > Au moment de la rédaction, vous devez faire une demande d’accès à Azure OpenAI.

- Installez Python <https://www.python.org/>
- Ayez créé une ressource Azure OpenAI Service. Consultez ce guide pour savoir comment [créer une ressource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Localiser la clé API et le point de terminaison

À ce stade, vous devez indiquer à votre bibliothèque `openai` quelle clé API utiliser. Pour trouver votre clé API, allez dans la section "Clés et point de terminaison" de votre ressource Azure OpenAI et copiez la valeur "Clé 1".

![Clés et point de terminaison dans Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Maintenant que vous avez copié cette information, indiquons aux bibliothèques de l’utiliser.

> [!NOTE]
> Il est conseillé de séparer votre clé API de votre code. Vous pouvez le faire en utilisant des variables d’environnement.
>
> - Définissez la variable d’environnement `OPENAI_API_KEY` avec votre clé API.
>   `export OPENAI_API_KEY='sk-...'`

### Configurer Azure

Si vous utilisez Azure OpenAI (maintenant partie de Microsoft Foundry), voici comment configurer. Nous utilisons le client standard `OpenAI` pointant vers le point de terminaison Azure OpenAI `/openai/v1/`, qui fonctionne avec l’API Responses et ne nécessite pas de `api_version` :

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Ci-dessus, nous définissons les éléments suivants :

- `api_key`, c’est votre clé API trouvée dans le portail Azure ou le portail Microsoft Foundry.
- `base_url`, c’est l’URL de votre ressource Foundry avec `/openai/v1/` ajouté. Le point de terminaison stable v1 fonctionne sur OpenAI et Azure OpenAI sans gestion de `api_version`.

> [!NOTE] > `os.environ` lit les variables d’environnement. Vous pouvez l’utiliser pour lire les variables d’environnement telles que `AZURE_OPENAI_API_KEY` et `AZURE_OPENAI_ENDPOINT`. Définissez ces variables d’environnement dans votre terminal ou en utilisant une bibliothèque comme `dotenv`.

## Générer du texte

La manière de générer du texte est d’utiliser l’API Responses via la méthode `responses.create`. Voici un exemple :

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # ceci est le nom de votre déploiement de modèle
    input=prompt,
    store=False,
)
print(response.output_text)
```

Dans le code ci-dessus, nous créons une réponse et passons le modèle que nous voulons utiliser ainsi que le prompt. Puis nous affichons le texte généré via `response.output_text`.

### Conversations à plusieurs tours

L’API Responses est bien adaptée à la fois pour la génération de texte en un seul tour et aux chatbots multi-tours - vous fournissez une liste de messages dans `input` pour construire une conversation :

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Plus de détails sur cette fonctionnalité dans un chapitre à venir.

## Exercice - votre première application de génération de texte

Maintenant que nous avons appris à configurer et paramétrer openai, il est temps de créer votre première application de génération de texte. Pour construire votre application, suivez ces étapes :

1. Créez un environnement virtuel et installez openai :

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Si vous utilisez Windows, tapez `venv\Scripts\activate` au lieu de `source venv/bin/activate`.

   > [!NOTE]
   > Localisez votre clé Azure OpenAI en allant sur [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) puis cherchez `Open AI`, sélectionnez la `ressource Open AI` puis accédez à `Clés et point de terminaison` et copiez la valeur `Clé 1`.

1. Créez un fichier _app.py_ et mettez-y le code suivant :

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # ajoutez votre code de complétion
   prompt = "Complete the following: Once upon a time there was a"

   # faites une requête en utilisant l'API Responses
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # affichez la réponse
   print(response.output_text)
   ```

   > [!NOTE]
   > Si vous utilisez OpenAI classique (pas Azure), utilisez `client = OpenAI(api_key="<remplacez cette valeur par votre clé OpenAI>")` (sans `base_url`) et passez un nom de modèle comme `gpt-5-mini` au lieu d’un nom de déploiement.

   Vous devriez voir une sortie comme la suivante :

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Différents types d'invites, selon les besoins

Maintenant que vous avez vu comment générer du texte avec une invite, vous avez même un programme opérationnel que vous pouvez modifier pour générer différents types de texte.

Les invites peuvent être utilisées pour toutes sortes de tâches. Par exemple :

- **Générer un type de texte**. Par exemple, vous pouvez générer un poème, des questions pour un quiz, etc.
- **Rechercher des informations**. Vous pouvez utiliser des invites pour chercher des informations comme dans l’exemple suivant « Que signifie CORS en développement web ? ».
- **Générer du code**. Vous pouvez utiliser des invites pour générer du code, par exemple développer une expression régulière pour valider des emails ou pourquoi pas générer un programme entier, comme une application web ?

## Un cas d'utilisation plus pratique : un générateur de recettes

Imaginez que vous avez des ingrédients à la maison et que vous voulez cuisiner quelque chose. Pour cela, vous avez besoin d'une recette. Une manière de trouver des recettes est d'utiliser un moteur de recherche ou vous pourriez utiliser un LLM pour cela.

Vous pourriez écrire une invite comme ceci :

> « Montre-moi 5 recettes pour un plat avec les ingrédients suivants : poulet, pommes de terre et carottes. Pour chaque recette, liste tous les ingrédients utilisés »

Avec cette invite, vous pourriez obtenir une réponse similaire à :

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

Ce résultat est formidable, je sais quoi cuisiner. À ce stade, ce qui pourrait être des améliorations utiles sont :

- Filtrer les ingrédients que je n’aime pas ou auxquels je suis allergique.
- Produire une liste de courses, au cas où je n’aurais pas tous les ingrédients chez moi.

Pour les cas ci-dessus, ajoutons une invite supplémentaire :

> « Veuillez supprimer les recettes contenant de l'ail car j'y suis allergique et remplacez-le par autre chose. Aussi, veuillez produire une liste de courses pour les recettes, en tenant compte du fait que j’ai déjà du poulet, des pommes de terre et des carottes chez moi. »

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

Voilà vos cinq recettes, sans ail mentionné et vous avez aussi une liste de courses en tenant compte de vos ingrédients déjà disponibles.

## Exercice - créer un générateur de recettes

Maintenant que nous avons simulé un scénario, écrivons un code correspondant au scénario démontré. Pour ce faire, suivez ces étapes :

1. Utilisez le fichier _app.py_ existant comme point de départ
1. Localisez la variable `prompt` et modifiez son code comme suit :

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Si vous exécutez maintenant le code, vous devriez voir une sortie similaire à :

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, votre LLM est non déterministe, vous pouvez donc obtenir des résultats différents à chaque exécution du programme.

   Super, voyons comment améliorer les choses. Pour cela, nous voulons que le code soit flexible, de sorte que les ingrédients et le nombre de recettes puissent être améliorés et modifiés.

1. Modifions le code de la manière suivante :

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpoler le nombre de recettes dans la consigne et les ingrédients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Une exécution de test du code pourrait ressembler à ceci :

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Améliorer en ajoutant filtre et liste de courses

Nous avons maintenant une application fonctionnelle capable de produire des recettes et elle est flexible car elle repose sur des entrées utilisateur, à la fois concernant le nombre de recettes et les ingrédients utilisés.

Pour l’améliorer encore, nous voulons ajouter ce qui suit :

- **Filtrer les ingrédients**. Nous voulons pouvoir filtrer les ingrédients que nous n’aimons pas ou auxquels nous sommes allergiques. Pour accomplir ce changement, nous pouvons modifier notre invite existante et ajouter une condition de filtre à la fin comme ceci :

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ci-dessus, nous ajoutons `{filter}` à la fin de l’invite et capturons aussi la valeur du filtre depuis l’utilisateur.

  Un exemple d’entrée lors de l’exécution du programme pourrait maintenant ressembler à ceci :

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

  Comme vous pouvez le voir, toutes les recettes contenant du lait ont été filtrées. Mais, si vous êtes intolérant au lactose, vous voudrez peut-être aussi filtrer les recettes contenant du fromage, donc il y a besoin d’être précis.


- **Produire une liste de courses**. Nous voulons produire une liste de courses, en tenant compte de ce que nous avons déjà à la maison.

  Pour cette fonctionnalité, nous pourrions soit essayer de tout résoudre en une seule requête, soit la diviser en deux requêtes. Essayons la deuxième approche. Ici, nous suggérons d’ajouter une requête supplémentaire, mais pour que cela fonctionne, nous devons ajouter le résultat de la première requête comme contexte à la seconde requête.

  Localisez la partie du code qui affiche le résultat de la première requête et ajoutez le code suivant en dessous :

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # afficher la réponse
  print("Shopping list:")
  print(response.output_text)
  ```

  Notez ce qui suit :

  1. Nous construisons une nouvelle requête en ajoutant le résultat de la première requête à la nouvelle requête :

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Nous faisons une nouvelle requête, mais en tenant aussi compte du nombre de tokens que nous avons demandé dans la première requête, cette fois nous mettons `max_output_tokens` à 1200.

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

Ce que nous avons jusqu’à présent est un code qui fonctionne, mais quelques ajustements devraient être faits pour améliorer davantage. Voici quelques points à appliquer :

- **Séparez les secrets du code**, comme la clé API. Les secrets ne doivent pas se trouver dans le code et doivent être stockés en lieu sûr. Pour séparer les secrets du code, nous pouvons utiliser des variables d’environnement et des bibliothèques comme `python-dotenv` pour les charger depuis un fichier. Voici comment cela se présente dans le code :

  1. Créez un fichier `.env` avec le contenu suivant :

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Notez que, pour Azure OpenAI dans Microsoft Foundry, vous devez plutôt définir les variables d’environnement suivantes :

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     En code, vous chargeriez ainsi les variables d’environnement :

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Un mot sur la longueur des tokens**. Nous devons considérer combien de tokens sont nécessaires pour générer le texte souhaité. Les tokens coûtent de l’argent, donc, autant que possible, il faut essayer d’économiser sur le nombre de tokens utilisés. Par exemple, pouvons-nous formuler la requête pour utiliser moins de tokens ?

  Pour modifier le nombre de tokens utilisés, vous pouvez utiliser le paramètre `max_output_tokens`. Par exemple, si vous voulez utiliser 100 tokens, vous faites :

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Expérimenter la température**. La température est quelque chose que nous n’avons pas encore mentionné, mais c’est un contexte important pour la performance de notre programme. Plus la température est élevée, plus la sortie sera aléatoire. À l’inverse, plus la température est basse, plus la sortie sera prévisible. Réfléchissez à si vous voulez de la variation dans votre sortie ou non.

  Pour modifier la température, vous pouvez utiliser le paramètre `temperature`. Par exemple, si vous voulez une température de 0,5, vous faites :

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Notez que plus la valeur est proche de 1.0, plus la sortie est variée.

- **Les modèles de raisonnement n'utilisent pas la `temperature`**. Il s’agit d’un changement important pour 2026. Les modèles actuels non obsolètes sur Microsoft Foundry sont des **modèles de raisonnement** (famille GPT-5, série o) - et ils **ne supportent pas `temperature` ou `top_p`** (ni `max_tokens`; utilisez `max_output_tokens`). Si vous envoyez `temperature` à `gpt-5-mini`, vous obtiendrez une erreur "paramètre non supporté". Pour essayer l’exemple de température ci-dessus, orientez-vous vers un modèle qui supporte encore les contrôles d’échantillonnage - par exemple un modèle ouvert **Llama** comme `Llama-3.3-70B-Instruct` du [catalogue de modèles Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), appelé via l’endpoint Foundry Models / Azure AI Inference (de la même manière que les échantillons `githubmodels-*`). Pour les modèles de raisonnement comme GPT-5, vous dirigez la sortie différemment :
  - **Engineering des requêtes** - des instructions claires, des exemples, et une sortie structurée (voir la leçon [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) font le travail que faisaient les réglages d’échantillonnage.
  - **Contrôles de raisonnement** - des paramètres comme effort de raisonnement / verbosité qui échangent profondeur de raisonnement contre latence et coût.

  En résumé : `temperature`/`top_p` sont encore valides sur de nombreux modèles (Llama, Mistral, Phi, et la famille GPT-4.x - bien que GPT-4.x soit en cours de dépréciation), mais la tendance est à l’ingénierie des requêtes + contrôles de raisonnement sur les modèles de raisonnement comme GPT-5.

## Devoir

Pour ce devoir, vous pouvez choisir ce que vous voulez construire.

Voici quelques suggestions :

- Améliorez l’application génératrice de recettes pour la rendre encore meilleure. Essayez différentes valeurs de température et modifiez les requêtes pour voir ce que vous pouvez obtenir.
- Créez un "partenaire d’étude". Cette application devrait pouvoir répondre à des questions sur un sujet, par exemple Python, vous pourriez avoir des requêtes comme "Qu’est-ce qu’un certain sujet en Python ?", ou une requête qui dit, montre-moi du code pour un certain sujet, etc.
- Un bot historique, faites revivre l’histoire, demandez au bot d'incarner un certain personnage historique et posez-lui des questions sur sa vie et son époque.

## Solution

### Partenaire d’étude

Voici une requête de départ, voyez comment vous pouvez l’utiliser et la modifier à votre goût.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot historique

Voici quelques requêtes que vous pourriez utiliser :

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Vérification des connaissances

Que fait le concept de température ?

1. Il contrôle le degré d'aléa dans la sortie.
1. Il contrôle la taille de la réponse.
1. Il contrôle le nombre de tokens utilisés.

## 🚀 Défi

En travaillant sur le devoir, essayez de varier la température, essayez de la régler à 0, 0,5 et 1. Rappelez-vous que 0 est la sortie la moins variée et 1 la plus variée. Quelle valeur fonctionne le mieux pour votre application ?

## Excellent travail ! Continuez votre apprentissage

Après avoir terminé cette leçon, consultez notre [collection d’apprentissage sur l’IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances sur l’IA générative !

Rendez-vous à la Leçon 7 où nous verrons comment [construire des applications de chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) !

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->