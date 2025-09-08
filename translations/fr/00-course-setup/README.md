<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T13:25:44+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fr"
}
-->
# Commencer ce cours

Nous sommes ravis que vous commenciez ce cours et impatients de voir ce que vous allez créer avec l’IA générative !

Pour vous aider à réussir, cette page détaille les étapes d’installation, les prérequis techniques et où trouver de l’aide si besoin.

## Étapes d’installation

Pour suivre ce cours, vous devez compléter les étapes suivantes.

### 1. Forker ce dépôt

[Forkez ce dépôt complet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sur votre propre compte GitHub pour pouvoir modifier le code et relever les défis. Vous pouvez aussi [ajouter une étoile (🌟) à ce dépôt](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pour le retrouver plus facilement, ainsi que les dépôts associés.

### 2. Créer un codespace

Pour éviter les problèmes de dépendances lors de l’exécution du code, nous vous recommandons de suivre ce cours dans un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dans votre fork : **Code -> Codespaces -> New on main**

![Boîte de dialogue montrant les boutons pour créer un codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Ajouter un secret

1. Icône ⚙️ -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Nommez-le OPENAI_API_KEY, collez votre clé, puis enregistrez.

### 3.  Et ensuite ?

| Je veux…             | Aller à…                                                                 |
|----------------------|--------------------------------------------------------------------------|
| Commencer la leçon 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Travailler hors ligne| [`setup-local.md`](02-setup-local.md)                                    |
| Configurer un fournisseur LLM | [`providers.md`](providers.md)                                  |
| Rencontrer d’autres apprenants | [Rejoindre notre Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Dépannage

| Symptôme                                 | Solution                                                      |
|------------------------------------------|---------------------------------------------------------------|
| Construction du conteneur bloquée > 10 min | **Codespaces ➜ “Rebuild Container”**                         |
| `python: command not found`              | Le terminal n’est pas attaché ; cliquez sur **+** ➜ *bash*    |
| `401 Unauthorized` d’OpenAI              | Clé `OPENAI_API_KEY` incorrecte ou expirée                    |
| VS Code affiche “Dev container mounting…”| Rafraîchissez l’onglet du navigateur—Codespaces perd parfois la connexion |
| Noyau du notebook manquant               | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Systèmes Unix :

   ```bash
   touch .env
   ```

   Windows :

   ```cmd
   echo . > .env
   ```

3. **Modifier le fichier `.env`** : Ouvrez le fichier `.env` dans un éditeur de texte (par exemple VS Code, Notepad++, ou tout autre éditeur). Ajoutez la ligne suivante, en remplaçant `your_github_token_here` par votre vrai token GitHub :

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Enregistrez le fichier** : Sauvegardez les modifications et fermez l’éditeur.

5. **Installer `python-dotenv`** : Si ce n’est pas déjà fait, vous devez installer le package `python-dotenv` pour charger les variables d’environnement du fichier `.env` dans votre application Python. Installez-le avec `pip` :

   ```bash
   pip install python-dotenv
   ```

6. **Charger les variables d’environnement dans votre script Python** : Dans votre script Python, utilisez le package `python-dotenv` pour charger les variables du fichier `.env` :

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Et voilà ! Vous avez créé un fichier `.env`, ajouté votre token GitHub et l’avez chargé dans votre application Python.

## Comment exécuter localement sur votre ordinateur

Pour exécuter le code localement, vous devez avoir une version de [Python installée](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pour utiliser le dépôt, il faut le cloner :

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Une fois le dépôt récupéré, vous pouvez commencer !

## Étapes optionnelles

### Installer Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) est un installateur léger pour installer [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python et quelques packages.
Conda est un gestionnaire de paquets qui facilite la création et le changement d’[**environnements virtuels**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python et de paquets. Il est aussi utile pour installer des paquets non disponibles via `pip`.

Suivez le [guide d’installation de MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pour l’installer.

Une fois Miniconda installé, clonez le [dépôt](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (si ce n’est pas déjà fait).

Ensuite, créez un environnement virtuel. Avec Conda, créez un nouveau fichier d’environnement (_environment.yml_). Si vous suivez avec Codespaces, créez-le dans le dossier `.devcontainer`, donc `.devcontainer/environment.yml`.

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

Le fichier d’environnement précise les dépendances nécessaires. `<environment-name>` est le nom que vous souhaitez donner à votre environnement Conda, et `<python-version>` est la version de Python désirée, par exemple, `3` pour la dernière version majeure.

Une fois prêt, créez votre environnement Conda en lançant les commandes ci-dessous dans votre terminal :

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consultez le [guide des environnements Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si vous avez des soucis.

### Utiliser Visual Studio Code avec l’extension Python

Nous recommandons d’utiliser l’éditeur [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) avec l’[extension Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installée pour ce cours. Cela reste une recommandation, pas une obligation.

> **Note** : En ouvrant le dépôt du cours dans VS Code, vous pouvez configurer le projet dans un conteneur grâce au dossier [spécial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) présent dans le dépôt. Nous en reparlerons plus tard.

> **Note** : Une fois le dépôt cloné et ouvert dans VS Code, il vous proposera automatiquement d’installer l’extension Python.

> **Note** : Si VS Code vous propose de rouvrir le dépôt dans un conteneur, refusez pour utiliser la version locale de Python.

### Utiliser Jupyter dans le navigateur

Vous pouvez aussi travailler sur le projet avec l’environnement [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directement dans votre navigateur. Jupyter classique et [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrent un environnement agréable avec des fonctionnalités comme l’auto-complétion, la coloration du code, etc.

Pour démarrer Jupyter localement, ouvrez le terminal, allez dans le dossier du cours et exécutez :

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Cela lancera une instance Jupyter et l’URL pour y accéder s’affichera dans le terminal.

Une fois sur l’URL, vous verrez la structure du cours et pourrez naviguer vers n’importe quel fichier `*.ipynb`. Par exemple, `08-building-search-applications/python/oai-solution.ipynb`.

### Exécuter dans un conteneur

Une alternative à l’installation sur votre ordinateur ou Codespace est d’utiliser un [conteneur](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Le dossier spécial `.devcontainer` dans le dépôt permet à VS Code de configurer le projet dans un conteneur. En dehors de Codespaces, cela nécessite d’installer Docker et demande un peu de travail, donc nous le conseillons surtout à ceux qui ont déjà travaillé avec des conteneurs.

L’une des meilleures façons de sécuriser vos clés API dans GitHub Codespaces est d’utiliser les Secrets Codespace. Suivez le [guide de gestion des secrets Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) pour en savoir plus.

## Leçons et prérequis techniques

Le cours comprend 6 leçons de concepts et 6 leçons de code.

Pour les leçons de code, nous utilisons Azure OpenAI Service. Vous aurez besoin d’un accès à Azure OpenAI et d’une clé API pour exécuter le code. Vous pouvez demander l’accès en [remplissant cette demande](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

En attendant la validation de votre demande, chaque leçon de code inclut aussi un fichier `README.md` où vous pouvez consulter le code et les résultats.

## Utiliser Azure OpenAI Service pour la première fois

Si c’est votre première utilisation du service Azure OpenAI, suivez ce guide pour [créer et déployer une ressource Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Utiliser l’API OpenAI pour la première fois

Si vous débutez avec l’API OpenAI, suivez le guide pour [créer et utiliser l’interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Rencontrer d’autres apprenants

Nous avons créé des salons sur notre [serveur Discord officiel de la communauté IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pour rencontrer d’autres apprenants. C’est un excellent moyen de réseauter avec d’autres entrepreneurs, créateurs, étudiants et toute personne souhaitant progresser en IA générative.

[![Rejoindre le salon Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

L’équipe du projet sera aussi présente sur ce serveur Discord pour aider les apprenants.

## Contribuer

Ce cours est une initiative open source. Si vous voyez des points à améliorer ou des problèmes, créez une [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou signalez un [problème GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

L’équipe du projet suivra toutes les contributions. Contribuer à l’open source est une excellente façon de développer votre carrière en IA générative.

La plupart des contributions nécessitent d’accepter un Contributor License Agreement (CLA) qui atteste que vous avez le droit de nous accorder l’utilisation de votre contribution. Pour plus d’informations, consultez le site du [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important : lors de la traduction de textes dans ce dépôt, veillez à ne pas utiliser de traduction automatique. La communauté vérifiera les traductions, donc ne proposez de traduire que dans les langues que vous maîtrisez.

Quand vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez fournir un CLA et annotera la PR en conséquence (étiquette, commentaire). Suivez simplement les instructions du bot. Vous n’aurez à le faire qu’une seule fois pour tous les dépôts utilisant notre CLA.

Ce projet a adopté le [Code de conduite Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pour plus d’informations, lisez la FAQ du Code de conduite ou contactez [Email opencode](opencode@microsoft.com) pour toute question ou commentaire.

## C’est parti !
Maintenant que vous avez terminé les étapes nécessaires pour suivre ce cours, commençons par une [introduction à l’IA générative et aux LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.