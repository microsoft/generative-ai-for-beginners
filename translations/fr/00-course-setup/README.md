<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T22:39:13+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "fr"
}
-->
# Commencer avec ce cours

Nous sommes très enthousiastes à l'idée que vous commenciez ce cours et découvriez ce que vous pouvez créer avec l'IA générative !

Pour garantir votre succès, cette page décrit les étapes de configuration, les exigences techniques et où obtenir de l'aide si nécessaire.

## Étapes de configuration

Pour commencer ce cours, vous devrez suivre les étapes suivantes.

### 1. Forker ce dépôt

[Forkez ce dépôt entier](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) sur votre propre compte GitHub pour pouvoir modifier le code et relever les défis. Vous pouvez également [ajouter une étoile (🌟) à ce dépôt](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pour le retrouver plus facilement ainsi que les dépôts associés.

### 2. Créer un Codespace

Pour éviter tout problème de dépendance lors de l'exécution du code, nous vous recommandons de suivre ce cours dans un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dans votre fork : **Code -> Codespaces -> Nouveau sur main**

![Boîte de dialogue montrant les boutons pour créer un Codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Ajouter un secret

1. ⚙️ Icône d'engrenage -> Palette de commandes -> Codespaces : Gérer les secrets utilisateur -> Ajouter un nouveau secret.
2. Nommez-le OPENAI_API_KEY, collez votre clé, Enregistrez.

### 3. Et ensuite ?

| Je veux…             | Aller à…                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| Commencer la leçon 1  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Travailler hors ligne | [`setup-local.md`](02-setup-local.md)                                   |
| Configurer un fournisseur LLM | [`providers.md`](03-providers.md)                                        |
| Rencontrer d'autres apprenants | [Rejoindre notre Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Résolution de problèmes

| Symptôme                                   | Solution                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Construction du conteneur bloquée > 10 min| **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Le terminal ne s'est pas attaché ; cliquez sur **+** ➜ *bash*   |
| `401 Unauthorized` de OpenAI              | Clé `OPENAI_API_KEY` incorrecte ou expirée                      |
| VS Code affiche “Montage du conteneur Dev…”| Actualisez l'onglet du navigateur—Codespaces perd parfois la connexion |
| Noyau de notebook manquant                | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Systèmes basés sur Unix :

   ```bash
   touch .env
   ```

   Windows :

   ```cmd
   echo . > .env
   ```

3. **Modifier le fichier `.env`** : Ouvrez le fichier `.env` dans un éditeur de texte (par exemple, VS Code, Notepad++, ou tout autre éditeur). Ajoutez la ligne suivante au fichier, en remplaçant `your_github_token_here` par votre véritable jeton GitHub :

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Enregistrez le fichier** : Enregistrez les modifications et fermez l'éditeur de texte.

5. **Installer `python-dotenv`** : Si ce n'est pas déjà fait, vous devrez installer le package `python-dotenv` pour charger les variables d'environnement du fichier `.env` dans votre application Python. Vous pouvez l'installer avec `pip` :

   ```bash
   pip install python-dotenv
   ```

6. **Charger les variables d'environnement dans votre script Python** : Dans votre script Python, utilisez le package `python-dotenv` pour charger les variables d'environnement du fichier `.env` :

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Et voilà ! Vous avez créé avec succès un fichier `.env`, ajouté votre jeton GitHub et l'avez chargé dans votre application Python.

## Comment exécuter localement sur votre ordinateur

Pour exécuter le code localement sur votre ordinateur, vous devez avoir une version de [Python installée](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Ensuite, pour utiliser le dépôt, vous devez le cloner :

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Une fois que tout est prêt, vous pouvez commencer !

## Étapes facultatives

### Installer Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) est un installateur léger pour installer [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, ainsi que quelques packages.
Conda est un gestionnaire de packages qui facilite la configuration et le changement entre différents [**environnements virtuels**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python et leurs packages. Il est également utile pour installer des packages qui ne sont pas disponibles via `pip`.

Vous pouvez suivre le [guide d'installation de MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pour le configurer.

Avec Miniconda installé, vous devez cloner le [dépôt](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (si ce n'est pas déjà fait).

Ensuite, vous devez créer un environnement virtuel. Pour ce faire avec Conda, créez un nouveau fichier d'environnement (_environment.yml_). Si vous suivez le cours avec Codespaces, créez ce fichier dans le répertoire `.devcontainer`, donc `.devcontainer/environment.yml`.

Ajoutez le contenu suivant à votre fichier d'environnement :

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

Si vous rencontrez des erreurs avec conda, vous pouvez installer manuellement les bibliothèques Microsoft AI en utilisant la commande suivante dans un terminal.

```
conda install -c microsoft azure-ai-ml
```

Le fichier d'environnement spécifie les dépendances nécessaires. `<environment-name>` fait référence au nom que vous souhaitez donner à votre environnement Conda, et `<python-version>` est la version de Python que vous souhaitez utiliser, par exemple, `3` est la dernière version majeure de Python.

Une fois cela fait, vous pouvez créer votre environnement Conda en exécutant les commandes ci-dessous dans votre ligne de commande/terminal :

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consultez le [guide des environnements Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si vous rencontrez des problèmes.

### Utiliser Visual Studio Code avec l'extension de support Python

Nous recommandons d'utiliser l'éditeur [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) avec l'[extension de support Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installée pour ce cours. Cependant, cela reste une recommandation et non une obligation.

> **Remarque** : En ouvrant le dépôt du cours dans VS Code, vous avez la possibilité de configurer le projet dans un conteneur. Cela est possible grâce au répertoire [spécial `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) présent dans le dépôt du cours. Plus d'informations à ce sujet plus tard.

> **Remarque** : Une fois que vous avez cloné et ouvert le répertoire dans VS Code, il vous suggérera automatiquement d'installer une extension de support Python.

> **Remarque** : Si VS Code vous suggère de rouvrir le dépôt dans un conteneur, refusez cette demande afin d'utiliser la version de Python installée localement.

### Utiliser Jupyter dans le navigateur

Vous pouvez également travailler sur le projet en utilisant l'environnement [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directement dans votre navigateur. Jupyter classique et [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrent un environnement de développement agréable avec des fonctionnalités telles que l'auto-complétion, la mise en surbrillance du code, etc.

Pour démarrer Jupyter localement, ouvrez le terminal/la ligne de commande, accédez au répertoire du cours et exécutez :

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Cela démarrera une instance Jupyter et l'URL pour y accéder sera affichée dans la fenêtre de la ligne de commande.

Une fois que vous accédez à l'URL, vous devriez voir le plan du cours et pouvoir naviguer vers n'importe quel fichier `*.ipynb`. Par exemple, `08-building-search-applications/python/oai-solution.ipynb`.

### Exécution dans un conteneur

Une alternative à la configuration de tout sur votre ordinateur ou Codespace est d'utiliser un [conteneur](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Le dossier spécial `.devcontainer` dans le dépôt du cours permet à VS Code de configurer le projet dans un conteneur. En dehors de Codespaces, cela nécessitera l'installation de Docker, et franchement, cela demande un peu de travail, donc nous recommandons cette option uniquement à ceux qui ont de l'expérience avec les conteneurs.

L'une des meilleures façons de sécuriser vos clés API lors de l'utilisation de GitHub Codespaces est d'utiliser les Secrets de Codespaces. Veuillez suivre le [guide de gestion des secrets de Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) pour en savoir plus.

## Leçons et exigences techniques

Le cours comprend 6 leçons conceptuelles et 6 leçons de codage.

Pour les leçons de codage, nous utilisons le service Azure OpenAI. Vous aurez besoin d'un accès au service Azure OpenAI et d'une clé API pour exécuter ce code. Vous pouvez demander un accès en [complétant cette application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

En attendant que votre demande soit traitée, chaque leçon de codage inclut également un fichier `README.md` où vous pouvez consulter le code et les résultats.

## Utiliser le service Azure OpenAI pour la première fois

Si c'est votre première fois avec le service Azure OpenAI, veuillez suivre ce guide pour [créer et déployer une ressource Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Utiliser l'API OpenAI pour la première fois

Si c'est votre première fois avec l'API OpenAI, veuillez suivre le guide sur [comment créer et utiliser l'interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Rencontrer d'autres apprenants

Nous avons créé des canaux sur notre serveur officiel [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pour rencontrer d'autres apprenants. C'est une excellente façon de réseauter avec d'autres entrepreneurs, créateurs, étudiants et toute personne souhaitant se perfectionner en IA générative.

[![Rejoindre le canal Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

L'équipe du projet sera également présente sur ce serveur Discord pour aider les apprenants.

## Contribuer

Ce cours est une initiative open-source. Si vous voyez des points à améliorer ou des problèmes, veuillez créer une [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou signaler un [problème sur GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

L'équipe du projet suivra toutes les contributions. Contribuer à l'open source est une excellente façon de développer votre carrière en IA générative.

La plupart des contributions nécessitent que vous acceptiez un Accord de Licence de Contributeur (CLA) déclarant que vous avez le droit et que vous accordez effectivement les droits nécessaires pour utiliser votre contribution. Pour plus de détails, visitez le site [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important : lors de la traduction du texte dans ce dépôt, veuillez vous assurer de ne pas utiliser de traduction automatique. Nous vérifierons les traductions via la communauté, donc veuillez ne vous porter volontaire que pour des traductions dans des langues que vous maîtrisez.

Lorsque vous soumettez une pull request, un bot CLA déterminera automatiquement si vous devez fournir un CLA et annotera la PR en conséquence (par exemple, étiquette, commentaire). Suivez simplement les instructions fournies par le bot. Vous n'aurez à le faire qu'une seule fois pour tous les dépôts utilisant notre CLA.

Ce projet a adopté le [Code de Conduite Open Source de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pour plus d'informations, lisez la FAQ sur le Code de Conduite ou contactez [Email opencode](opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Commençons !
Maintenant que vous avez terminé les étapes nécessaires pour suivre ce cours, commençons par une [introduction à l'IA générative et aux LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.