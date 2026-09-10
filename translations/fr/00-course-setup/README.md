# Premiers pas avec ce cours

Nous sommes très enthousiastes à l'idée que vous commenciez ce cours et voyiez ce que l'IA Générative vous inspirera de construire !

Pour assurer votre réussite, cette page décrit les étapes de configuration, les exigences techniques et où obtenir de l'aide si nécessaire.

## Étapes de configuration

Pour commencer ce cours, vous devez compléter les étapes suivantes.

### 1. Forkez ce Repo

[Forkez ce dépôt complet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) dans votre propre compte GitHub pour pouvoir modifier le code et réaliser les défis. Vous pouvez également [mettre une étoile (🌟) à ce dépôt](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) afin de le retrouver plus facilement ainsi que les dépôts liés.

### 2. Créez un codespace

Pour éviter tout problème de dépendances lors de l'exécution du code, nous recommandons d'exécuter ce cours dans un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dans votre fork : **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/fr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Ajoutez un secret

1. ⚙️ Icône d'engrenage -> Command Pallete-> Codespaces : Manage user secret -> Ajouter un nouveau secret.
2. Nommer OPENAI_API_KEY, coller votre clé, Enregistrer.

### 3. Et après ?

| Je veux…           | Aller à…                                                               |
|---------------------|-------------------------------------------------------------------------|
| Commencer la leçon 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Travailler hors ligne | [`setup-local.md`](02-setup-local.md)                                   |
| Configurer un fournisseur LLM | [`providers.md`](03-providers.md)                                        |
| Rencontrer d'autres apprenants | [Rejoignez notre Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Dépannage


| Symptôme                                  | Solution                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| Construction de container bloquée > 10 min | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`                | Le terminal ne s'est pas attaché ; cliquez sur **+** ➜ *bash*  |
| `401 Unauthorized` de OpenAI                | `OPENAI_API_KEY` erronée ou expirée                            |
| VS Code affiche “Dev container mounting…”  | Rafraîchissez l'onglet du navigateur—Codespaces perd parfois la connexion  |
| Noyau du notebook manquant                 | Menu notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Systèmes basés sur Unix :

   ```bash
   touch .env
   ```

   Windows :

   ```cmd
   echo . > .env
   ```

3. **Modifier le fichier `.env`** : Ouvrez le fichier `.env` dans un éditeur de texte (par ex., VS Code, Notepad++, ou tout autre éditeur). Ajoutez les lignes suivantes au fichier, en remplaçant les espaces réservés par votre point de terminaison et clé des modèles Microsoft Foundry (voir [`providers.md`](03-providers.md) pour savoir comment les obtenir) :

   > **Note :** Les modèles GitHub (et sa variable `GITHUB_TOKEN`) seront retirés fin juillet 2026. Utilisez plutôt les [modèles Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Enregistrez le fichier** : Sauvegardez les modifications et fermez l'éditeur de texte.

5. **Installez `python-dotenv`** : Si ce n'est pas encore fait, vous devez installer le paquet `python-dotenv` pour charger les variables d'environnement du fichier `.env` dans votre application Python. Vous pouvez l'installer avec `pip` :

   ```bash
   pip install python-dotenv
   ```

6. **Chargez les variables d'environnement dans votre script Python** : Dans votre script Python, utilisez le paquet `python-dotenv` pour charger les variables d'environnement du fichier `.env` :

   ```python
   from dotenv import load_dotenv
   import os

   # Charger les variables d'environnement depuis le fichier .env
   load_dotenv()

   # Accéder aux variables des modèles Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Voilà ! Vous avez créé avec succès un fichier `.env`, ajouté vos identifiants des modèles Microsoft Foundry, et les avez chargés dans votre application Python.

## Comment exécuter localement sur votre ordinateur

Pour exécuter le code localement sur votre ordinateur, vous devez avoir une version de [Python installée](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pour utiliser ensuite le dépôt, vous devez le cloner :

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Une fois tout téléchargé, vous pouvez commencer !

## Étapes optionnelles

### Installer Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) est un installateur léger pour installer [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, ainsi que quelques paquets.
Conda est un gestionnaire de paquets qui facilite la configuration et le changement entre différents [environnements virtuels](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python et paquets. Il est également très utile pour installer des paquets non disponibles via `pip`.

Vous pouvez suivre le [guide d'installation de MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pour le mettre en place.

Avec Miniconda installé, vous devez cloner le [dépôt](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (si ce n’est pas déjà fait)

Ensuite, vous devez créer un environnement virtuel. Pour cela avec Conda, créez un nouveau fichier d’environnement (_environment.yml_). Si vous utilisez Codespaces, créez-le dans le répertoire `.devcontainer`, donc `.devcontainer/environment.yml`.

Remplissez le fichier d’environnement avec l’extrait ci-dessous :

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

Si vous avez des erreurs avec conda, vous pouvez installer manuellement les bibliothèques Microsoft AI en exécutant la commande suivante dans un terminal.

```
conda install -c microsoft azure-ai-ml
```

Le fichier d’environnement précise les dépendances nécessaires. `<environment-name>` désigne le nom que vous souhaitez donner à votre environnement Conda, et `<python-version>` est la version de Python que vous souhaitez utiliser, par exemple, `3` est la dernière version majeure disponible.

Une fois cela fait, créez votre environnement Conda en exécutant les commandes suivantes dans votre terminal/ligne de commande

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Le sous-chemin .devcontainer s'applique uniquement aux configurations Codespace
conda activate ai4beg
```

Consultez le [guide des environnements Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) en cas de problème.

### Utilisation de Visual Studio Code avec l’extension de support Python

Nous recommandons d’utiliser l’éditeur [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) avec l’[extension de support Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installée pour ce cours. Il s’agit toutefois d’une recommandation et non d’une exigence absolue.

> **Note** : En ouvrant le dépôt du cours dans VS Code, vous avez la possibilité de configurer le projet au sein d’un conteneur. Ceci est rendu possible grâce au [répertoire `.devcontainer` spécial](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) présent dans le dépôt du cours. Nous y reviendrons plus tard.

> **Note** : Une fois que vous clonez et ouvrez le répertoire dans VS Code, il vous proposera automatiquement d’installer une extension de support Python.

> **Note** : Si VS Code vous suggère de rouvrir le dépôt dans un conteneur, refusez cette demande afin d’utiliser la version Python installée localement.

### Utilisation de Jupyter dans le navigateur

Vous pouvez aussi travailler sur le projet en utilisant l’environnement [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) directement dans votre navigateur. Jupyter classique et [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) offrent un environnement de développement très agréable avec des fonctions telles que l’auto-complétion, la mise en surbrillance du code, etc.

Pour démarrer Jupyter localement, ouvrez un terminal/ligne de commande, naviguez dans le dossier du cours, et exécutez :

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Cela démarrera une instance Jupyter et l’URL pour y accéder s’affichera dans la fenêtre du terminal.

Une fois que vous avez accédé à l’URL, vous devriez voir le plan du cours et pouvoir naviguer dans n’importe quel fichier `*.ipynb`. Par exemple, `08-building-search-applications/python/oai-solution.ipynb`.

### Exécution dans un conteneur

Une alternative à la configuration sur votre ordinateur ou Codespace est d’utiliser un [conteneur](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Le dossier spécial `.devcontainer` dans le dépôt du cours permet à VS Code de configurer le projet dans un conteneur. En dehors de Codespaces, cela nécessite l’installation de Docker et, franchement, cela demande un peu de travail ; nous recommandons cette option uniquement aux personnes expérimentées avec les conteneurs.

Une des meilleures façons de sécuriser vos clés API lors de l’utilisation des Codespaces GitHub est d’utiliser les Secrets Codespace. Veuillez suivre le guide de [gestion des secrets dans Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) pour en savoir plus.


## Leçons et exigences techniques

Le cours comprend des leçons "Apprendre" qui expliquent les concepts de l’IA Générative et des leçons "Construire" avec des exemples de code pratiques en **Python** et en **TypeScript** quand c’est possible.

Pour les leçons de codage, nous utilisons Azure OpenAI dans Microsoft Foundry. Vous aurez besoin d’un abonnement Azure et d’une clé API. L’accès est ouvert — pas de demande requise — vous pouvez donc [créer une ressource Microsoft Foundry et déployer un modèle](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) pour obtenir votre point de terminaison et votre clé.

Chaque leçon de codage comprend aussi un fichier `README.md` où vous pouvez voir le code et les résultats sans rien exécuter.

## Utilisation du service Azure OpenAI pour la première fois

Si c’est la première fois que vous travaillez avec le service Azure OpenAI, veuillez suivre ce guide sur [comment créer et déployer une ressource Azure OpenAI.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Utilisation de l’API OpenAI pour la première fois

Si c’est la première fois que vous travaillez avec l’API OpenAI, veuillez suivre le guide sur [comment créer et utiliser l’interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Rencontrer d’autres apprenants

Nous avons créé des canaux sur notre serveur officiel Discord de la [communauté IA](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pour rencontrer d’autres apprenants. C’est un excellent moyen de réseauter avec d’autres entrepreneurs, développeurs, étudiants et toute personne souhaitant progresser en IA Générative.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

L’équipe projet sera également présente sur ce serveur Discord pour aider les apprenants.

## Contribuer

Ce cours est une initiative open source. Si vous identifiez des améliorations ou des problèmes, veuillez créer une [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ou signaler un [problème GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

L’équipe projet suivra toutes les contributions. Contribuer à l’open source est une excellente manière de développer votre carrière en IA Générative.

La plupart des contributions nécessitent que vous acceptiez un Accord de Licence de Contributeur (CLA) déclarant que vous avez le droit et que vous accordez effectivement le droit d’utiliser votre contribution. Pour plus de détails, visitez le [site CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important : lors de la traduction des textes de ce dépôt, veuillez ne pas utiliser de traduction automatique. Nous vérifierons les traductions via la communauté, merci donc de ne proposer des traductions que dans des langues que vous maîtrisez.


Lorsque vous soumettez une pull request, un CLA-bot déterminera automatiquement si vous devez fournir une CLA et décorera la PR en conséquence (par exemple, étiquette, commentaire). Suivez simplement les instructions fournies par le bot. Vous n'aurez besoin de le faire qu'une seule fois pour tous les dépôts utilisant notre CLA.

Ce projet a adopté le [Code de conduite open source de Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pour plus d'informations, consultez la FAQ du Code de conduite ou contactez [Email opencode](opencode@microsoft.com) pour toute question ou commentaire supplémentaire.

## Commençons

Maintenant que vous avez complété les étapes nécessaires pour terminer ce cours, commençons par une [introduction à l'IA générative et aux LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->