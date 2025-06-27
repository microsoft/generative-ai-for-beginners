<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:34:06+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fr"
}
-->
# Commencer avec ce cours

Nous sommes très enthousiastes à l'idée que vous commenciez ce cours et découvriez ce que vous serez inspiré de créer avec l'IA générative !

Pour garantir votre succès, cette page décrit les étapes de configuration, les exigences techniques, et où obtenir de l'aide si nécessaire.

## Étapes de configuration

Pour commencer ce cours, vous devrez suivre les étapes suivantes.

### 1. Forker ce dépôt

[Forkez l'ensemble de ce dépôt](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sur votre propre compte GitHub pour pouvoir modifier le code et relever les défis. Vous pouvez également [mettre une étoile (🌟) à ce dépôt](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pour le retrouver plus facilement ainsi que les dépôts connexes.

### 2. Créer un codespace

Pour éviter tout problème de dépendance lors de l'exécution du code, nous recommandons de suivre ce cours dans un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Cela peut être créé en sélectionnant l'option `Code` sur votre version forkée de ce dépôt et en choisissant l'option **Codespaces**.

![Dialogue montrant les boutons pour créer un codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Stocker vos clés API

Garder vos clés API sûres et sécurisées est important lors de la création de tout type d'application. Nous recommandons de ne pas stocker directement vos clés API dans votre code. Commettre ces détails dans un dépôt public pourrait entraîner des problèmes de sécurité et même des coûts indésirables si utilisés par un acteur malveillant. Voici un guide étape par étape sur comment créer un fichier `.env` pour Python et y ajouter le `GITHUB_TOKEN` :

1. **Naviguer vers votre répertoire de projet** : Ouvrez votre terminal ou invite de commande et naviguez jusqu'au répertoire racine de votre projet où vous souhaitez créer le fichier `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Créer le fichier `.env`** : Utilisez votre éditeur de texte préféré pour créer un nouveau fichier nommé `.env`. Si vous utilisez la ligne de commande, vous pouvez utiliser `touch` (on Unix-based systems) or `echo` (sous Windows) :

   Systèmes basés sur Unix :
   ```bash
   touch .env
   ```

   Windows :
   ```cmd
   echo . > .env
   ```

3. **Éditer le fichier `.env`** : Ouvrez le fichier `.env` dans un éditeur de texte (par exemple, VS Code, Notepad++, ou tout autre éditeur). Ajoutez la ligne suivante au fichier, en remplaçant `your_github_token_here` par votre véritable jeton GitHub :

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Enregistrer le fichier** : Enregistrez les modifications et fermez l'éditeur de texte.

5. **Installer le package `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` pour charger les variables d'environnement depuis le fichier `.env` dans votre application Python. Vous pouvez l'installer en utilisant `pip` :

   ```bash
   pip install python-dotenv
   ```

6. **Charger les variables d'environnement dans votre script Python** : Dans votre script Python, utilisez le package `python-dotenv` pour charger les variables d'environnement depuis le fichier `.env` :

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Voilà ! Vous avez créé avec succès un fichier `.env`, ajouté votre jeton GitHub, et l'avez chargé dans votre application Python.

## Comment exécuter localement sur votre ordinateur

Pour exécuter le code localement sur votre ordinateur, vous devez avoir une version de [Python installée](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pour ensuite utiliser le dépôt, vous devez le cloner :

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Une fois que vous avez tout vérifié, vous pouvez commencer !

## Étapes optionnelles

### Installer Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) est un installateur léger pour installer [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, ainsi que quelques packages. Conda est un gestionnaire de packages, qui facilite la configuration et le changement entre différents [**environnements virtuels**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python et packages. Il est également utile pour installer des packages qui ne sont pas disponibles via `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Allez-y et remplissez votre fichier d'environnement avec le fragment ci-dessous :

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

Si vous rencontrez des erreurs en utilisant conda, vous pouvez installer manuellement les bibliothèques Microsoft AI en utilisant la commande suivante dans un terminal.

```
conda install -c microsoft azure-ai-ml
```

Le fichier d'environnement spécifie les dépendances dont nous avons besoin. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` est la dernière version majeure de Python.

Avec cela, vous pouvez créer votre environnement Conda en exécutant les commandes ci-dessous dans votre ligne de commande/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consultez le [guide des environnements Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si vous rencontrez des problèmes.

### Utiliser Visual Studio Code avec l'extension de support Python

Nous recommandons d'utiliser l'éditeur [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) avec l'[extension de support Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installée pour ce cours. Cependant, c'est plus une recommandation qu'une exigence absolue.

> **Note** : En ouvrant le dépôt du cours dans VS Code, vous avez la possibilité de configurer le projet dans un conteneur. Cela est dû à la [répertoire spécial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) trouvé dans le dépôt du cours. Plus à ce sujet plus tard.

> **Note** : Une fois que vous clonez et ouvrez le répertoire dans VS Code, il vous suggérera automatiquement d'installer une extension de support Python.

> **Note** : Si VS Code vous suggère de rouvrir le dépôt dans un conteneur, déclinez cette demande pour utiliser la version de Python installée localement.

### Utiliser Jupyter dans le navigateur

Vous pouvez également travailler sur le projet en utilisant l'[environnement Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directement dans votre navigateur. Les Jupyter classiques et [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrent un environnement de développement agréable avec des fonctionnalités telles que l'auto-complétion, la mise en évidence du code, etc.

Pour démarrer Jupyter localement, rendez-vous sur le terminal/l'invite de commande, naviguez jusqu'au répertoire du cours, et exécutez :

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Cela lancera une instance Jupyter et l'URL pour y accéder sera affichée dans la fenêtre de la ligne de commande.

Une fois que vous accédez à l'URL, vous devriez voir le plan du cours et pouvoir naviguer vers n'importe quel fichier `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` où vous pouvez voir le code et les sorties.

## Utiliser le service Azure OpenAI pour la première fois

Si c'est la première fois que vous travaillez avec le service Azure OpenAI, veuillez suivre ce guide sur comment [créer et déployer une ressource du service Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Utiliser l'API OpenAI pour la première fois

Si c'est la première fois que vous travaillez avec l'API OpenAI, veuillez suivre le guide sur comment [créer et utiliser l'Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Rencontrer d'autres apprenants

Nous avons créé des canaux dans notre serveur Discord officiel de la communauté AI pour rencontrer d'autres apprenants. C'est un excellent moyen de réseauter avec d'autres entrepreneurs, constructeurs, étudiants, et toute personne cherchant à progresser en IA générative.

[![Rejoindre le canal discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

L'équipe de projet sera également présente sur ce serveur Discord pour aider les apprenants.

## Contribuer

Ce cours est une initiative open-source. Si vous voyez des domaines d'amélioration ou des problèmes, veuillez créer une [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou enregistrer un [problème GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

L'équipe de projet suivra toutes les contributions. Contribuer à l'open source est une manière incroyable de développer votre carrière en IA générative.

La plupart des contributions nécessitent que vous acceptiez un Accord de Licence de Contributeur (CLA) déclarant que vous avez le droit de et accordez effectivement les droits d'utiliser votre contribution. Pour plus de détails, visitez le [site de l'Accord de Licence de Contributeur (CLA)](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important : lorsque vous traduisez du texte dans ce dépôt, assurez-vous de ne pas utiliser la traduction automatique. Nous vérifierons les traductions via la communauté, donc veuillez ne vous porter volontaire pour des traductions que dans les langues où vous êtes compétent.

Lorsque vous soumettez une pull request, un CLA-bot déterminera automatiquement si vous devez fournir un CLA et décorera la PR de manière appropriée (par exemple, étiquette, commentaire). Suivez simplement les instructions fournies par le bot. Vous n'aurez besoin de le faire qu'une seule fois pour tous les dépôts utilisant notre CLA.

Ce projet a adopté le [Code de Conduite Open Source de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pour plus d'informations, lisez la FAQ du Code de Conduite ou contactez [Email opencode](opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Commençons

Maintenant que vous avez terminé les étapes nécessaires pour suivre ce cours, commençons par obtenir une [introduction à l'IA générative et aux LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Clause de non-responsabilité** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.