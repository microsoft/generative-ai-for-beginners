# AGENTS.md

## Aperçu du projet

Ce dépôt contient un cursus complet de 21 leçons enseignant les fondamentaux de l'IA générative et le développement d'applications. Le cours est conçu pour les débutants et couvre tout, des concepts de base à la création d'applications prêtes pour la production.

**Technologies clés :**
- Python 3.9+ avec les bibliothèques : `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript avec Node.js et les bibliothèques : `openai` (Azure OpenAI via le point de terminaison v1 + API Responses), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, et Microsoft Foundry Models (GitHub Models est retiré fin juillet 2026)
- Jupyter Notebooks pour un apprentissage interactif
- Dev Containers pour un environnement de développement cohérent

**Structure du dépôt :**
- 21 répertoires de leçons numérotés (00-21) contenant des README, des exemples de code et des devoirs
- Multiples implémentations : exemples en Python, TypeScript, et parfois .NET
- Répertoire de traductions avec plus de 40 versions linguistiques
- Configuration centralisée via fichier `.env` (utiliser `.env.copy` comme modèle)

## Commandes d'installation

### Initialisation du dépôt

```bash
# Cloner le dépôt
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copier le modèle d'environnement
cp .env.copy .env
# Modifier .env avec vos clés API et points de terminaison
```

### Configuration de l’environnement Python

```bash
# Créer un environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
# Sur macOS/Linux :
source venv/bin/activate
# Sur Windows :
venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### Configuration Node.js/TypeScript

```bash
# Installer les dépendances au niveau root (pour les outils de documentation)
npm install

# Pour les exemples TypeScript de chaque leçon, naviguez vers la leçon spécifique :
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configuration du Dev Container (recommandé)

Le dépôt inclut une configuration `.devcontainer` pour GitHub Codespaces ou les Dev Containers VS Code :

1. Ouvrir le dépôt dans GitHub Codespaces ou VS Code avec l’extension Dev Containers
2. Le Dev Container va automatiquement :
   - Installer les dépendances Python depuis `requirements.txt`
   - Exécuter le script post-création (`.devcontainer/post-create.sh`)
   - Configurer le kernel Jupyter

## Flux de développement

### Variables d'environnement

Toutes les leçons nécessitant un accès API utilisent des variables d'environnement définies dans `.env` :

- `OPENAI_API_KEY` - Pour l’API OpenAI
- `AZURE_OPENAI_API_KEY` - Pour Azure OpenAI dans Microsoft Foundry (Azure OpenAI Service fait maintenant partie de Microsoft Foundry : https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL du point de terminaison Azure OpenAI (point de terminaison ressource Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Nom du déploiement du modèle de complétion de chat (par défaut du cours : `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Nom du déploiement du modèle d’embeddings (par défaut du cours : `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Version de l’API (par défaut : `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Pour les modèles Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Point de terminaison des Microsoft Foundry Models (catalogue multi-fournisseurs)
- `AZURE_INFERENCE_CREDENTIAL` - Clé API Microsoft Foundry Models (remplace le `GITHUB_TOKEN` retiré)
- `AZURE_INFERENCE_CHAT_MODEL` - Modèle sans raisonnement (par ex. `Llama-3.3-70B-Instruct`) utilisé par les exemples avec la variable `temperature`, car les modèles de raisonnement ne supportent pas le contrôle d’échantillonnage

### Conventions des modèles (important)

- **Modèle de chat par défaut est `gpt-5-mini`** - un modèle de **raisonnement** actuel et non déprécié. En 2026, les anciens modèles “mini” capables de gérer la variable temperature (`gpt-4o-mini`, `gpt-4.1-mini`) sont *dépréciés*, donc le cursus se standardise sur la famille GPT-5.
- **Les modèles de raisonnement refusent `temperature` et `top_p`**, et utilisent `max_output_tokens` (API Responses) / `max_completion_tokens` (complétions chat) à la place de `max_tokens`. Ne **pas** ajouter `temperature`/`top_p`/`max_tokens` aux exemples qui appellent `gpt-5-mini`.
- **Pour démontrer `temperature`**, les exemples utilisent un modèle **Llama** (`Llama-3.3-70B-Instruct`) via le point de terminaison Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). Orientez les modèles de raisonnement via l’ingénierie des prompts et les contrôles de raisonnement plutôt que par les paramètres d’échantillonnage.
- **L’affinage (lesson 18)** conserve `gpt-4.1-mini` : GPT-5 supporte seulement le fine-tuning par renforcement (RFT) et pas le fine-tuning supervisé (SFT) montré dans cette leçon.
- Les leçons 20 (Mistral) et 21 (Meta) conservent `temperature`/`max_tokens` car elles ciblent les modèles Mistral/Llama qui les supportent.

### Exécution des exemples Python

```bash
# Naviguez vers le répertoire de la leçon
cd 06-text-generation-apps/python

# Exécutez un script Python
python aoai-app.py
```

### Exécution des exemples TypeScript

```bash
# Naviguer vers le répertoire de l'application TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Compiler le code TypeScript
npm run build

# Exécuter l'application
npm start
```

### Exécution des Jupyter Notebooks

```bash
# Démarrer Jupyter à la racine du dépôt
jupyter notebook

# Ou utiliser VS Code avec l'extension Jupyter
```

### Travail avec différents types de leçons

- **Leçons “Learn”** : Focus sur la documentation README.md et les concepts
- **Leçons “Build”** : Incluent des exemples de code fonctionnel en Python et TypeScript
- Chaque leçon possède un README.md avec théorie, parcours du code, et liens vers du contenu vidéo

## Lignes directrices pour le style de code

### Python

- Utiliser `python-dotenv` pour la gestion des variables d’environnement
- Importer la bibliothèque `openai` pour l’interaction avec l’API
- Utiliser `pylint` pour le linting (certains exemples incluent `# pylint: disable=all` pour simplifier)
- Suivre les conventions de nommage PEP 8
- Stocker les identifiants API dans un fichier `.env`, jamais dans le code

### TypeScript

- Utiliser le paquet `dotenv` pour les variables d’environnement
- Configuration TypeScript dans `tsconfig.json` pour chaque application
- Utiliser le paquet `openai` pour Azure OpenAI (pointer le client vers le point de terminaison `/openai/v1/` et appeler `client.responses.create`); utiliser `@azure-rest/ai-inference` pour Microsoft Foundry Models
- Utiliser `nodemon` pour le développement avec rechargement automatique
- Compiler avant l’exécution : `npm run build` puis `npm start`

### Conventions générales

- Garder les exemples de code simples et pédagogiques
- Inclure des commentaires expliquant les concepts clés
- Le code de chaque leçon doit être autonome et exécutable
- Utiliser une nomenclature cohérente : préfixe `aoai-` pour Azure OpenAI, `oai-` pour OpenAI API, `githubmodels-` pour Microsoft Foundry Models (préfixe hérité de l’ère GitHub Models)

## Directives de documentation

### Style Markdown

- Toutes les URLs doivent être encadrées dans le format `[texte](../../url)` sans espaces supplémentaires
- Les liens relatifs doivent commencer par `./` ou `../`
- Tous les liens vers des domaines Microsoft doivent inclure un ID de suivi : `?WT.mc_id=academic-105485-koreyst`
- Pas de locales spécifiques au pays dans les URLs (éviter `/en-us/`)
- Les images sont stockées dans le dossier `./images` avec des noms descriptifs
- Utiliser des caractères anglais, chiffres et tirets dans les noms de fichiers

### Support des traductions

- Le dépôt supporte plus de 40 langues via des GitHub Actions automatisées
- Les traductions sont stockées dans le répertoire `translations/`
- Ne pas soumettre de traductions partielles
- Les traductions automatiques ne sont pas acceptées
- Les images traduites sont stockées dans le répertoire `translated_images/`

## Tests et validation

### Vérifications pré-soumission

Ce dépôt utilise GitHub Actions pour la validation. Avant de soumettre des PR :

1. **Vérifier les liens Markdown** :
   ```bash
   # Le workflow validate-markdown.yml vérifie :
   # - Chemins relatifs cassés
   # - Identifiants de suivi manquants sur les chemins
   # - Identifiants de suivi manquants sur les URL
   # - URL avec localisateur de pays
   # - URL externes cassées
   ```

2. **Tests manuels** :
   - Tester les exemples Python : activer venv et exécuter les scripts
   - Tester les exemples TypeScript : `npm install`, `npm run build`, `npm start`
   - Vérifier que les variables d’environnement sont correctement configurées
   - Contrôler que les clés API fonctionnent avec les exemples de code

3. **Exemples de code** :
   - S’assurer que tout le code s’exécute sans erreurs
   - Tester avec Azure OpenAI et OpenAI API lorsque c’est applicable
   - Vérifier que les exemples fonctionnent avec Microsoft Foundry Models quand c’est supporté

### Pas de tests automatisés

Il s’agit d’un dépôt éducatif axé sur les tutoriels et exemples. Il n’y a pas de tests unitaires ni d’intégration à exécuter. La validation repose principalement sur :
- Tests manuels des exemples de code
- GitHub Actions pour la validation Markdown
- Revue communautaire du contenu éducatif

## Directives pour les demandes de tirage (Pull Requests)

### Avant de soumettre

1. Tester les modifications de code en Python et TypeScript lorsque possible
2. Exécuter la validation Markdown (déclenchée automatiquement sur PR)
3. S’assurer que les ID de suivi sont présents sur toutes les URLs Microsoft
4. Vérifier que les liens relatifs sont valides
5. Contrôler que les images sont correctement référencées

### Format du titre de PR

- Utiliser des titres descriptifs : `[Leçon 06] Correction d’une faute dans l’exemple Python` ou `Mise à jour du README pour la leçon 08`
- Référencer les numéros de tickets quand applicables : `Fixes #123`

### Description de PR

- Expliquer ce qui a été changé et pourquoi
- Lier les tickets liés
- Pour les changements de code, spécifier les exemples testés
- Pour les PR de traduction, inclure tous les fichiers pour une traduction complète

### Conditions de contribution

- Signer la CLA Microsoft (automatique lors de la première PR)
- Forker le dépôt sur votre compte avant de faire des modifications
- Une PR par changement logique (ne pas combiner des corrections non liées)
- Garder les PR ciblées et petites quand c’est possible

## Flux de travail courants

### Ajouter un nouvel exemple de code

1. Se rendre dans le répertoire de la leçon concernée
2. Créer l’exemple dans le sous-répertoire `python/` ou `typescript/`
3. Suivre la convention de nommage : `{provider}-{example-name}.{py|ts|js}`
4. Tester avec de véritables identifiants API
5. Documenter toutes nouvelles variables d’environnement dans le README de la leçon

### Mise à jour de la documentation

1. Modifier le README.md dans le répertoire de la leçon
2. Suivre les directives Markdown (ID de suivi, liens relatifs)
3. Les traductions sont gérées par GitHub Actions (ne pas éditer manuellement)
4. Tester que tous les liens sont valides

### Travail avec les Dev Containers

1. Le dépôt inclut `.devcontainer/devcontainer.json`
2. Le script post-création installe automatiquement les dépendances Python
3. Les extensions pour Python et Jupyter sont préconfigurées
4. L’environnement est basé sur `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Déploiement et publication

Il s’agit d’un dépôt d’apprentissage - il n’existe pas de processus de déploiement. Le cursus est consommé via :

1. **Dépôt GitHub** : accès direct au code et à la documentation
2. **GitHub Codespaces** : environnement dev instantané avec configuration préétablie
3. **Microsoft Learn** : le contenu peut être syndiqué sur la plateforme d’apprentissage officielle
4. **docsify** : site de documentation généré à partir du Markdown (voir `docsifytopdf.js` et `package.json`)

### Construction du site de documentation

```bash
# Générer un PDF à partir de la documentation (si nécessaire)
npm run convert
```

## Résolution des problèmes

### Problèmes courants

**Erreurs d’import Python** :
- Vérifier que l’environnement virtuel est activé
- Exécuter `pip install -r requirements.txt`
- S’assurer que la version Python est 3.9+

**Erreurs de compilation TypeScript** :
- Exécuter `npm install` dans le répertoire de l’application spécifique
- Vérifier que la version de Node.js est compatible
- Supprimer `node_modules` et réinstaller si nécessaire

**Erreurs d’authentification API** :
- Vérifier que le fichier `.env` existe et contient les bonnes valeurs
- Contrôler que les clés API sont valides et non expirées
- S’assurer que les URLs des endpoints sont correctes pour votre région

**Variables d’environnement manquantes** :
- Copier `.env.copy` en `.env`
- Remplir toutes les valeurs requises pour la leçon sur laquelle vous travaillez
- Redémarrer votre application après mise à jour de `.env`

## Ressources supplémentaires

- [Guide d’installation du cours](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Directives de contribution](./CONTRIBUTING.md)
- [Code de conduite](./CODE_OF_CONDUCT.md)
- [Politique de sécurité](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection d’exemples avancés de code](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Notes spécifiques au projet

- Il s’agit d’un **dépôt éducatif** centré sur l’apprentissage, pas sur un code de production
- Les exemples sont volontairement simples et focalisés pour enseigner des concepts
- La qualité du code est équilibrée avec la clarté pédagogique
- Chaque leçon est autonome et peut être complétée indépendamment
- Le dépôt supporte plusieurs fournisseurs d’API : Azure OpenAI, OpenAI, Microsoft Foundry Models, et fournisseurs hors ligne comme Foundry Local et Ollama
- Le contenu est multilingue avec des workflows de traduction automatisés
- Communauté active sur Discord pour questions et support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->