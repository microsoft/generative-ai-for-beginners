# Feuille de Route des Fonctionnalités Améliorées et des Améliorations

Ce document présente les améliorations recommandées pour le programme Generative AI for Beginners, basées sur une revue complète du code et une analyse des meilleures pratiques de l'industrie.

## Résumé Exécutif

Le code a été analysé pour la sécurité, la qualité du code et l'efficacité pédagogique. Ce document fournit des recommandations pour des corrections immédiates, des améliorations à court terme et des évolutions futures.

---

## 1. Améliorations de la Sécurité (Priorité : Critique)

### 1.1 Corrections Immédiates (Terminées)

| Problème | Fichiers Affectés | Statut |
|-------|----------------|--------|
| SECRET_KEY codé en dur | `05-advanced-prompts/python/aoai-solution.py` | Corrigé |
| Validation d'env manquante | Plusieurs fichiers JS/TS | Corrigé |
| Appels de fonction non sécurisés | `11-integrating-with-function-calling/js-githubmodels/app.js` | Corrigé |
| Fuites de handle de fichiers | `08-building-search-applications/scripts/` | Corrigé |
| Absence de timeout de requête | `09-building-image-applications/python/` | Corrigé |

### 1.2 Fonctionnalités de Sécurité Supplémentaires Recommandées

1. **Exemples de Limitation de Taux**
   - Ajouter du code exemple montrant comment implémenter la limitation de taux pour les appels API
   - Démontrer les schémas de backoff exponentiel

2. **Rotation des Clés API**
   - Ajouter une documentation sur les bonnes pratiques de rotation des clés API
   - Inclure des exemples d’utilisation d’Azure Key Vault ou services similaires

3. **Intégration de la Sécurité du Contenu**
   - Ajouter des exemples utilisant l’API Azure Content Safety
   - Démontrer des schémas de modération d’entrée/sortie

---

## 2. Améliorations de la Qualité du Code

### 2.1 Fichiers de Configuration Ajoutés

| Fichier | Objectif |
|------|---------|
| `.eslintrc.json` | Règles de linting JavaScript/TypeScript |
| `.prettierrc` | Standards de formatage du code |
| `pyproject.toml` | Configuration des outils Python (Black, Ruff, mypy) |

### 2.2 Utilitaires Partagés Créés

Nouveau module `shared/python/` avec :
- `env_utils.py` - Gestion des variables d’environnement
- `input_validation.py` - Validation et assainissement des entrées
- `api_utils.py` - Wrappers sécurisés pour les requêtes API

### 2.3 Améliorations de Code Recommandées

1. **Couverture des Annotations de Type**
   - Ajouter des annotations de type dans tous les fichiers Python
   - Activer le mode TypeScript strict dans tous les projets TS

2. **Standards de Documentation**
   - Ajouter des docstrings à toutes les fonctions Python
   - Ajouter des commentaires JSDoc à toutes les fonctions JavaScript/TypeScript

3. **Cadre de Tests**
   - Ajouter la configuration pytest et exemples de tests _(réalisé : config pytest dans `pyproject.toml` ; exemples de tests pour les utilitaires partagés dans [`tests/`](../../../tests) lancés en CI)_
   - Ajouter la configuration Jest pour JavaScript/TypeScript

---

## 3. Améliorations Éducatives

### 3.1 Nouveaux Sujets de Leçon

1. **Sécurité dans les Applications IA** (Leçon proposée 22)
   - Attaques et défenses par injection de prompt
   - Gestion des clés API
   - Modération de contenu
   - Limitation de taux et prévention des abus

2. **Déploiement en Production** (Leçon proposée 23)
   - Conteneurisation avec Docker
   - Pipelines CI/CD
   - Supervision et journalisation
   - Gestion des coûts

3. **Techniques RAG Avancées** (Leçon proposée 24)
   - Recherche hybride (mot-clé + sémantique)
   - Stratégies de re-ranking
   - RAG multimodal
   - Métriques d’évaluation

### 3.2 Améliorations des Leçons Existantes

| Leçon | Amélioration Recommandée |
|--------|------------------------|
| 06 - Génération de Texte | Ajouter des exemples de réponses en streaming |
| 07 - Applications de Chat | Ajouter des schémas de mémoire de conversation |
| 08 - Applications de Recherche | Ajouter une comparaison de bases de données vectorielles |
| 09 - Génération d’Images | Ajouter des exemples d’édition et de variation d’images |
| 11 - Appel de Fonction | Ajouter des appels de fonction parallèles |
| 15 - RAG | Ajouter une comparaison des stratégies de découpage |
| 17 - Agents IA | Ajouter l’orchestration multi-agent |

---

## 4. Modernisation de l’API

### 4.1 Modèles d’API Dépréciés (Migration Complétée)

Tous les exemples Python et TypeScript **chat** ont été migrés de l’API Chat Completions vers l’**API Responses** (`client.responses.create(...)` → `response.output_text`).

| Ancien Modèle | Nouveau Modèle | Statut |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (API Responses) | Terminé |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Terminé |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | package `openai` `client.responses.create()` → `response.output_text` | Terminé |
| `df.append()` (pandas) | `pd.concat()` | Terminé |

> **Note :** Les exemples Microsoft Foundry Models utilisant le SDK `azure-ai-inference` / `@azure-rest/ai-inference` (`client.complete()`) restent sur l’API Model Inference, qui ne supporte pas l’API Responses. `AzureOpenAI()` est sciemment conservé là où il est encore valide (embeddings et génération d’images).

### 4.2 Nouvelles Fonctionnalités d’API à Démontrer

1. **Sorties Structurées** (OpenAI)
   - Mode JSON
   - Appel de fonction avec schémas stricts

2. **Capacités Vision**
   - Analyse d’image avec GPT-4o (vision)
   - Prompts multimodaux

3. **Outils Intégrés de l’API Responses** (remplace l’ancienne API Assistants)
   - Interpréteur de code
   - Recherche de fichiers
   - Recherche web et outils personnalisés

---

## 5. Améliorations de l’Infrastructure

### 5.1 Améliorations CI/CD

Implémentées dans [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml) : le linting/formatage Python (Ruff + Black) est **appliqué** strictement sur le module utilitaire `shared/` maintenu et est **conseillé** pour le reste du programme, avec un passage ESLint conseillé pour JavaScript/TypeScript. La baseline illustrative était :

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Analyse de Sécurité

Implémentée dans [`.github/workflows/security.yml`](../../../.github/workflows/security.yml) : analyse CodeQL pour Python et JavaScript/TypeScript (sur push, pull request, et planification hebdomadaire) plus revue des dépendances sur pull requests. La baseline illustrative était :

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Améliorations de l’Expérience Développeur

### 6.1 Améliorations DevContainer

Implémentées dans [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) et [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh) : le conteneur embarque désormais les extensions Pylance, le formateur Black, Ruff, ESLint, Prettier, et Copilot, active le formatage à la sauvegarde lié à la config Black/Prettier du dépôt, et installe les outils développeur (`ruff`, `black`, `mypy`, `pytest`) pour pouvoir reproduire localement le [workflow de qualité de code](../../../.github/workflows/code-quality.yml). L’image de base `mcr.microsoft.com/devcontainers/universal` contient déjà Python et Node, donc aucun module supplémentaire n’est requis. La baseline illustrative était :

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Aire de Jeu Interactive

Envisager d’ajouter :
- Des notebooks Jupyter avec clés API préremplies (via environnement)
- Des démonstrations Gradio/Streamlit pour les apprenants visuels
- Des quiz interactifs pour l’évaluation des connaissances

---

## 7. Support Multilingue

### 7.1 Couverture Linguistique Actuelle

| Technologie | Leçons Couvertes | Statut |
|------------|-----------------|--------|
| Python | Toutes | Complète |
| TypeScript | 06-09, 11 | Partielle |
| JavaScript | 06-08, 11 | Partielle |
| .NET/C# | Certaines | Partielle |

### 7.2 Ajouts Recommandés

1. **Go** - Croissance rapide dans l’outillage IA/ML
2. **Rust** - Applications critiques en performance
3. **Java/Kotlin** - Applications d’entreprise

---

## 8. Optimisations de Performance

### 8.1 Optimisations au Niveau du Code

1. **Patterns Async/Await**
   - Ajouter des exemples async pour le traitement par lots
   - Démontrer les appels API concurrents

2. **Stratégies de Cache**
   - Ajouter des exemples de mise en cache des embeddings
   - Démontrer les schémas de mise en cache des réponses

3. **Optimisation des Tokens**
   - Ajouter des exemples d’utilisation de tiktoken
   - Démontrer des techniques de compression de prompt

### 8.2 Exemples d’Optimisation des Coûts

Ajouter des exemples démontrant :
- La sélection de modèle selon la complexité de la tâche
- L’ingénierie de prompt pour l’efficacité des tokens
- Le traitement par lots pour les opérations en masse

---

## 9. Accessibilité et Internationalisation

### 9.1 Statut Actuel des Traductions

Toutes les traductions sont **complètes** et générées automatiquement par le [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), qui produit et maintient à jour plus de 50 versions linguistiques du programme en synchronisation avec la source anglaise. Le contenu traduit se trouve sous `translations/` et les images localisées sous `translated_images/` ; la liste complète des langues disponibles est publiée en tête du README du dépôt.

| Aspect | Statut |
|--------|--------|
| Couverture de la traduction | Complète — 50+ langues, toutes les leçons |
| Méthode de traduction | Automatisée via [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Maintenu synchronisé avec la source anglaise | Oui — régénéré automatiquement |

### 9.2 Améliorations d’Accessibilité

1. Ajouter un texte alternatif à toutes les images
2. Assurer la mise en forme syntaxique correcte des exemples de code
3. Ajouter les transcriptions vidéo pour tout contenu vidéo
4. Garantir que le contraste des couleurs respecte les directives WCAG

---

## 10. Priorité de Mise en Œuvre

### Phase 1 : Immédiate (Semaines 1-2)
- [x] Corriger les problèmes de sécurité critiques
- [x] Ajouter la configuration de qualité du code
- [x] Créer des utilitaires partagés
- [x] Documenter les directives de sécurité

### Phase 2 : Court terme (Semaines 3-4)
- [x] Mettre à jour les modèles d’API dépréciés (Chat Completions → Responses API, Python + TypeScript)
- [ ] Ajouter des annotations de type à tous les fichiers Python (fait pour le module maintenu `shared/` ; les exemples de leçon restent simples)
- [x] Ajouter les workflows CI/CD pour la qualité du code
- [x] Créer le workflow d’analyse de sécurité

### Phase 3 : Moyen terme (Mois 2-3)
- [ ] Ajouter la nouvelle leçon sécurité
- [ ] Ajouter la leçon déploiement en production
- [x] Améliorer la configuration DevContainer
- [ ] Ajouter des démonstrations interactives

### Phase 4 : Long terme (Mois 4+)
- [ ] Ajouter la leçon RAG avancée
- [ ] Étendre la couverture linguistique
- [ ] Ajouter une suite de tests complète
- [ ] Créer un programme de certification

---

## Conclusion

Cette feuille de route propose une approche structurée pour améliorer le programme Generative AI for Beginners. En traitant les enjeux de sécurité, en modernisant les API et en enrichissant le contenu pédagogique, le cours préparera mieux les étudiants au développement d’applications IA en conditions réelles.

Pour toute question ou contribution, veuillez ouvrir un problème sur le dépôt GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->