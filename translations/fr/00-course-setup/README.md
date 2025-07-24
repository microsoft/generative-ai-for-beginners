<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T06:57:56+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fr"
}
-->
# Bien démarrer avec ce cours

Nous sommes très enthousiastes à l’idée que vous commenciez ce cours et découvriez ce que vous serez inspiré à créer avec l’IA générative !

Pour vous assurer de réussir, cette page décrit les étapes d’installation, les exigences techniques, ainsi que les ressources d’aide en cas de besoin.

## Étapes d’installation

Pour commencer ce cours, vous devrez suivre les étapes suivantes.

### 1. Forker ce dépôt

[Forkez ce dépôt complet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sur votre propre compte GitHub afin de pouvoir modifier le code et relever les défis. Vous pouvez aussi [étoiler (🌟) ce dépôt](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pour le retrouver plus facilement, ainsi que les dépôts associés.

### 2. Créer un codespace

Pour éviter tout problème de dépendances lors de l’exécution du code, nous recommandons d’utiliser ce cours dans un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Vous pouvez créer un codespace en sélectionnant l’option `Code` sur votre version forkée de ce dépôt, puis en choisissant l’option **Codespaces**.

![Dialogue montrant les boutons pour créer un codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Stocker vos clés API

Il est important de garder vos clés API en sécurité lorsque vous développez une application. Nous vous recommandons de ne pas stocker vos clés API directement dans votre code. Les inclure dans un dépôt public peut entraîner des problèmes de sécurité et même des coûts non désirés si elles sont utilisées par une personne malveillante.  
Voici un guide étape par étape pour créer un fichier `.env` en Python et y ajouter le `GITHUB_TOKEN` :

1. **Accédez au répertoire de votre projet** : Ouvrez votre terminal ou invite de commandes et placez-vous à la racine de votre projet où vous souhaitez créer le fichier `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Créez le fichier `.env`** : Utilisez votre éditeur de texte préféré pour créer un nouveau fichier nommé `.env`. En ligne de commande, vous pouvez utiliser `touch` (sur systèmes Unix) ou `echo` (sur Windows) :

   Systèmes Unix :

   ```bash
   touch .env
   ```

   Windows :

   ```cmd
   echo . > .env
   ```

3. **Modifiez le fichier `.env`** : Ouvrez le fichier `.env` dans un éditeur de texte (par exemple VS Code, Notepad++, ou autre). Ajoutez la ligne suivante en remplaçant `your_github_token_here` par votre vrai token GitHub :

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Enregistrez le fichier** : Sauvegardez les modifications et fermez l’éditeur.

5. **Installez `python-dotenv`** : Si ce n’est pas déjà fait, installez le paquet `python-dotenv` pour charger les variables d’environnement depuis le fichier `.env` dans votre application Python. Vous pouvez l’installer avec `pip` :

   ```bash
   pip install python-dotenv
   ```

6. **Chargez les variables d’environnement dans votre script Python** : Dans votre script Python, utilisez le paquet `python-dotenv` pour charger les variables d’environnement depuis le fichier `.env` :

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Voilà ! Vous avez créé un fichier `.env`, ajouté votre token GitHub, et chargé celui-ci dans votre application Python.

## Comment exécuter localement sur votre ordinateur

Pour exécuter le code localement, vous devez avoir une version de [Python installée](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Ensuite, pour utiliser le dépôt, vous devez le cloner :

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Une fois tout récupéré, vous pouvez commencer !

## Étapes optionnelles

### Installer Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) est un installateur léger pour installer [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, ainsi que quelques paquets.  
Conda est un gestionnaire de paquets qui facilite la création et la gestion de différents [environnements virtuels](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python et leurs paquets. Il est aussi utile pour installer des paquets non disponibles via `pip`.

Vous pouvez suivre le [guide d’installation de MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pour le configurer.

Une fois Miniconda installé, vous devez cloner le [dépôt](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (si ce n’est pas déjà fait).

Ensuite, créez un environnement virtuel. Pour cela avec Conda, créez un nouveau fichier d’environnement (_environment.yml_). Si vous suivez ce cours avec Codespaces, créez-le dans le répertoire `.devcontainer`, donc `.devcontainer/environment.yml`.

Remplissez votre fichier d’environnement avec l’extrait ci-dessous :

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

Si vous rencontrez des erreurs avec conda, vous pouvez installer manuellement les bibliothèques Microsoft AI avec la commande suivante dans un terminal.

```
conda install -c microsoft azure-ai-ml
```

Le fichier d’environnement spécifie les dépendances nécessaires. `<environment-name>` correspond au nom que vous souhaitez donner à votre environnement Conda, et `<python-version>` est la version de Python désirée, par exemple `3` pour la dernière version majeure.

Une fois cela fait, créez votre environnement Conda en lançant les commandes ci-dessous dans votre terminal :

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consultez le [guide des environnements Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) en cas de problème.

### Utiliser Visual Studio Code avec l’extension Python

Nous recommandons d’utiliser l’éditeur [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) avec l’[extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) pour ce cours. C’est toutefois une recommandation, pas une obligation.

> **Note** : En ouvrant le dépôt du cours dans VS Code, vous pouvez configurer le projet dans un conteneur grâce au [répertoire spécial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) présent dans le dépôt. Nous y reviendrons plus tard.

> **Note** : Une fois le dépôt cloné et ouvert dans VS Code, il vous proposera automatiquement d’installer l’extension Python.

> **Note** : Si VS Code vous suggère de rouvrir le dépôt dans un conteneur, refusez cette demande pour utiliser la version locale de Python installée sur votre machine.

### Utiliser Jupyter dans le navigateur

Vous pouvez aussi travailler sur le projet avec l’environnement [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directement dans votre navigateur. Jupyter classique et [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrent un environnement de développement agréable avec des fonctionnalités comme l’autocomplétion, la coloration syntaxique, etc.

Pour lancer Jupyter localement, ouvrez un terminal, placez-vous dans le répertoire du cours, et exécutez :

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Cela démarrera une instance Jupyter et l’URL d’accès s’affichera dans la fenêtre du terminal.

Une fois l’URL ouverte, vous verrez le plan du cours et pourrez naviguer vers n’importe quel fichier `*.ipynb`. Par exemple, `08-building-search-applications/python/oai-solution.ipynb`.

### Exécuter dans un conteneur

Une alternative à l’installation locale ou dans Codespaces est d’utiliser un [conteneur](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Le dossier spécial `.devcontainer` dans le dépôt permet à VS Code de configurer le projet dans un conteneur. En dehors de Codespaces, cela nécessite l’installation de Docker et demande un peu de travail, donc nous recommandons cette option uniquement aux personnes expérimentées avec les conteneurs.

Une des meilleures façons de sécuriser vos clés API dans GitHub Codespaces est d’utiliser les Codespace Secrets. Veuillez suivre le guide [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) pour en savoir plus.

## Leçons et exigences techniques

Le cours comprend 6 leçons conceptuelles et 6 leçons de codage.

Pour les leçons de codage, nous utilisons le service Azure OpenAI. Vous aurez besoin d’un accès au service Azure OpenAI et d’une clé API pour exécuter ce code. Vous pouvez demander l’accès en [remplissant cette demande](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

En attendant la validation de votre demande, chaque leçon de codage inclut un fichier `README.md` où vous pouvez consulter le code et les résultats.

## Utiliser le service Azure OpenAI pour la première fois

Si c’est votre première fois avec le service Azure OpenAI, suivez ce guide pour [créer et déployer une ressource Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Utiliser l’API OpenAI pour la première fois

Si c’est votre première fois avec l’API OpenAI, suivez le guide pour [créer et utiliser l’interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Rencontrer d’autres apprenants

Nous avons créé des salons dans notre serveur officiel [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pour rencontrer d’autres apprenants. C’est un excellent moyen de réseauter avec d’autres entrepreneurs, développeurs, étudiants, et toute personne souhaitant progresser en IA générative.

[![Rejoindre le salon discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

L’équipe du projet sera également présente sur ce serveur Discord pour aider les apprenants.

## Contribuer

Ce cours est une initiative open source. Si vous voyez des points à améliorer ou des problèmes, créez une [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou signalez un [issue GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

L’équipe du projet suit toutes les contributions. Contribuer à l’open source est une excellente façon de faire avancer votre carrière en IA générative.

La plupart des contributions nécessitent que vous acceptiez un Contrat de Licence de Contributeur (CLA) déclarant que vous avez le droit et accordez effectivement à Microsoft les droits d’utiliser votre contribution. Pour plus de détails, consultez le site [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important : lors de la traduction des textes de ce dépôt, assurez-vous de ne pas utiliser de traduction automatique. Nous vérifierons les traductions via la communauté, donc ne proposez vos services que pour des langues que vous maîtrisez.

Lorsque vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez fournir un CLA et ajoutera les labels ou commentaires appropriés. Suivez simplement les instructions du bot. Vous n’aurez à le faire qu’une seule fois pour tous les dépôts utilisant notre CLA.

Ce projet a adopté le [Code de conduite open source Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pour plus d’informations, consultez la FAQ du Code de conduite ou contactez [Email opencode](opencode@microsoft.com) pour toute question ou remarque.

## Commençons

Maintenant que vous avez complété les étapes nécessaires pour suivre ce cours, commençons par une [introduction à l’IA générative et aux LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.