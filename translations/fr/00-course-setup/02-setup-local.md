<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T12:34:16+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "fr"
}
-->
# Configuration locale 🖥️

**Utilisez ce guide si vous préférez tout exécuter sur votre propre ordinateur portable.**  
Vous avez deux options : **(A) Python natif + virtual-env** ou **(B) Conteneur de développement VS Code avec Docker**.  
Choisissez celle qui vous semble la plus simple—les deux mènent aux mêmes leçons.

## 1.  Prérequis

| Outil              | Version / Notes                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (téléchargez-le depuis <https://python.org>)                                  |
| **Git**            | Dernière version (fourni avec Xcode / Git pour Windows / gestionnaire de paquets Linux) |
| **VS Code**        | Optionnel mais recommandé <https://code.visualstudio.com>                            |
| **Docker Desktop** | *Uniquement* pour l’option B. Installation gratuite : <https://docs.docker.com/desktop/> |

> 💡 **Astuce** – Vérifiez les outils dans un terminal :  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Option A – Python natif (le plus rapide)

### Étape 1  Clonez ce dépôt

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Étape 2 Créez et activez un environnement virtuel

```bash
python -m venv .venv          # en faire un
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ L’invite devrait maintenant commencer par (.venv)—cela signifie que vous êtes dans l’environnement.

### Étape 3 Installez les dépendances

```bash
pip install -r requirements.txt
```

Passez à la Section 3 sur les [clés API](../../../00-course-setup)

## 2. Option B – Conteneur de développement VS Code (Docker)

Nous avons configuré ce dépôt et ce cours avec un [conteneur de développement](https://containers.dev?WT.mc_id=academic-105485-koreyst) qui dispose d’un runtime universel pouvant supporter Python3, .NET, Node.js et Java. La configuration associée est définie dans le fichier `devcontainer.json` situé dans le dossier `.devcontainer/` à la racine de ce dépôt.

>**Pourquoi choisir cela ?**  
>Environnement identique à Codespaces ; pas de dérive des dépendances.

### Étape 0 Installez les extras

Docker Desktop – vérifiez que ```docker --version``` fonctionne.  
Extension VS Code Remote – Containers (ID : ms-vscode-remote.remote-containers).

### Étape 1 Ouvrez le dépôt dans VS Code

Fichier ▸ Ouvrir un dossier… → generative-ai-for-beginners

VS Code détecte .devcontainer/ et affiche une invite.

### Étape 2 Rouvrez dans le conteneur

Cliquez sur « Reopen in Container ». Docker construit l’image (≈ 3 min la première fois).  
Quand l’invite du terminal apparaît, vous êtes dans le conteneur.

## 2.  Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) est un installateur léger pour installer [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, ainsi que quelques paquets.  
Conda est un gestionnaire de paquets qui facilite la configuration et la gestion de différents [**environnements virtuels**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python et paquets. Il est aussi utile pour installer des paquets non disponibles via `pip`.

### Étape 0  Installez Miniconda

Suivez le [guide d’installation de MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pour le configurer.

```bash
conda --version
```

### Étape 1 Créez un environnement virtuel

Créez un nouveau fichier d’environnement (*environment.yml*). Si vous suivez avec Codespaces, créez-le dans le répertoire `.devcontainer`, donc `.devcontainer/environment.yml`.

### Étape 2  Remplissez votre fichier d’environnement

Ajoutez l’extrait suivant dans votre `environment.yml`

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

Exécutez les commandes ci-dessous dans votre terminal/ligne de commande

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Le sous-chemin .devcontainer s'applique uniquement aux configurations Codespace
conda activate ai4beg
```

Consultez le [guide des environnements Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) en cas de problème.

## 2  Option D – Jupyter classique / Jupyter Lab (dans votre navigateur)

> **Pour qui ?**  
> Toute personne qui aime l’interface classique de Jupyter ou souhaite exécuter des notebooks sans VS Code.

### Étape 1  Assurez-vous que Jupyter est installé

Pour démarrer Jupyter localement, ouvrez un terminal/ligne de commande, naviguez vers le dossier du cours, et exécutez :

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Cela lancera une instance Jupyter et l’URL d’accès sera affichée dans la fenêtre de commande.

Une fois l’URL accessible, vous devriez voir le plan du cours et pouvoir naviguer vers n’importe quel fichier `*.ipynb`. Par exemple, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Ajoutez vos clés API

Il est important de garder vos clés API sûres et sécurisées lors de la création de toute application. Nous recommandons de ne pas stocker les clés API directement dans votre code. Les commettre dans un dépôt public pourrait entraîner des problèmes de sécurité et même des coûts indésirables si elles sont utilisées par un acteur malveillant.  
Voici un guide étape par étape pour créer un fichier `.env` pour Python et ajouter le `GITHUB_TOKEN` :

1. **Naviguez vers le répertoire de votre projet** : Ouvrez votre terminal ou invite de commandes et allez dans le répertoire racine de votre projet où vous souhaitez créer le fichier `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Créez le fichier `.env`** : Utilisez votre éditeur de texte préféré pour créer un nouveau fichier nommé `.env`. Si vous utilisez la ligne de commande, vous pouvez utiliser `touch` (sur systèmes Unix) ou `echo` (sur Windows) :

   Systèmes Unix :

   ```bash
   touch .env
   ```

   Windows :

   ```cmd
   echo . > .env
   ```

3. **Éditez le fichier `.env`** : Ouvrez le fichier `.env` dans un éditeur de texte (par exemple VS Code, Notepad++, ou autre). Ajoutez la ligne suivante, en remplaçant `your_github_token_here` par votre vrai token GitHub :

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

   # Charger les variables d'environnement depuis le fichier .env
   load_dotenv()

   # Accéder à la variable GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

C’est tout ! Vous avez créé un fichier `.env`, ajouté votre token GitHub, et l’avez chargé dans votre application Python.

🔐 Ne commettez jamais .env—il est déjà dans .gitignore.  
Les instructions complètes des fournisseurs sont dans [`providers.md`](03-providers.md).

## 4. Et ensuite ?

| Je veux…            | Aller à…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Commencer la leçon 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Configurer un fournisseur LLM | [`providers.md`](03-providers.md)                                       |
| Rencontrer d’autres apprenants | [Rejoignez notre Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Dépannage

| Symptôme                                  | Solution                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| `python not found`                        | Ajoutez Python au PATH ou rouvrez le terminal après l’installation |
| `pip` ne peut pas construire les wheels (Windows) | `pip install --upgrade pip setuptools wheel` puis réessayez.   |
| `ModuleNotFoundError: dotenv`             | Exécutez `pip install -r requirements.txt` (l’environnement n’était pas installé). |
| Échec de build Docker *No space left*     | Docker Desktop ▸ *Paramètres* ▸ *Ressources* → augmentez la taille du disque. |
| VS Code demande sans cesse de rouvrir     | Vous avez peut-être les deux options actives ; choisissez-en une (venv **ou** conteneur) |
| Erreurs OpenAI 401 / 429                   | Vérifiez la valeur de `OPENAI_API_KEY` / limites de taux de requêtes. |
| Erreurs avec Conda                        | Installez les bibliothèques Microsoft AI avec `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->