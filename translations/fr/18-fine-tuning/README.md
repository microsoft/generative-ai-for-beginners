[![Modèles Open Source](../../../translated_images/fr/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Affiner votre LLM

Utiliser de grands modèles de langage pour construire des applications d'IA générative apporte de nouveaux défis. Un enjeu clé est de garantir la qualité des réponses (exactitude et pertinence) dans le contenu généré par le modèle pour une demande utilisateur donnée. Dans les leçons précédentes, nous avons discuté des techniques comme l'ingénierie des prompts et la génération augmentée par récupération qui tentent de résoudre le problème en _modifiant l'entrée du prompt_ au modèle existant.

Dans la leçon d'aujourd'hui, nous abordons une troisième technique, **l'affinage**, qui cherche à relever le défi en _réentraînant le modèle lui-même_ avec des données supplémentaires. Entrons dans les détails.

## Objectifs d'apprentissage

Cette leçon introduit le concept d'affinage pour les modèles de langage pré-entraînés, explore les avantages et défis de cette approche, et fournit des conseils sur quand et comment utiliser l'affinage pour améliorer la performance de vos modèles d'IA générative.

À la fin de cette leçon, vous devriez être capable de répondre aux questions suivantes :

- Qu'est-ce que l'affinage pour les modèles de langage ?
- Quand et pourquoi l'affinage est-il utile ?
- Comment puis-je affiner un modèle pré-entraîné ?
- Quelles sont les limites de l'affinage ?

Prêt ? Commençons.

## Guide illustré

Vous souhaitez avoir une vue d'ensemble de ce que nous allons couvrir avant de plonger ? Consultez ce guide illustré qui décrit le parcours d'apprentissage pour cette leçon - depuis l'apprentissage des concepts clés et de la motivation pour l'affinage, jusqu'à la compréhension du processus et des meilleures pratiques pour réaliser la tâche d'affinage. C'est un sujet fascinant à explorer, alors n'oubliez pas de consulter la page [Ressources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pour des liens supplémentaires qui soutiennent votre parcours d'apprentissage autodirigé !

![Guide illustré de l'affinage des modèles de langage](../../../translated_images/fr/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Qu'est-ce que l'affinage pour les modèles de langage ?

Par définition, les grands modèles de langage sont _pré-entraînés_ sur de grandes quantités de texte provenant de sources diverses incluant Internet. Comme nous l'avons appris dans les leçons précédentes, nous avons besoin de techniques telles que _l’ingénierie des prompts_ et la _génération augmentée par récupération_ pour améliorer la qualité des réponses du modèle aux questions de l'utilisateur (« prompts »).

Une technique populaire d'ingénierie de prompt consiste à donner au modèle plus de directives sur ce qui est attendu dans la réponse soit en fournissant des _instructions_ (guidance explicite) soit en _donnant quelques exemples_ (guidance implicite). Cela s'appelle l’_apprentissage par très peu d'exemples_ mais cela a deux limitations :

- Les limites de tokens du modèle peuvent restreindre le nombre d'exemples que vous pouvez donner, et limiter l'efficacité.
- Les coûts de tokens du modèle peuvent rendre coûteux l’ajout d’exemples à chaque prompt, et limiter la flexibilité.

L'affinage est une pratique courante dans les systèmes d'apprentissage automatique où l'on prend un modèle pré-entraîné et on le réentraîne avec de nouvelles données pour améliorer ses performances sur une tâche spécifique. Dans le contexte des modèles de langage, on peut affiner le modèle pré-entraîné _avec un ensemble sélectionné d'exemples pour une tâche ou un domaine d'application donné_ pour créer un **modèle personnalisé** qui peut être plus précis et pertinent pour cette tâche ou ce domaine spécifique. Un bénéfice secondaire de l'affinage est qu'il peut également réduire le nombre d'exemples nécessaires pour l'apprentissage par très peu d'exemples - réduisant ainsi l'utilisation des tokens et les coûts associés.

## Quand et pourquoi devons-nous affiner les modèles ?

Dans _ce_ contexte, lorsque nous parlons d'affinage, nous faisons référence à l'affinage **supervisé** où le réentraînement se fait en **ajoutant de nouvelles données** qui ne faisaient pas partie du jeu de données de formation original. Cela diffère de l'approche d'affinage non supervisé où le modèle est réentraîné sur les données originales, mais avec des hyperparamètres différents.

La chose importante à retenir est que l'affinage est une technique avancée qui nécessite un certain niveau d'expertise pour obtenir les résultats souhaités. Si elle est mal réalisée, elle peut ne pas apporter les améliorations attendues, voire dégrader les performances du modèle pour votre domaine ciblé.

Donc, avant d'apprendre « comment » affiner les modèles de langage, vous devez savoir « pourquoi » vous devriez choisir cette voie, et « quand » commencer le processus d'affinage. Commencez par vous poser ces questions :

- **Cas d’usage** : Quel est votre _cas d’usage_ pour l'affinage ? Quel aspect du modèle pré-entraîné actuel voulez-vous améliorer ?
- **Alternatives** : Avez-vous essayé _d'autres techniques_ pour atteindre les résultats souhaités ? Utilisez-les pour créer une base de comparaison.
  - Ingénierie des prompts : Essayez des techniques comme le prompt avec peu d'exemples pertinents. Évaluez la qualité des réponses.
  - Génération augmentée par récupération : Essayez d'augmenter les prompts avec des résultats de requêtes récupérées dans vos données. Évaluez la qualité des réponses.
- **Coûts** : Avez-vous identifié les coûts de l'affinage ?
  - Possibilité d’affinage - le modèle pré-entraîné est-il disponible pour l'affinage ?
  - Effort - pour préparer les données d'entraînement, évaluer et affiner le modèle.
  - Calcul - pour exécuter les tâches d'affinage et déployer le modèle affiné.
  - Données - accès à suffisamment d'exemples de qualité pour un impact d'affinage.
- **Avantages** : Avez-vous confirmé les avantages de l'affinage ?
  - Qualité - le modèle affiné a-t-il dépassé la référence ?
  - Coût - cela réduit-il l'utilisation des tokens en simplifiant les prompts ?
  - Extensibilité - pouvez-vous réutiliser le modèle de base pour de nouveaux domaines ?

En répondant à ces questions, vous devriez pouvoir décider si l’affinage est la bonne approche pour votre cas d’usage. Idéalement, cette approche est valable seulement si les avantages l’emportent sur les coûts. Une fois que vous décidez de continuer, il est temps de réfléchir à _comment_ affiner le modèle pré-entraîné.

Vous voulez plus d'informations sur le processus de prise de décision ? Regardez [Affiner ou ne pas affiner](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Comment pouvons-nous affiner un modèle pré-entraîné ?

Pour affiner un modèle pré-entraîné, vous devez disposer de :

- un modèle pré-entraîné à affiner
- un jeu de données à utiliser pour l'affinage
- un environnement d’entraînement pour exécuter la tâche d'affinage
- un environnement d’hébergement pour déployer le modèle affiné

## Affinage sur Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) est l’endroit où vous affinez, déployez et gérez les modèles personnalisés sur Azure aujourd’hui (il regroupe ce qui était auparavant Azure OpenAI Studio et Azure AI Studio). Avant de commencer un travail, il est utile de comprendre les options que Foundry vous offre - ainsi que les meilleures pratiques recommandées par la plateforme. En coulisses, Foundry utilise **LoRA (adaptation à faible rang)** pour affiner les modèles efficacement, ce qui garde la formation plus rapide et plus abordable que de réentraîner chaque poids.

### Étape 1 : Choisissez une technique de formation

Foundry supporte trois techniques d’affinage. **Commencez par SFT** - c’est celle qui couvre la plus grande diversité de scénarios.

| Technique | Ce qu'elle fait | Quand l'utiliser |
| --- | --- | --- |
| **Affinage supervisé (SFT)** | Entraîne sur des paires exemple entrée/sortie afin que le modèle apprenne à produire les réponses souhaitées. | Par défaut pour la plupart des tâches : spécialisation de domaine, performance de tâche, style et ton, suivi des instructions, et adaptation linguistique. |
| **Optimisation directe de préférence (DPO)** | Apprend à partir de paires réponses _préférées vs non-préférées_ pour aligner les sorties avec les préférences humaines. | Pour améliorer la qualité, la sécurité et l'alignement des réponses quand vous disposez de retours comparatifs. |
| **Affinage par renforcement (RFT)** | Utilise des signaux de récompense provenant de _correcteurs_ pour optimiser des comportements complexes avec apprentissage par renforcement. | Domaines objectifs et nécessitant du raisonnement (maths, chimie, physique) avec réponses claires correctes/incorrectes. Nécessite plus d'expertise ML. |

### Étape 2 : Choisissez un niveau d’entraînement

Foundry vous permet de choisir comment et où s'exécute l’entraînement :

- **Standard** - s'entraîne dans la région de votre ressource et garantit la résidence des données. Utilisez-le lorsque les données doivent rester dans une région spécifique.
- **Global** - moins cher et plus rapide à mettre en file d’attente en utilisant de la capacité au-delà de votre région (les données et poids sont copiés dans la région d’entraînement). Un bon choix par défaut lorsque la résidence des données n’est pas une contrainte.
- **Développeur** - coût le plus bas, utilisant une capacité inoccupée sans garantie de latence/SLA (les emplois peuvent être interrompus puis repris). Idéal pour l’expérimentation.

### Étape 3 : Choisissez un modèle de base

Les modèles pouvant être affinés incluent OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini`, et `gpt-4.1-nano` (SFT; la famille 4o/4.1 supporte aussi DPO), les modèles de raisonnement `o4-mini` et `gpt-5` (RFT), plus les modèles open-source comme `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct`, et `gpt-oss-20b` (SFT sur ressources Foundry). Vérifiez toujours la liste actuelle des [Modèles d’affinage](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) pour les méthodes, régions et disponibilités supportées.

> Foundry propose deux modalités : **serverless** (tarification à la consommation, pas de quota GPU à gérer, OpenAI et modèles sélectionnés) et **calcul géré** (apportez vos propres machines virtuelles via Azure Machine Learning pour la plus large gamme de modèles). La plupart des utilisateurs devraient commencer par le serverless.

### Meilleures pratiques Foundry

- **Commencez par la référence.** Mesurez le modèle de base avec ingénierie des prompts et RAG _avant_ d’affiner, pour prouver le gain.
- **Démarrez petit, puis scalez.** Commencez avec 50-100 exemples de haute qualité pour valider l’approche, puis augmentez à 500+ pour la production. La qualité prime sur la quantité - élaguez les exemples de mauvaise qualité.
- **Formatez correctement les données.** Les fichiers d'entraînement et de validation doivent être JSONL, UTF-8 **avec BOM**, moins de 512 Mo, utilisant le format message chat-completions. Toujours inclure un fichier de validation pour surveiller le sur-apprentissage.
- **Conservez le prompt système d’entraînement à l'inférence.** Utilisez le même message système lors de l'appel du modèle que celui utilisé pendant l'entraînement.
- **Évaluez les checkpoints - ne déployez pas aveuglément le dernier.** Foundry conserve les trois dernières époques comme checkpoints déployables ; choisissez celui qui généralise le mieux en observant `train_loss` / `valid_loss` et la précision des tokens.
- **Mesurez le coût en tokens en parallèle à la qualité** lors de la comparaison du modèle affiné à la référence.
- **Itérez avec un affinage continu.** Vous pouvez affiner un modèle déjà affiné sur de nouvelles données (supporté pour les modèles OpenAI).
- **Prenez en compte les coûts d’hébergement.** Un modèle personnalisé déployé est facturé à l'heure, et un déploiement inactif est supprimé après 15 jours - nettoyez ce dont vous n’avez pas besoin.

Suivez le tutoriel complet dans [Personnaliser un modèle avec l'affinage](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), et consultez les guides pour [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) et [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) lorsque vous serez prêt pour les autres techniques.

## Affinage en pratique

Les ressources suivantes fournissent des tutoriels pas à pas qui vous guident à travers un exemple réel sur un modèle actuellement supporté avec un jeu de données sélectionné. Pour les suivre, vous avez besoin d'un compte chez le fournisseur spécifique, ainsi que l’accès au modèle et aux jeux de données pertinents.

| Fournisseur | Tutoriel                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Comment affiner des modèles de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)           | Apprenez à affiner un modèle de chat OpenAI récent pour un domaine spécifique (« assistant recettes ») en préparant les données d’entraînement, en lançant la tâche d’affinage, puis en utilisant le modèle affiné pour l'inférence.                                                                                                                                                                                                 |
| Microsoft Foundry | [Personnaliser un modèle avec l'affinage](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Apprenez à affiner un modèle actuellement supporté tel que `gpt-4.1-mini` **sur Azure** avec Microsoft Foundry : préparez et téléchargez les données d’entraînement et de validation, exécutez la tâche d’affinage, puis déployez et utilisez le nouveau modèle.                                                                                                                                                                        |

| Hugging Face | [Affiner les LLMs avec Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Ce billet de blog vous guide pour affiner un _LLM ouvert_ (ex : `CodeLlama 7B`) en utilisant la bibliothèque [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) avec des [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) ouverts sur Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Affiner les LLMs avec AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ou AutoTrain Advanced) est une bibliothèque Python développée par Hugging Face qui permet l’affinement pour de nombreuses tâches différentes, y compris l’affinement des LLMs. AutoTrain est une solution sans code et l’affinement peut être réalisé dans votre propre cloud, sur Hugging Face Spaces ou localement. Il supporte à la fois une interface GUI web, CLI et l'entraînement via des fichiers de configuration yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Affiner les LLMs avec Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth est un cadre open-source qui supporte l’affinement des LLMs et l’apprentissage par renforcement (RL). Unsloth simplifie l’entraînement local, l’évaluation et le déploiement avec des [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) prêts à l’emploi. Il supporte également la synthèse vocale (TTS), les modèles BERT et multimodaux. Pour commencer, lisez leur guide étape par étape [Affiner les LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Exercice

Sélectionnez un des tutoriels ci-dessus et suivez-le. _Nous pourrions reproduire une version de ces tutoriels dans des Jupyter Notebooks dans ce dépôt à titre de référence uniquement. Veuillez utiliser les sources originales directement pour obtenir les dernières versions_.

## Bon travail ! Continuez votre apprentissage.

Après avoir terminé cette leçon, consultez notre [collection d’apprentissage sur l’IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à améliorer vos connaissances en IA générative !

Félicitations !! Vous avez terminé la leçon finale de la série v2 de ce cours ! Ne cessez pas d’apprendre et de construire. **Consultez la page [RESSOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pour une liste de suggestions supplémentaires sur ce sujet uniquement.

Notre série v1 de leçons a également été mise à jour avec plus d’exercices et de concepts. Prenez donc une minute pour rafraîchir vos connaissances – et veuillez [partager vos questions et retours](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) pour nous aider à améliorer ces leçons pour la communauté.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->