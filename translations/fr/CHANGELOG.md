# Journal des modifications

Tous les changements notables du programme d'apprentissage Generative AI for Beginners sont documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Parce qu'il s'agit d'un
programme d'apprentissage plutôt que d'un paquet logiciel versionné, les entrées sont regroupées par date.

## [2026-07-16] — Validation du contenu + Ressources images de la leçon 09

### Modifications

- **Leçon 10 (applications IA low-code) :** mise à jour de deux liens `docs.microsoft.com/powerapps/...` Dataverse retirés
  vers le `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` actuel
  (vérifié en direct).
- **Leçon 17 (agents IA) :** modernisation d’un exemple de modèle daté (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) et d’un nom de déploiement temporaire dans l'exemple du cadre d'agents
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Racine `README.md` :** ajout de l'ID de suivi `?WT.mc_id=academic-105485-koreyst` manquant au lien
  *Microsoft for Startups*.
- **Ressources images de la leçon 09** régénérées avec le modèle `gpt-image` : `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, et
  `images/startup.png` (la paire avant/après de l'exemple d'édition a été produite via un vrai
  appel `client.images.edit` avec un masque généré).

### Validations

- Audit des README des leçons 01, 03, 05, 12, 14 et 16 — tous à jour (nomenclature et liens Microsoft Foundry corrects) ; aucune modification nécessaire.
- Exécution d’une validation complète markdown sur les 41 fichiers markdown du dépôt (traductions exclues) pour
  vérifier les chemins de documentation obsolètes, les locales Microsoft `/en-us/`, les noms de produits/modèles dépassés, les ID de suivi manquants, et les liens/images relatifs cassés. Seul le manque d’ID de suivi *Microsoft for Startups* était
  exploitable ; toutes les autres alertes ont été confirmées comme faux positifs (liens de traduction auto-générés,
  espaces réservés dans les commentaires, et URLs structurelles tierces `/en/`).



## [2026-07-15] — Réécriture de la leçon 09 (Applications d’images) pour les modèles GPT Image

### Modifications

- **Réécriture de la leçon 09 "Construire des applications de génération d'images"** autour de la famille de modèles **`gpt-image`** actuelle
  (par défaut **`gpt-image-2`** ; `gpt-image-1.5` / `gpt-image-1-mini` également GA), remplaçant les
  contenus hérités de DALL·E 2/3. Corrections clés :
  - Les modèles `gpt-image` renvoient l'image en **base64 (`b64_json`)**, pas une URL. Mise à jour de tous les exemples pour
    utiliser `base64.b64decode(...)` au lieu de télécharger un `url` avec `requests`.
  - Passage à la version `2025-04-01-preview` de l'API image.
  - Remplacement de la section "température" fabriquée (les modèles d'image ne prennent pas `temperature`) et du contenu sur les
    **variations** d'image spécifique à DALL·E-2 par une section **édition d'images** (masque / inpainting).
  - Mise à jour des `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, des deux
    notebooks d'exercices (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), et du notebook .NET `.dib`.

### Supprimé

- Suppression des exemples obsolètes `python/aoai-app-variation.py` et `python/oai-app-variation.py`
  (`images.create_variation` est uniquement pour DALL·E-2 et non pris en charge par `gpt-image`).
- Suppression de 4 actifs image orphelins liés à la section supprimée de comparaison de température
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Suppression de la dépendance inutile `requests` des exemples Python et des exigences de la leçon.

### Validé

- Exécution complète de `aoai-app.py` contre un modèle `gpt-image-1.5` déployé et confirmation que le flux de décodage/enregistrement base64
  produit un PNG. Notebooks confirmés comme étant du JSON valide.

## [2026-07-14] — Mise à jour du modèle par défaut + directives pour les modèles de raisonnement

### Changé

- **Modèle de chat par défaut `gpt-4o-mini` → `gpt-5-mini`** dans les exemples exécutables du cursus,
  la documentation et la configuration. Cela a été motivé par le cycle de vie du modèle : sur Microsoft Foundry,
  `gpt-4o-mini` (retraite le 2026-10-01) et toute la famille `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, retraite le 2026-10-14) sont **en cours de dépréciation**, tandis que la **famille GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) est généralement disponible** (retraite le 2027-02-06). Mise à jour :
  - `.env.copy`, `00-course-setup/03-providers.md` (recommandation de déploiement et commandes `az cognitiveservices`
    de déploiement), et les READMEs des leçons 04, 06, 07, et 15.
  - Exemples Python des leçons 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) et scripts de la leçon 08.
  - Exemples TypeScript / JavaScript des leçons 06, 07, et 11, et notebooks `.dib` .NET des
    leçons 06 et 07.
  - Notebooks d'exercices dans les leçons 04, 06, 07, et 11 (cellules de code), plus exemples de docstring `shared/python/api_utils.py`.

- **Orientation sur les paramètres des modèles de raisonnement (nouveau).** `gpt-5-mini` est un modèle de *raisonnement* : il ne
  prend pas en charge `temperature`/`top_p`, et utilise `max_completion_tokens` (completions de chat) /
  `max_output_tokens` (API de réponses) au lieu de `max_tokens`. En conséquence :
  - Suppression de `temperature`/`top_p`/`max_tokens` dans les exemples qui utilisent désormais par défaut `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, README RAG de la leçon 15).
  - Ajout d'une **note "Les modèles de raisonnement n'utilisent pas `temperature`"** dans la leçon 06, expliquant que
    les modèles de raisonnement sont dirigés par **l'ingénierie de prompt + contrôles de raisonnement** plutôt que par
    des réglages d'échantillonnage, alors que `temperature`/`top_p` restent valides sur les modèles non-raisonnants
    (GPT-4.x, Mistral, Llama, Phi, modèles open source).
- **`gpt-5-mini` n'est pas utilisé pour le tutoriel de fine-tuning (leçon 18).** GPT-5 supporte uniquement
  le fine-tuning par renforcement (RFT); le parcours supervisé de fine-tuning (SFT) de la leçon 18
  conserve `gpt-4.1-mini`, qui supporte SFT/DPO.
- **Les démonstrations de température utilisent un modèle Llama.** Pour continuer à enseigner `temperature` (que les modèles de raisonnement
  rejettent), un modèle `Llama-3.3-70B-Instruct` est utilisé via le point d'accès Foundry Models. Ajout d'une nouvelle
  variable `AZURE_INFERENCE_CHAT_MODEL` à `.env.copy` ; les notebooks `githubmodels` des leçons 04/06 et
  l'exemple `06` `js-githubmodels` la lisent (retombant sur `Llama-3.3-70B-Instruct`) et conservent leurs
  démos `temperature`/`top_p`/`max_tokens`.
- **Exemples JS / .NET mis à jour pour GPT-5.** Suppression de `temperature`/`top_p`/`max_tokens` dans les exemples GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - qui élève aussi `MaxOutputTokenCount`
  pour éviter que la sortie du raisonnement soit tronquée). L'exemple `06` `js-githubmodels` utilise maintenant Llama pour conserver sa
  démo de température. Les notes `.dib` indiquent qu'un modèle `Azure.AI.Inference` + Llama est la méthode pour
  démontrer `Temperature` en .NET.
- Conservation de `gpt-4o-mini` / `gpt-5-mini` là où ils restent exacts : références d'encodage de tokens `tiktoken`,
  listes de disponibilité du catalogue de modèles, et modèles de voix de la leçon 02 (`gpt-4o-transcribe`).
- Les exemples des leçons 20 (Mistral) et 21 (Meta) conservent `temperature`/`max_tokens` car ils ciblent
  des modèles Mistral/Llama, qui supportent ces paramètres.

## [2026-07-06] — Actualisation de modernisation du contenu

Une vaste actualisation pour maintenir le cursus à jour en 2026 : API modernes, noms de produits et
modèles actuels, directives fournisseurs mises à jour, et nouveaux outils d'expérience développeur.

### Ajouté

- Section **Microsoft Agent Framework** dans la leçon `17-ai-agents` couvrant les agents de chat uniques,
  outils/appel de fonction, configuration Azure OpenAI (Microsoft Foundry), et orchestration de flux de travail multi-agents
  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** documenté comme fournisseur hors ligne / sur appareil (aux côtés d'Ollama) dans
  `00-course-setup/03-providers.md` et la leçon `19-slm`.
- **Flux de travail d’intégration continue** :
  - `.github/workflows/code-quality.yml` — Ruff + Black (enforcement sur le module maintenu `shared/`,
    conseil pour le reste du cursus), passage ESLint en conseil, et job pytest.
  - `.github/workflows/security.yml` — analyse CodeQL (Python + JavaScript/TypeScript) et
    revue des dépendances sur les pull requests.
- **Suite de tests** sous `tests/` — 41 tests pytest couvrant le module utilitaire partagé.
- **Compétence migration Azure OpenAI vers Responses API** sous
  `.github/skills/azure-openai-to-responses/` utilisée pour guider la migration API.

### Changé

- **Chat Completions API → Responses API** dans tous les exemples de chat Python et TypeScript
  (`client.responses.create(...)` → `response.output_text`), incluant les leçons 04, 06, 07, 11,
  15 et 18, ainsi que leurs READMEs.
- **GitHub Models → Microsoft Foundry Models** à travers le texte, liens, et exemples. GitHub Models
  prend fin fin juillet 2026 ; les exemples pointent désormais vers le catalogue de modèles Microsoft Foundry et utilisent
  les variables d’environnement `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md` et la documentation fournisseur** mis à jour pour refléter que Azure OpenAI fait maintenant partie
  de Microsoft Foundry, et la version API par défaut passée à `2024-10-21`.
- **Exemples TypeScript** (leçons 06, 07, 08, 11) migrés hors du SDK beta déprécié `@azure/openai`
  vers le package `openai` (les applications chat utilisent Responses API ; l’application de recherche utilise le
  client d’embededdings).
- **Notebooks .NET** (`dotnet/*.dib`) standardisés sur `Azure.AI.OpenAI` **2.1.0** : les leçons 06 et 07
  utilisent l’API `ChatClient`, la leçon 08 utilise `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), et
  la leçon 09 utilise `ImageClient` (`GenerateImage`) avec `gpt-image-1`, remplaçant le ancien
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` de `1.0.0-beta.9`.
- **Modernisation des noms de produits** : "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (leçons 14, 16, 17) et "Bing" → **Microsoft Copilot** (leçon 12), quand ils désignaient les
  produits actuels.
- **DevContainer** (`.devcontainer/`) inclut désormais les extensions Pylance, Black, Ruff, ESLint, Prettier, et Copilot,
  active le format à la sauvegarde, et installe `ruff`, `black`, `mypy`, et `pytest` pour permettre la reproduction
  locale des vérifications CI.
- **Génération d’images** (leçon 09) recommande `gpt-image-1` pour Azure (le catalogue Azure a supprimé
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** mis à jour pour refléter le travail accompli (migration API, CI,
  DevContainer, tests) et les faits actuels (les traductions sont produites automatiquement par le
  traducteur Azure Co-op ; l’API Assistants est remplacée par l’API Responses).

### Corrigé

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` renvoie maintenant une
  chaîne vide pour une entrée constituée uniquement d’espaces au lieu de déclencher une erreur "trop court" (conforme au
  cas `None`). Trouvé et couvert par la nouvelle suite de tests.
- **Exemples d’images de la leçon 09** — correction de bugs réels : `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  et une variable qui masquait le module `openai`.
- **Carnet RAG de la leçon 15** — réparation de la configuration client, remplacement de `DataFrame.append` supprimé
  par `pd.concat`, et modernisation de l’utilisation de l’ancien SDK.
- Noms de modèles dépréciés / retirés (`gpt-3.5-turbo`, `gpt-35-turbo`) remplacés par `gpt-4o-mini`
  dans les exemples actifs ; les résultats historiques de fine-tuning de la leçon 18 ont été conservés et annotés
  plutôt que réécrits.

### Déprécié / Notes

- **Exemples des modèles Microsoft Foundry** utilisant le SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — les exemples `githubmodels-*` et `js-githubmodels` ainsi que les leçons 19, 20,
  et 21 — restent sur l’API Model Inference, qui ne prend **pas** en charge l’API Responses. Ceux-ci sont
  délibérément laissés sur ce SDK.
- `AzureOpenAI()` est intentionnellement conservé là où il est encore approprié (embeddings et génération d’images),
  car ces flux de travail ne font pas partie de la migration vers l’API Responses.
- Les références `text-embedding-ada-002` sont conservées là où un index d’embedding pré-calculé en dépend.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->