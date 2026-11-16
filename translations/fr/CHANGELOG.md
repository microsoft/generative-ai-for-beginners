# Journal des modifications

Tous les changements notables apportés au programme Generative AI for Beginners sont documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Comme il s'agit d'un
programme d'apprentissage plutôt que d'un paquet logiciel versionné, les entrées sont regroupées par date.

## [2026-07-16] — Validation du contenu + Ressources d’images de la leçon 09

### Modifications

- **Leçon 10 (applications IA low-code) :** mise à jour de deux liens Dataverse `docs.microsoft.com/powerapps/...` retirés
  vers le `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` actuel
  (vérifié en direct).
- **Leçon 17 (agents IA) :** modernisation d’un exemple de modèle daté (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) et d’un nom de déploiement temporaire dans l’exemple Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Racine `README.md` :** ajout de l’ID de suivi `?WT.mc_id=academic-105485-koreyst` manquant au
  lien *Microsoft for Startups*.
- **Ressources d’images de la leçon 09** régénérées avec le modèle `gpt-image` : `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, et
  `images/startup.png` (la paire avant/après de l’exemple de retouche a été produite via un vrai
  appel `client.images.edit` avec un masque généré).

### Validé

- Audit des README des leçons 01, 03, 05, 12, 14 et 16 — tous à jour (dénomination correcte et liens Microsoft Foundry) ; aucune modification nécessaire.
  nommage et liens); aucun changement requis.
- A effectué une validation complète de markdown sur les 41 fichiers markdown du dépôt (traductions exclues) pour
  les chemins de documentation obsolètes, `/en-us/` locales Microsoft, noms de produits/modèles dépassés, identifiants de suivi manquants,
  et liens/images relatifs cassés. Seule la lacune unique de l’identifiant de suivi *Microsoft for Startups* était
  exploitable ; tous les autres drapeaux ont été confirmés comme faux positifs (liens de traduction générés automatiquement,
  espaces réservés commentés, et URL structurelles tierces `/en/`).

## [2026-07-15] — Leçon 09 (Applications d'images) Réécriture pour les modèles d'image GPT

### Changé

- **Réécriture de la leçon 09 "Création d'applications de génération d'images"** autour de l'actuel **`gpt-image`**
  famille de modèles (par défaut **`gpt-image-2`** ; `gpt-image-1.5` / `gpt-image-1-mini` également GA), remplaçant le
  contenu hérité de DALL·E 2/3. Corrections clés :
  - Les modèles `gpt-image` renvoient l'image en **base64 (`b64_json`)**, pas une URL. Mise à jour de tous les exemples pour
    utiliser `base64.b64decode(...)` au lieu de télécharger un `url` avec `requests`.
  - Passage à la version d'API d'image `2025-04-01-preview`.
  - Remplacement de la section "température" fabriquée (les modèles d'image ne prennent pas `temperature`) et du
    contenu uniquement DALL·E-2 des **variations** d'image par une section **édition d'image** (masque/repeinture).
  - Mise à jour de `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, tant
    les notebooks d'assignations (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), et le notebook .NET `.dib`.

### Supprimé

- Suppression des exemples obsolètes `python/aoai-app-variation.py` et `python/oai-app-variation.py`
  (`images.create_variation` est uniquement DALL·E-2 et non supporté par `gpt-image`).
- Suppression de 4 ressources d'image orphelines liées à la section supprimée de comparaison de température
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Suppression de la dépendance inutile `requests` des exemples Python et des exigences de la leçon.

### Validé

- Exécution de `aoai-app.py` de bout en bout sur un modèle déployé `gpt-image-1.5` confirmant que le flux de décodage/enregistrement base64
  produit un PNG. Confirmation que les notebooks contiennent du JSON valide.

## [2026-07-14] — Mise à jour du modèle par défaut + Guidance du modèle de raisonnement

### Changé

- **Modèle de chat par défaut `gpt-4o-mini` → `gpt-5-mini`** dans tous les exemples exécutables du cursus,
  la documentation, et la configuration. Ceci est motivé par le cycle de vie du modèle : sur Microsoft Foundry,
  `gpt-4o-mini` (retrait le 2026-10-01) et toute la famille `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, retrait le 2026-10-14) sont **en dépréciation**, tandis que la **famille GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) est Généralement Disponible** (retrait le 2027-02-06). Mise à jour :
  - `.env.copy`, `00-course-setup/03-providers.md` (déploiement recommandé et commandes `az cognitiveservices`
    de déploiement), et les fichiers README pour les leçons 04, 06, 07, et 15.
  - Exemples Python dans la leçon 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) et scripts de la leçon 08.
  - Exemples TypeScript / JavaScript dans les leçons 06, 07, et 11, et les notebooks .NET `.dib` pour
    les leçons 06 et 07.
  - Notebooks d'assignation dans les leçons 04, 06, 07, et 11 (cellules de code), plus `shared/python/api_utils.py`
    exemples de docstring.
- **Guide des paramètres des modèles de raisonnement (nouveau).** `gpt-5-mini` est un modèle de *raisonnement* : il ne prend **pas**
  en charge `temperature`/`top_p`, et utilise `max_completion_tokens` (achèvements de chat) /
  `max_output_tokens` (API Réponses) au lieu de `max_tokens`. En conséquence :
  - Suppression de `temperature`/`top_p`/`max_tokens` des exemples qui utilisent désormais `gpt-5-mini` par défaut
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, leçon 15 RAG README).
  - Ajout d'une **note "Les modèles de raisonnement n'utilisent pas `temperature`"** à la leçon 06, expliquant que
    les modèles de raisonnement sont pilotés par **l'ingénierie des invites + les contrôles de raisonnement** plutôt que
    par les réglages d'échantillonnage, tandis que `temperature`/`top_p` restent valides pour les modèles non-raisonnement
    (GPT-4.x, Mistral, Llama, Phi, modèles ouverts).
- **`gpt-5-mini` n'est pas utilisé pour le tutoriel de fine-tuning (leçon 18).** GPT-5 supporte uniquement
  le fine-tuning par renforcement (RFT) ; le tutoriel de fine-tuning supervisé (SFT) à la leçon 18 conserve
  `gpt-4.1-mini`, qui prend en charge le SFT/DPO.
- **Les démonstrations sur la température utilisent un modèle Llama.** Pour continuer à enseigner `temperature` (que les modèles de raisonnement
  reject), un modèle `Llama-3.3-70B-Instruct` est utilisé via le point de terminaison Foundry Models. Ajout d'une nouvelle
  variable `AZURE_INFERENCE_CHAT_MODEL` à `.env.copy` ; les cahiers de la leçon 04/06 `githubmodels` et
  l'échantillon `06` `js-githubmodels` le lisent (retombant sur `Llama-3.3-70B-Instruct`) et conservent leurs
  démos `temperature`/`top_p`/`max_tokens`.
- **Exemples JS / .NET mis à jour pour GPT-5.** Suppression de `temperature`/`top_p`/`max_tokens` de GPT-5
  exemples (`06` `recipe-app` TypeScript, `06` `.dib` .NET - ce qui permet également d'éviter `MaxOutputTokenCount`
  que la sortie du raisonnement soit tronquée). L'exemple `06` `js-githubmodels` utilise désormais Llama pour maintenir sa
  démonstration de température. L'exemple `.dib` note que `Azure.AI.Inference` + un modèle Llama est la meilleure façon de
  démontrer `Temperature` en .NET.
- Les `gpt-4o-mini` / `gpt-5-mini` à gauche restent en place où ils demeurent précis : `tiktoken` références d'encodage de tokens,
  listes de disponibilité du catalogue des modèles, et modèles de discours de la leçon 02 (`gpt-4o-transcribe`).
- Les exemples des leçons 20 (Mistral) et 21 (Meta) conservent `temperature`/`max_tokens` car ils ciblent
  des modèles Mistral/Llama, qui supportent ces paramètres.

## [2026-07-06] — Actualisation de la modernisation du contenu

Une large actualisation pour garder le programme précis pour 2026 : APIs modernes, noms actuels de produits et
noms de modèles, orientation mise à jour des fournisseurs, et nouveaux outils pour l'expérience développeur.

### Ajouté

- **Section Microsoft Agent Framework** dans la leçon `17-ai-agents` couvrant les agents de chat uniques,
  les appels d'outils / de fonctions, la configuration Azure OpenAI (Microsoft Foundry) et l'orchestration
  des workflows multi-agents (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** documenté comme fournisseur hors ligne / sur appareil (aux côtés d'Ollama) dans
  `00-course-setup/03-providers.md` et la leçon `19-slm`.
- **Workflows d'intégration continue** :
  - `.github/workflows/code-quality.yml` — Ruff + Black (appliqués sur le module maintenu `shared/`,
    conseillé sur le reste du cursus), une passe ESLint consultative, et un job pytest.
  - `.github/workflows/security.yml` — Analyse CodeQL (Python + JavaScript/TypeScript) et
    revue des dépendances sur les pull requests.
- **Suite de tests** sous `tests/` — 41 tests pytest couvrant le module utilitaire partagé.
- **Compétence de migration Azure OpenAI → Responses API** sous
  `.github/skills/azure-openai-to-responses/` utilisée pour guider la migration de l'API.

### Changé

- **Chat Completions API → Responses API** dans tous les exemples de chat Python et TypeScript
  (`client.responses.create(...)` → `response.output_text`), incluant les leçons 04, 06, 07, 11,
  15, et 18, ainsi que leurs README.
- **GitHub Models → Microsoft Foundry Models** dans tout le texte, les liens et les exemples. GitHub Models
  prend fin fin juillet 2026 ; les exemples pointent désormais vers le catalogue de modèles Microsoft Foundry et utilisent
  les variables d'environnement `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, et documentation fournisseur** mises à jour pour refléter qu'Azure OpenAI fait désormais partie
  de Microsoft Foundry, et la version API par défaut est passée à `2024-10-21`.
- **Exemples TypeScript** (leçons 06, 07, 08, 11) migrés du SDK bêta déprécié `@azure/openai`
  vers le package `openai` (les applications de chat utilisent Responses API ; l’application de recherche utilise le
  client embeddings).
- **Notebooks .NET** (`dotnet/*.dib`) standardisés sur `Azure.AI.OpenAI` **2.1.0** : les leçons 06 et 07
  utilisent l'API `ChatClient`, la leçon 08 utilise `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), et
  la leçon 09 utilise `ImageClient` (`GenerateImage`) avec `gpt-image-1`, remplaçant les anciens
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` issus de `1.0.0-beta.9`.
- **Modernisation des noms de produit** : "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (leçons 14, 16, 17) et "Bing" → **Microsoft Copilot** (leçon 12), lorsque ces noms faisaient référence aux
  produits actuels.
- **DevContainer** (`.devcontainer/`) inclut désormais les extensions Pylance, Black, Ruff, ESLint, Prettier et Copilot,
  active le formatage à la sauvegarde, et installe `ruff`, `black`, `mypy`, et `pytest` afin que les contrôles CI
  puissent être reproduits localement.
- **Génération d’images** (leçon 09) recommande `gpt-image-1` pour Azure (le catalogue Azure a supprimé
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** mis à jour pour refléter le travail accompli (migration API, CI, 
  DevContainer, tests) et les faits actuels (les traductions sont produites automatiquement par le 
  Traducteur Azure Co-op ; l'API Assistants est remplacée par l'API Responses).

### Corrigé

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` renvoie désormais une 
  chaîne vide pour une entrée composée uniquement d'espaces blancs au lieu de renvoyer une erreur "trop court" (conforme au 
  cas `None`). Trouvé et couvert par la nouvelle suite de tests.
- **Exemples d'images de la leçon 09** — correction de vrais bugs : `InvalidRequestError` → `BadRequestError`, 
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`, 
  et une variable qui masquait le module `openai`.
- **Bloc-notes RAG de la leçon 15** — réparation de la configuration du client, remplacement de `DataFrame.append` supprimé 
  par `pd.concat`, et modernisation de l'utilisation du SDK ancien.
- Noms de modèles obsolètes / retirés (`gpt-3.5-turbo`, `gpt-35-turbo`) remplacés par `gpt-4o-mini` 
  dans les exemples actifs ; les résultats historiques de fine-tuning de la leçon 18 ont été conservés et annotés 
  plutôt que réécrits.

### Obsolète / Notes

- **Exemples de modèles Microsoft Foundry** utilisant `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — les exemples `githubmodels-*` et `js-githubmodels` ainsi que les leçons 19, 20,
  et 21 — restent sur l’API d’inférence de modèle, qui ne prend **pas** en charge l’API des réponses. Ceux-ci sont
  laissés intentionnellement sur ce SDK.
- `AzureOpenAI()` est intentionnellement conservé là où il est encore approprié (embeddings et génération d’images),
  car ces workflows ne font pas partie de la migration vers l’API des réponses.
- `text-embedding-ada-002` des références sont maintenues lorsqu’un index d’embeddings pré-calculé en dépend.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->