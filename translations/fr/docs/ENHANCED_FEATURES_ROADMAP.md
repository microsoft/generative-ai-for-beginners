# Feuille de route des fonctionnalités améliorées et des améliorations

Ce document décrit les améliorations recommandées pour le programme Générative AI pour débutants, basées sur une revue complète du code et une analyse des meilleures pratiques de l'industrie.

## Résumé exécutif

La base de code a été analysée en termes de sécurité, qualité du code et efficacité pédagogique. Ce document fournit des recommandations pour des corrections immédiates, des améliorations à court terme et des améliorations futures.

---

## 1. Améliorations de la sécurité (Priorité : Critique)

### 1.1 Corrections immédiates (Terminé)

| Problème | Fichiers concernés | Statut |
|----------|--------------------|--------|
| SECRET_KEY codée en dur | `05-advanced-prompts/python/aoai-solution.py` | Corrigé |
| Validation d'environnement manquante | Plusieurs fichiers JS/TS | Corrigé |
| Appels de fonctions non sécurisés | `11-integrating-with-function-calling/js-githubmodels/app.js` | Corrigé |
| Fuites de gestionnaires de fichiers | `08-building-search-applications/scripts/` | Corrigé |
| Absence de timeouts sur les requêtes | `09-building-image-applications/python/` | Corrigé |

### 1.2 Fonctionnalités de sécurité supplémentaires recommandées

1. **Exemples de limitation de débit**
   - Ajouter un exemple de code montrant comment implémenter une limitation de débit pour les appels API
   - Démontrer des modèles de temporisation exponentielle

2. **Rotation des clés API**
   - Ajouter une documentation sur les meilleures pratiques pour la rotation des clés API
   - Inclure des exemples d'utilisation de Azure Key Vault ou services similaires

3. **Intégration de la sécurité des contenus**
   - Ajouter des exemples utilisant l’API Azure Content Safety
   - Démontrer les modèles de modération d’entrée/sortie

---

## 2. Améliorations de la qualité du code

### 2.1 Fichiers de configuration ajoutés

| Fichier | Objet |
|---------|-------|
| `.eslintrc.json` | Règles de linting JavaScript/TypeScript |
| `.prettierrc` | Normes de formatage du code |
| `pyproject.toml` | Configuration des outils Python (Black, Ruff, mypy) |

### 2.2 Utilitaires partagés créés

Nouveau module `shared/python/` avec :
- `env_utils.py` - Gestion des variables d’environnement
- `input_validation.py` - Validation et assainissement des entrées
- `api_utils.py` - Enveloppes sécurisées pour les requêtes API

### 2.3 Améliorations recommandées du code

1. **Couverture des annotations de type**
   - Ajouter des annotations de type dans tous les fichiers Python
   - Activer le mode strict TypeScript dans tous les projets TS

2. **Normes de documentation**
   - Ajouter des docstrings à toutes les fonctions Python
   - Ajouter des commentaires JSDoc à toutes les fonctions JavaScript/TypeScript

3. **Cadre de tests**
   - Ajouter une configuration pytest et des tests exemples
   - Ajouter une configuration Jest pour JavaScript/TypeScript

---

## 3. Améliorations pédagogiques

### 3.1 Nouveaux sujets de leçons

1. **Sécurité dans les applications IA** (Leçon proposée 22)
   - Attaques et défenses contre l’injection de prompt
   - Gestion des clés API
   - Modération de contenu
   - Limitation de débit et prévention des abus

2. **Déploiement en production** (Leçon proposée 23)
   - Containerisation avec Docker
   - Pipelines CI/CD
   - Monitoring et journalisation
   - Gestion des coûts

3. **Techniques RAG avancées** (Leçon proposée 24)
   - Recherche hybride (mots-clés + sémantique)
   - Stratégies de re-rank
   - RAG multimodal
   - Métriques d’évaluation

### 3.2 Améliorations des leçons existantes

| Leçon | Amélioration recommandée |
|-------|--------------------------|
| 06 - Génération de texte | Ajouter des exemples de réponse en streaming |
| 07 - Applications chat | Ajouter des modèles de mémoire de conversation |
| 08 - Applications de recherche | Ajouter une comparaison des bases vectorielles |
| 09 - Génération d’images | Ajouter des exemples d’édition/variations d’image |
| 11 - Appel de fonctions | Ajouter l’appel parallèle de fonctions |
| 15 - RAG | Ajouter une comparaison des stratégies de découpage |
| 17 - Agents IA | Ajouter l’orchestration multi-agents |

---

## 4. Modernisation de l’API

### 4.1 Modèles d’API dépréciés à mettre à jour

| Ancien modèle | Nouveau modèle | Fichiers concernés |
|---------------|---------------|--------------------|
| `openai.api_type = "azure"` | client `AzureOpenAI()` | Plusieurs scripts dans `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Plusieurs notebooks |
| `df.append()` (pandas) | `pd.concat()` | Notebook RAG |

### 4.2 Nouvelles fonctionnalités API à démontrer

1. **Sorties structurées** (OpenAI)
   - Mode JSON
   - Appels de fonctions avec schémas stricts

2. **Capacités Vision**
   - Analyse d’images avec GPT-4V
   - Prompts multimodaux

3. **API Assistants**
   - Interpréteur de code
   - Recherche de fichiers
   - Outils personnalisés

---

## 5. Améliorations de l’infrastructure

### 5.1 Améliorations CI/CD

Les workflows actuels gèrent la validation markdown. Ajouts recommandés :

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

### 5.2 Analyse de sécurité

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

## 6. Améliorations de l’expérience développeur

### 6.1 Améliorations DevContainer

Mettre à jour `.devcontainer/devcontainer.json` :

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

### 6.2 Playground interactif

Envisager d’ajouter :
- Des notebooks Jupyter avec clés API préremplies (via environnement)
- Des démos Gradio/Streamlit pour les apprenants visuels
- Des quiz interactifs pour l’évaluation des connaissances

---

## 7. Support multilingue

### 7.1 Couverture actuelle des langues

| Technologie | Leçons couvertes | Statut |
|-------------|------------------|--------|
| Python | Toutes | Complète |
| TypeScript | 06-09, 11 | Partielle |
| JavaScript | 06-08, 11 | Partielle |
| .NET/C# | Certaines | Partielle |

### 7.2 Ajouts recommandés

1. **Go** - Croissance dans les outils IA/ML
2. **Rust** - Applications à haute performance
3. **Java/Kotlin** - Applications d’entreprise

---

## 8. Optimisations de performance

### 8.1 Optimisations au niveau du code

1. **Modèles Async/Await**
   - Ajouter des exemples async pour le traitement par lots
   - Démontrer les appels API concurrents

2. **Stratégies de mise en cache**
   - Ajouter des exemples de mise en cache des embeddings
   - Démontrer les modèles de mise en cache des réponses

3. **Optimisation des tokens**
   - Ajouter des exemples d’utilisation de tiktoken
   - Démontrer les techniques de compression de prompt

### 8.2 Exemples d’optimisation des coûts

Ajouter des exemples démontrant :
- La sélection de modèle basée sur la complexité de la tâche
- L’ingénierie de prompt pour l’efficacité en tokens
- Le traitement par lots pour les opérations en masse

---

## 9. Accessibilité et internationalisation

### 9.1 Statut actuel des traductions

| Langue | Statut |
|--------|--------|
| Anglais | Complète |
| Chinois (Simplifié) | Complète |
| Japonais | Complète |
| Coréen | Complète |
| Espagnol | Partielle |
| Portugais | Partielle |
| Turc | Partielle |
| Polonais | Partielle |

### 9.2 Améliorations de l’accessibilité

1. Ajouter du texte alternatif à toutes les images
2. Assurer une coloration syntaxique correcte des exemples de code
3. Ajouter des transcriptions vidéo pour tout le contenu vidéo
4. Garantir que le contraste des couleurs respecte les directives WCAG

---

## 10. Priorité de mise en œuvre

### Phase 1 : Immédiate (Semaines 1-2)
- [x] Corriger les problèmes critiques de sécurité
- [x] Ajouter la configuration qualité de code
- [x] Créer les utilitaires partagés
- [x] Documenter les lignes directrices de sécurité

### Phase 2 : Court terme (Semaines 3-4)
- [ ] Mettre à jour les modèles API dépréciés
- [ ] Ajouter des annotations de type à tous les fichiers Python
- [ ] Ajouter des workflows CI/CD pour la qualité du code
- [ ] Créer un workflow d’analyse de sécurité

### Phase 3 : Moyen terme (Mois 2-3)
- [ ] Ajouter une nouvelle leçon sur la sécurité
- [ ] Ajouter une leçon sur le déploiement en production
- [ ] Améliorer la configuration DevContainer
- [ ] Ajouter des démos interactives

### Phase 4 : Long terme (Mois 4+)
- [ ] Ajouter une leçon avancée RAG
- [ ] Étendre la couverture linguistique
- [ ] Ajouter une suite de tests complète
- [ ] Créer un programme de certification

---

## Conclusion

Cette feuille de route propose une approche structurée pour améliorer le programme Générative AI pour débutants. En abordant les problèmes de sécurité, en modernisant les API et en ajoutant du contenu pédagogique, le cours préparera mieux les étudiants au développement d’applications IA réelles.

Pour toute question ou contribution, veuillez ouvrir une issue sur le dépôt GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour toute information critique, nous recommandons une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->