# Commencer avec ce cours

Nous sommes très enthousiastes à l'idée que vous commenciez ce cours et découvriez ce que vous serez inspiré à créer avec l'IA générative !

Pour garantir votre succès, cette page décrit les étapes de configuration, les exigences techniques et où obtenir de l'aide si nécessaire.

## Étapes de Configuration

Pour commencer ce cours, vous devrez compléter les étapes suivantes.

### 1. Forker ce Répertoire

[Forkez ce répertoire entier](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sur votre propre compte GitHub pour pouvoir modifier le code et relever les défis. Vous pouvez également [mettre une étoile (🌟) à ce répertoire](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pour le retrouver plus facilement ainsi que les répertoires associés.

### 2. Créer un codespace

Pour éviter tout problème de dépendance lors de l'exécution du code, nous recommandons de suivre ce cours dans un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Cela peut être créé en sélectionnant l'option `Code` sur votre version forkée de ce répertoire et en choisissant l'option **Codespaces**.

![Dialogue montrant les boutons pour créer un codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Stocker Vos Clés API

Il est important de garder vos clés API sûres et sécurisées lors de la création de tout type d'application. Nous recommandons de ne pas stocker de clés API directement dans votre code. Les commettre dans un dépôt public pourrait entraîner des problèmes de sécurité et même des coûts indésirables si elles sont utilisées par un acteur malveillant.

## Comment Exécuter Localement sur Votre Ordinateur

Pour exécuter le code localement sur votre ordinateur, vous devrez avoir une version de [Python installée](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Ensuite, pour utiliser le répertoire, vous devez le cloner :

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Une fois que tout est vérifié, vous pouvez commencer !

### Installer Miniconda (étape optionnelle)

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) est un installateur léger pour installer [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, ainsi que quelques packages.
Conda lui-même est un gestionnaire de paquets, qui facilite la configuration et le passage entre différents [**environnements virtuels**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python et packages. Il est également utile pour installer des packages qui ne sont pas disponibles via `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Allez-y et remplissez votre fichier d'environnement avec l'extrait ci-dessous :

```yml
name: <environment-name>
channels:
 - defaults
dependencies:
- python=<python-version>
- openai
- python-dotenv
- azure-ai-inference

```

Le fichier d'environnement spécifie les dépendances dont nous avons besoin. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` est la dernière version majeure de Python.

Avec cela fait, vous pouvez créer votre environnement Conda en exécutant les commandes ci-dessous dans votre ligne de commande/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consultez le [guide des environnements Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si vous rencontrez des problèmes.

### Utiliser Visual Studio Code avec l'extension de support Python

Nous recommandons d'utiliser l'éditeur [Visual Studio Code (VS Code)](http://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) avec l'[extension de support Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installée pour ce cours. Ceci est toutefois plus une recommandation qu'une exigence absolue.

> **Note** : En ouvrant le répertoire du cours dans VS Code, vous avez la possibilité de configurer le projet dans un conteneur. Cela est dû au [répertoire spécial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) trouvé dans le répertoire du cours. Plus d'informations à ce sujet plus tard.

> **Note** : Une fois que vous clonez et ouvrez le répertoire dans VS Code, il vous suggérera automatiquement d'installer une extension de support Python.

> **Note** : Si VS Code vous suggère de rouvrir le répertoire dans un conteneur, déclinez cette demande afin d'utiliser la version localement installée de Python.

### Utiliser Jupyter dans le Navigateur

Vous pouvez également travailler sur le projet en utilisant l'[environnement Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directement dans votre navigateur. Tant le Jupyter classique que le [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrent un environnement de développement agréable avec des fonctionnalités telles que l'auto-complétion, la mise en surbrillance du code, etc.

Pour démarrer Jupyter localement, rendez-vous dans le terminal/lignes de commande, naviguez vers le répertoire du cours, et exécutez :

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Cela lancera une instance Jupyter et l'URL pour y accéder sera affichée dans la fenêtre de ligne de commande.

Une fois que vous accédez à l'URL, vous devriez voir le plan du cours et pouvoir naviguer vers n'importe quel fichier `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` où vous pouvez voir le code et les sorties.

## Utiliser le Service Azure OpenAI pour la première fois

Si c'est la première fois que vous travaillez avec le service Azure OpenAI, veuillez suivre ce guide sur comment [créer et déployer une ressource de service Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Utiliser l'API OpenAI pour la première fois

Si c'est la première fois que vous travaillez avec l'API OpenAI, veuillez suivre le guide sur comment [créer et utiliser l'Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Rencontrer d'Autres Apprenants

Nous avons créé des canaux dans notre serveur Discord officiel de la [communauté AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pour rencontrer d'autres apprenants. C'est une excellente façon de réseauter avec d'autres entrepreneurs, créateurs, étudiants, et toute personne cherchant à progresser en IA générative.

[![Rejoindre le canal Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

L'équipe du projet sera également sur ce serveur Discord pour aider les apprenants.

## Contribuer

Ce cours est une initiative open-source. Si vous voyez des domaines à améliorer ou des problèmes, veuillez créer une [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou enregistrer un [problème GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

L'équipe du projet suivra toutes les contributions. Contribuer à l'open source est une façon incroyable de bâtir votre carrière en IA générative.

La plupart des contributions nécessitent que vous acceptiez un Accord de Licence de Contributeur (CLA) déclarant que vous avez le droit et que vous accordez effectivement les droits d'utiliser votre contribution. Pour plus de détails, visitez [le site web CLA, Accord de Licence de Contributeur](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important : lors de la traduction de texte dans ce dépôt, veuillez vous assurer de ne pas utiliser de traduction automatique. Nous vérifierons les traductions via la communauté, alors veuillez ne vous porter volontaire pour les traductions que dans les langues où vous êtes compétent.

Lorsque vous soumettez une pull request, un CLA-bot déterminera automatiquement si vous devez fournir un CLA et décorera le PR de manière appropriée (par exemple, étiquette, commentaire). Suivez simplement les instructions fournies par le bot. Vous n'aurez besoin de faire cela qu'une seule fois pour tous les dépôts utilisant notre CLA.

Ce projet a adopté le [Code de Conduite Open Source de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pour plus d'informations, lisez la FAQ sur le Code de Conduite ou contactez [Email opencode](opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Commençons

Maintenant que vous avez complété les étapes nécessaires pour suivre ce cours, commençons par obtenir une [introduction à l'IA générative et aux LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.