<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:49:26+00:00",
  "source_file": "AGENTS.md",
  "language_code": "fr"
}
-->
# AGENTS.md

## Aperçu du projet

Ce dépôt contient un programme complet de 21 leçons pour enseigner les fondamentaux de l'IA générative et le développement d'applications. Le cours est conçu pour les débutants et couvre tout, des concepts de base à la création d'applications prêtes pour la production.

**Technologies clés :**
- Python 3.9+ avec les bibliothèques : `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript avec Node.js et les bibliothèques : `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Service Azure OpenAI, API OpenAI et modèles GitHub
- Jupyter Notebooks pour un apprentissage interactif
- Conteneurs de développement pour un environnement de développement cohérent

**Structure du dépôt :**
- 21 répertoires de leçons numérotés (00-21) contenant des fichiers README, des exemples de code et des exercices
- Plusieurs implémentations : Python, TypeScript, et parfois des exemples en .NET
- Répertoire de traductions avec plus de 40 versions linguistiques
- Configuration centralisée via le fichier `.env` (utiliser `.env.copy` comme modèle)

## Commandes d'installation

### Configuration initiale du dépôt

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Configuration de l'environnement Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration de Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configuration du conteneur de développement (recommandé)

Le dépôt inclut une configuration `.devcontainer` pour GitHub Codespaces ou les conteneurs de développement de VS Code :

1. Ouvrez le dépôt dans GitHub Codespaces ou VS Code avec l'extension Dev Containers
2. Le conteneur de développement effectuera automatiquement :
   - L'installation des dépendances Python depuis `requirements.txt`
   - L'exécution du script post-création (`.devcontainer/post-create.sh`)
   - La configuration du noyau Jupyter

## Flux de travail de développement

### Variables d'environnement

Toutes les leçons nécessitant un accès API utilisent des variables d'environnement définies dans `.env` :

- `OPENAI_API_KEY` - Pour l'API OpenAI
- `AZURE_OPENAI_API_KEY` - Pour le service Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL de l'endpoint Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Nom du déploiement du modèle de complétion de chat
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nom du déploiement du modèle d'embeddings
- `AZURE_OPENAI_API_VERSION` - Version de l'API (par défaut : `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Pour les modèles Hugging Face
- `GITHUB_TOKEN` - Pour les modèles GitHub

### Exécution des exemples Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Exécution des exemples TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Exécution des Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Travail avec différents types de leçons

- **Leçons "Learn"** : Axées sur la documentation README.md et les concepts
- **Leçons "Build"** : Incluent des exemples de code fonctionnels en Python et TypeScript
- Chaque leçon contient un README.md avec la théorie, des explications de code et des liens vers du contenu vidéo

## Directives de style de code

### Python

- Utilisez `python-dotenv` pour la gestion des variables d'environnement
- Importez la bibliothèque `openai` pour les interactions avec l'API
- Utilisez `pylint` pour le linting (certains exemples incluent `# pylint: disable=all` pour simplifier)
- Suivez les conventions de nommage PEP 8
- Stockez les identifiants API dans le fichier `.env`, jamais dans le code

### TypeScript

- Utilisez le package `dotenv` pour les variables d'environnement
- Configuration TypeScript dans `tsconfig.json` pour chaque application
- Utilisez `@azure/openai` ou `@azure-rest/ai-inference` pour les services Azure
- Utilisez `nodemon` pour le développement avec rechargement automatique
- Compilez avant d'exécuter : `npm run build` puis `npm start`

### Conventions générales

- Gardez les exemples de code simples et éducatifs
- Incluez des commentaires expliquant les concepts clés
- Le code de chaque leçon doit être autonome et exécutable
- Utilisez un nommage cohérent : préfixe `aoai-` pour Azure OpenAI, `oai-` pour l'API OpenAI, `githubmodels-` pour les modèles GitHub

## Directives de documentation

### Style Markdown

- Toutes les URLs doivent être encapsulées dans le format `[texte](../../url)` sans espaces supplémentaires
- Les liens relatifs doivent commencer par `./` ou `../`
- Tous les liens vers des domaines Microsoft doivent inclure un ID de suivi : `?WT.mc_id=academic-105485-koreyst`
- Pas de locales spécifiques aux pays dans les URLs (évitez `/en-us/`)
- Les images doivent être stockées dans le dossier `./images` avec des noms descriptifs
- Utilisez des caractères anglais, des chiffres et des tirets dans les noms de fichiers

### Support de traduction

- Le dépôt prend en charge plus de 40 langues via des actions GitHub automatisées
- Les traductions sont stockées dans le répertoire `translations/`
- Ne soumettez pas de traductions partielles
- Les traductions automatiques ne sont pas acceptées
- Les images traduites sont stockées dans le répertoire `translated_images/`

## Tests et validation

### Vérifications avant soumission

Ce dépôt utilise GitHub Actions pour la validation. Avant de soumettre des PRs :

1. **Vérifiez les liens Markdown** :
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Tests manuels** :
   - Testez les exemples Python : activez l'environnement virtuel et exécutez les scripts
   - Testez les exemples TypeScript : `npm install`, `npm run build`, `npm start`
   - Vérifiez que les variables d'environnement sont correctement configurées
   - Assurez-vous que les clés API fonctionnent avec les exemples de code

3. **Exemples de code** :
   - Assurez-vous que tout le code s'exécute sans erreurs
   - Testez avec le service Azure OpenAI et l'API OpenAI lorsque cela est applicable
   - Vérifiez que les exemples fonctionnent avec les modèles GitHub lorsqu'ils sont pris en charge

### Pas de tests automatisés

Il s'agit d'un dépôt éducatif axé sur les tutoriels et les exemples. Il n'y a pas de tests unitaires ou de tests d'intégration à exécuter. La validation repose principalement sur :
- Des tests manuels des exemples de code
- GitHub Actions pour la validation Markdown
- La revue communautaire du contenu éducatif

## Directives pour les Pull Requests

### Avant de soumettre

1. Testez les modifications de code en Python et TypeScript lorsque cela est applicable
2. Exécutez la validation Markdown (déclenchée automatiquement sur la PR)
3. Assurez-vous que les IDs de suivi sont présents sur toutes les URLs Microsoft
4. Vérifiez que les liens relatifs sont valides
5. Vérifiez que les images sont correctement référencées

### Format du titre de la PR

- Utilisez des titres descriptifs : `[Leçon 06] Correction de la faute de frappe dans l'exemple Python` ou `Mise à jour du README pour la leçon 08`
- Référencez les numéros de problème lorsque cela est applicable : `Fixes #123`

### Description de la PR

- Expliquez ce qui a été modifié et pourquoi
- Liez les problèmes associés
- Pour les modifications de code, spécifiez quels exemples ont été testés
- Pour les PRs de traduction, incluez tous les fichiers pour une traduction complète

### Exigences de contribution

- Signez le CLA Microsoft (automatique lors de la première PR)
- Forkez le dépôt sur votre compte avant de faire des modifications
- Une PR par changement logique (ne combinez pas des corrections non liées)
- Gardez les PRs ciblées et petites lorsque cela est possible

## Flux de travail courants

### Ajout d'un nouvel exemple de code

1. Accédez au répertoire de la leçon appropriée
2. Créez un exemple dans le sous-répertoire `python/` ou `typescript/`
3. Suivez la convention de nommage : `{provider}-{example-name}.{py|ts|js}`
4. Testez avec des identifiants API réels
5. Documentez toutes les nouvelles variables d'environnement dans le README de la leçon

### Mise à jour de la documentation

1. Modifiez le README.md dans le répertoire de la leçon
2. Suivez les directives Markdown (IDs de suivi, liens relatifs)
3. Les traductions sont gérées par les actions GitHub (ne les modifiez pas manuellement)
4. Testez que tous les liens sont valides

### Travail avec les conteneurs de développement

1. Le dépôt inclut `.devcontainer/devcontainer.json`
2. Le script post-création installe automatiquement les dépendances Python
3. Les extensions pour Python et Jupyter sont préconfigurées
4. L'environnement est basé sur `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Déploiement et publication

Il s'agit d'un dépôt d'apprentissage - il n'y a pas de processus de déploiement. Le programme est consommé via :

1. **Dépôt GitHub** : Accès direct au code et à la documentation
2. **GitHub Codespaces** : Environnement de développement instantané avec configuration préconfigurée
3. **Microsoft Learn** : Le contenu peut être syndiqué sur la plateforme d'apprentissage officielle
4. **docsify** : Site de documentation construit à partir de Markdown (voir `docsifytopdf.js` et `package.json`)

### Construction du site de documentation

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Résolution des problèmes

### Problèmes courants

**Erreurs d'importation Python** :
- Assurez-vous que l'environnement virtuel est activé
- Exécutez `pip install -r requirements.txt`
- Vérifiez que la version de Python est 3.9+

**Erreurs de compilation TypeScript** :
- Exécutez `npm install` dans le répertoire de l'application spécifique
- Vérifiez que la version de Node.js est compatible
- Supprimez `node_modules` et réinstallez si nécessaire

**Erreurs d'authentification API** :
- Vérifiez que le fichier `.env` existe et contient les valeurs correctes
- Assurez-vous que les clés API sont valides et non expirées
- Vérifiez que les URLs des endpoints sont correctes pour votre région

**Variables d'environnement manquantes** :
- Copiez `.env.copy` dans `.env`
- Remplissez toutes les valeurs requises pour la leçon sur laquelle vous travaillez
- Redémarrez votre application après avoir mis à jour `.env`

## Ressources supplémentaires

- [Guide de configuration du cours](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Directives de contribution](./CONTRIBUTING.md)
- [Code de conduite](./CODE_OF_CONDUCT.md)
- [Politique de sécurité](./SECURITY.md)
- [Discord Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection d'exemples de code avancés](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notes spécifiques au projet

- Il s'agit d'un **dépôt éducatif** axé sur l'apprentissage, pas sur le code de production
- Les exemples sont intentionnellement simples et axés sur l'enseignement des concepts
- La qualité du code est équilibrée avec la clarté éducative
- Chaque leçon est autonome et peut être complétée indépendamment
- Le dépôt prend en charge plusieurs fournisseurs d'API : Azure OpenAI, OpenAI et modèles GitHub
- Le contenu est multilingue avec des workflows de traduction automatisés
- Communauté active sur Discord pour les questions et le support

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.