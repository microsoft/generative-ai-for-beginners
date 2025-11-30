<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T13:24:53+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "fr"
}
-->
# Configuration locale 🖥️

**Suivez ce guide si vous préférez tout exécuter sur votre propre ordinateur portable.**  
Vous avez deux options : **(A) Python natif + virtual-env** ou **(B) Dev Container VS Code avec Docker**.  
Choisissez celle qui vous semble la plus simple—les deux mènent aux mêmes leçons.

## 1.  Prérequis

| Outil               | Version / Remarques                                                                      |
|---------------------|-----------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (téléchargez-le sur <https://python.org>)                                        |
| **Git**             | Dernière version (inclus avec Xcode / Git pour Windows / gestionnaire de paquets Linux) |
| **VS Code**         | Optionnel mais recommandé <https://code.visualstudio.com>                               |
| **Docker Desktop**  | *Uniquement* pour l’option B. Installation gratuite : <https://docs.docker.com/desktop/>|

> 💡 **Astuce** – Vérifiez les outils dans un terminal :  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Option A – Python natif (la plus rapide)

### Étape 1  Clonez ce dépôt

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Étape 2 Créez et activez un environnement virtuel

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ L’invite devrait maintenant commencer par (.venv)—cela signifie que vous êtes dans l’environnement.

### Étape 3 Installez les dépendances

```bash
pip install -r requirements.txt
```

Passez à la section 3 sur [les clés API](../../../00-course-setup)

## 2. Option B – Dev Container VS Code (Docker)

Nous avons configuré ce dépôt et ce cours avec un [container de développement](https://containers.dev?WT.mc_id=academic-105485-koreyst) qui propose un environnement universel compatible avec Python3, .NET, Node.js et Java. La configuration associée se trouve dans le fichier `devcontainer.json` situé dans le dossier `.devcontainer/` à la racine du dépôt.

>**Pourquoi choisir cette option ?**
>Environnement identique à Codespaces ; pas de divergence de dépendances.

### Étape 0 Installez les extras

Docker Desktop – vérifiez que ```docker --version``` fonctionne.
Extension VS Code Remote – Containers (ID : ms-vscode-remote.remote-containers).

### Étape 1 Ouvrez le dépôt dans VS Code

Fichier ▸ Ouvrir le dossier…  → generative-ai-for-beginners

VS Code détecte .devcontainer/ et affiche une invite.

### Étape 2 Rouvrez dans le container

Cliquez sur “Reopen in Container”. Docker construit l’image (≈ 3 min la première fois).
Quand l’invite du terminal apparaît, vous êtes dans le container.

## 2.  Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) est un installateur léger pour installer [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, ainsi que quelques paquets.
Conda est un gestionnaire de paquets qui facilite la création et le changement d’[**environnements virtuels**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python et de paquets. Il est aussi utile pour installer des paquets non disponibles via `pip`.

### Étape 0  Installez Miniconda

Suivez le [guide d’installation de MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pour l’installer.

```bash
conda --version
```

### Étape 1 Créez un environnement virtuel

Créez un nouveau fichier d’environnement (*environment.yml*). Si vous suivez le cours avec Codespaces, créez-le dans le dossier `.devcontainer`, donc `.devcontainer/environment.yml`.

### Étape 2  Remplissez votre fichier d’environnement

Ajoutez l’extrait suivant à votre fichier `environment.yml`

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

Exécutez les commandes ci-dessous dans votre terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consultez le [guide des environnements Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) si vous rencontrez des problèmes.

## 2  Option D – Jupyter classique / Jupyter Lab (dans votre navigateur)

> **Pour qui ?**  
> Ceux qui préfèrent l’interface Jupyter classique ou veulent exécuter des notebooks sans VS Code.  

### Étape 1  Vérifiez que Jupyter est installé

Pour démarrer Jupyter localement, ouvrez le terminal, allez dans le dossier du cours et exécutez :

```bash
jupyter notebook
```

ou

```bash
jupyterhub
```

Cela lancera une instance Jupyter et l’URL d’accès s’affichera dans la fenêtre du terminal.

Une fois sur l’URL, vous verrez le plan du cours et pourrez naviguer vers n’importe quel fichier `*.ipynb`. Par exemple, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Ajoutez vos clés API

Protéger vos clés API est essentiel lors du développement d’applications. Il est recommandé de ne jamais stocker vos clés API directement dans le code. Les inclure dans un dépôt public peut entraîner des problèmes de sécurité et même des coûts imprévus si elles sont utilisées par une personne malveillante.
Voici comment créer un fichier `.env` pour Python et y ajouter le `GITHUB_TOKEN` :

1. **Allez dans le dossier de votre projet** : Ouvrez le terminal et placez-vous à la racine du projet où vous souhaitez créer le fichier `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Créez le fichier `.env`** : Utilisez votre éditeur préféré pour créer un fichier nommé `.env`. En ligne de commande, utilisez `touch` (Unix) ou `echo` (Windows) :

   Systèmes Unix :

   ```bash
   touch .env
   ```

   Windows :

   ```cmd
   echo . > .env
   ```

3. **Modifiez le fichier `.env`** : Ouvrez le fichier `.env` dans un éditeur (VS Code, Notepad++, etc.). Ajoutez la ligne suivante, en remplaçant `your_github_token_here` par votre vrai token GitHub :

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Enregistrez le fichier** : Sauvegardez et fermez l’éditeur.

5. **Installez `python-dotenv`** : Si ce n’est pas déjà fait, installez le paquet `python-dotenv` pour charger les variables d’environnement du fichier `.env` dans votre application Python. Installez-le avec `pip` :

   ```bash
   pip install python-dotenv
   ```

6. **Chargez les variables d’environnement dans votre script Python** : Dans votre script, utilisez le paquet `python-dotenv` pour charger les variables du fichier `.env` :

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Voilà ! Vous avez créé un fichier `.env`, ajouté votre token GitHub et l’avez chargé dans votre application Python.

🔐 Ne jamais committer .env—il est déjà dans .gitignore.
Les instructions complètes pour les fournisseurs sont dans [`providers.md`](03-providers.md).

## 4. Et maintenant ?

| Je veux…            | Aller à…                                                                  |
|---------------------|---------------------------------------------------------------------------|
| Commencer la leçon 1| [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| Configurer un fournisseur LLM | [`providers.md`](03-providers.md)                                |
| Rencontrer d’autres apprenants | [Rejoindre notre Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Dépannage

| Symptôme                                   | Solution                                                        |
|--------------------------------------------|-----------------------------------------------------------------|
| `python not found`                         | Ajoutez Python au PATH ou rouvrez le terminal après installation|
| `pip` ne peut pas construire de wheels (Windows) | `pip install --upgrade pip setuptools wheel` puis réessayez.    |
| `ModuleNotFoundError: dotenv`              | Exécutez `pip install -r requirements.txt` (l’environnement n’a pas été installé).|
| Échec de build Docker *No space left*      | Docker Desktop ▸ *Paramètres* ▸ *Ressources* → augmentez la taille du disque.|
| VS Code demande sans cesse de rouvrir      | Vous avez peut-être les deux options actives ; choisissez-en une (venv **ou** container)|
| Erreurs OpenAI 401 / 429                   | Vérifiez la valeur de `OPENAI_API_KEY` / les limites de requêtes.|
| Erreurs avec Conda                         | Installez les librairies Microsoft AI avec `conda install -c microsoft azure-ai-ml`|

---

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.