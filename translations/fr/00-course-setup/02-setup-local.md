# Configuration Locale 🖥️

**Utilisez ce guide si vous préférez tout exécuter sur votre propre ordinateur portable.**   
Vous avez deux options : **(A) Python natif + virtual-env** ou **(B) Conteneur de développement VS Code avec Docker**.  
Choisissez celle qui vous semble la plus simple — les deux mènent aux mêmes leçons.

## 1. Prérequis

| Outil              | Version / Notes                                                                       |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (à télécharger sur <https://python.org>)                                     |
| **Git**            | Dernière version (fourni avec Xcode / Git pour Windows / gestionnaire de paquets Linux)|
| **VS Code**        | Optionnel mais recommandé <https://code.visualstudio.com>                           |
| **Docker Desktop** | *Uniquement* pour l'option B. Installation gratuite : <https://docs.docker.com/desktop/> |

> 💡 **Astuce** – Vérifiez les outils dans un terminal :  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Option A – Python Natif (le plus rapide)

### Étape 1 Cloner ce dépôt

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Étape 2 Créez et activez un environnement virtuel

```bash
python -m venv .venv          # faire un
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ L’invite devrait maintenant commencer par (.venv) — cela signifie que vous êtes dans l’environnement.

### Étape 3 Installer les dépendances

```bash
pip install -r requirements.txt
```

Passez à la Section 3 sur les [clés API](#3-ajoutez-vos-clés-api)

## 2. Option B – Conteneur de développement VS Code (Docker)

Nous avons configuré ce dépôt et ce cours avec un [conteneur de développement](https://containers.dev?WT.mc_id=academic-105485-koreyst) qui dispose d’un runtime universel capable de supporter Python3, .NET, Node.js et Java. La configuration associée est définie dans le fichier `devcontainer.json` situé dans le dossier `.devcontainer/` à la racine de ce dépôt.

>**Pourquoi choisir ceci ?**
>Environnement identique à Codespaces ; pas de dérive des dépendances.

### Étape 0 Installer les extras

Docker Desktop – vérifiez que ```docker --version``` fonctionne.
Extension VS Code Remote – Containers (ID : ms-vscode-remote.remote-containers).

### Étape 1 Ouvrez le dépôt dans VS Code

Fichier ▸ Ouvrir un dossier… → generative-ai-for-beginners

VS Code détecte .devcontainer/ et affiche une invite.

### Étape 2 Rouvrez dans le conteneur

Cliquez sur « Rouvrir dans le conteneur ». Docker construit l’image (≈ 3 min la première fois).
Lorsque l’invite du terminal apparaît, vous êtes à l’intérieur du conteneur.

## 2. Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) est un installateur léger pour installer [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, ainsi que quelques paquets.
Conda lui-même est un gestionnaire de paquets, qui facilite la création et la gestion de différents [**environnements virtuels**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python et paquets. Il est aussi pratique pour installer des paquets non disponibles via `pip`.

### Étape 0 Installer Miniconda

Suivez le [guide d’installation de MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pour le configurer.

```bash
conda --version
```

### Étape 1 Créer un environnement virtuel

Créez un nouveau fichier d’environnement (*environment.yml*). Si vous suivez avec Codespaces, créez-le dans le répertoire `.devcontainer`, donc `.devcontainer/environment.yml`.

### Étape 2 Remplissez votre fichier d’environnement

Ajoutez le snippet suivant à votre `environment.yml`

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

### Étape 3 Créez votre environnement Conda

Exécutez les commandes ci-dessous dans votre ligne de commande/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Le chemin secondaire .devcontainer s'applique uniquement aux configurations Codespace
conda activate ai4beg
```

Consultez le [guide des environnements Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si vous rencontrez des problèmes.

## 2 Option D – Jupyter classique / Jupyter Lab (dans votre navigateur)

> **Pour qui ?**  
> Toute personne qui aime l’interface classique de Jupyter ou souhaite exécuter des notebooks sans VS Code.  

### Étape 1 Vérifiez que Jupyter est installé

Pour démarrer Jupyter localement, ouvrez le terminal/ligne de commande, naviguez jusqu’au répertoire du cours, et exécutez :

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Cela lancera une instance Jupyter et l’URL d’accès sera affichée dans la fenêtre de la ligne de commande.

Une fois que vous accédez à l’URL, vous devriez voir le plan du cours et pouvoir naviguer vers n’importe quel fichier `*.ipynb`. Par exemple, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Ajoutez Vos Clés API

Il est important de garder vos clés API sécurisées lors de la création de toute application. Nous recommandons de ne pas stocker vos clés API directement dans votre code. Les commettre dans un dépôt public pourrait entraîner des problèmes de sécurité et même des coûts indésirables s’ils sont utilisés par une personne malveillante.
Voici un guide étape par étape pour créer un fichier `.env` en Python et ajouter vos identifiants des Microsoft Foundry Models :

> **Note :** Les GitHub Models (et sa variable `GITHUB_TOKEN`) seront retirés fin juillet 2026. Ce guide utilise [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) à la place. Vous préférez travailler hors ligne ? Consultez [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Naviguez vers le Répertoire de Votre Projet** : Ouvrez votre terminal ou invite de commande et allez à la racine de votre projet où vous souhaitez créer le fichier `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Créez le fichier `.env`** : Utilisez votre éditeur de texte préféré pour créer un fichier nommé `.env`. Si vous utilisez la ligne de commande, vous pouvez utiliser `touch` (sur systèmes Unix) ou `echo` (sur Windows) :

   Sur systèmes Unix :

   ```bash
   touch .env
   ```

   Sur Windows :

   ```cmd
   echo . > .env
   ```

3. **Éditez le fichier `.env`** : Ouvrez le fichier `.env` dans un éditeur de texte (ex. : VS Code, Notepad++, ou tout autre éditeur). Ajoutez les lignes suivantes, en remplaçant les placeholders par votre véritable endpoint Microsoft Foundry et clé API :

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Enregistrez le fichier** : Sauvegardez vos modifications et fermez l’éditeur.

5. **Installez `python-dotenv`** : Si ce n’est pas déjà fait, vous devez installer le paquet `python-dotenv` pour charger les variables d’environnement depuis le fichier `.env` dans votre application Python. Vous pouvez l’installer via `pip` :

   ```bash
   pip install python-dotenv
   ```

6. **Chargez les variables d'environnement dans votre script Python** : Dans votre script Python, utilisez le paquet `python-dotenv` pour charger les variables d’environnement depuis le fichier `.env` :

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

C’est tout ! Vous avez créé avec succès un fichier `.env`, ajouté vos identifiants Microsoft Foundry Models, et chargé ces variables dans votre application Python.

🔐 Ne commettez jamais le fichier .env — il est déjà dans .gitignore.
Les instructions complètes des fournisseurs se trouvent dans [`providers.md`](03-providers.md).

## 4. Et après ?

| Je veux…           | Aller à…                                                                 |
|--------------------|-------------------------------------------------------------------------|
| Commencer la Leçon 1| [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Configurer un Fournisseur LLM | [`providers.md`](03-providers.md)                                 |
| Rencontrer d'autres apprenants | [Rejoignez notre Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Dépannage

| Symptôme                                   | Solution                                                        |
|--------------------------------------------|----------------------------------------------------------------|
| `python not found`                          | Ajoutez Python au PATH ou rouvrez le terminal après installation |
| `pip` ne peut pas construire les wheels (Windows) | `pip install --upgrade pip setuptools wheel` puis réessayez.    |
| `ModuleNotFoundError: dotenv`               | Exécutez `pip install -r requirements.txt` (l’environnement n’a pas été installé). |
| Échec de la construction Docker *Plus d’espace* | Docker Desktop ▸ *Paramètres* ▸ *Ressources* → augmentez la taille du disque. |
| VS Code continue de proposer de rouvrir   | Vous avez peut-être les deux options actives ; choisissez une (venv **ou** conteneur) |
| Erreurs OpenAI 401 / 429                    | Vérifiez la valeur de `OPENAI_API_KEY` / limites de taux de requêtes. |
| Erreurs avec Conda                          | Installez les bibliothèques Microsoft AI via `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->