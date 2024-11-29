[![Open Source Models](../../../translated_images/18-lesson-banner.png?WT.73626ba24f59a39704c5137a18c9de8b23179ea0e1ace42c97e02f0310adcee0.fr.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson18-gh?WT.mc_id=academic-105485-koreyst)

# Affiner Votre Modèle de Langage

Utiliser des modèles de langage de grande taille pour construire des applications d'IA générative apporte de nouveaux défis. Un problème clé est d'assurer la qualité des réponses (précision et pertinence) dans le contenu généré par le modèle pour une requête utilisateur donnée. Dans les leçons précédentes, nous avons discuté de techniques comme l'ingénierie des invites et la génération augmentée par récupération qui tentent de résoudre le problème en _modifiant l'entrée de l'invite_ au modèle existant.

Dans la leçon d'aujourd'hui, nous discutons d'une troisième technique, **l'affinage**, qui tente de relever le défi en _réentraînant le modèle lui-même_ avec des données supplémentaires. Plongeons dans les détails.

## Objectifs d'apprentissage

Cette leçon introduit le concept d'affinage pour les modèles de langage pré-entraînés, explore les avantages et les défis de cette approche, et fournit des conseils sur quand et comment utiliser l'affinage pour améliorer la performance de vos modèles d'IA générative.

À la fin de cette leçon, vous devriez être capable de répondre aux questions suivantes :

- Qu'est-ce que l'affinage pour les modèles de langage ?
- Quand, et pourquoi, l'affinage est-il utile ?
- Comment puis-je affiner un modèle pré-entraîné ?
- Quelles sont les limitations de l'affinage ?

Prêt ? Commençons.

## Guide Illustré

Vous voulez avoir une vue d'ensemble de ce que nous allons couvrir avant de plonger ? Consultez ce guide illustré qui décrit le parcours d'apprentissage de cette leçon - depuis l'apprentissage des concepts de base et la motivation pour l'affinage, jusqu'à la compréhension du processus et des meilleures pratiques pour exécuter la tâche d'affinage. C'est un sujet fascinant à explorer, alors n'oubliez pas de consulter la page [Ressources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pour des liens supplémentaires pour soutenir votre parcours d'apprentissage autonome !

![Guide Illustré de l'Affinage des Modèles de Langage](../../../translated_images/18-fine-tuning-sketchnote.png?WT.6cca0798e805b67b1f22beaba7478f40066f3a2879380a0e27dbc70ac1dc7832.fr.mc_id=academic-105485-koreyst)

## Qu'est-ce que l'affinage pour les modèles de langage ?

Par définition, les modèles de langage de grande taille sont _pré-entraînés_ sur de grandes quantités de texte provenant de sources diverses, y compris Internet. Comme nous l'avons appris dans les leçons précédentes, nous avons besoin de techniques comme _l'ingénierie des invites_ et la _génération augmentée par récupération_ pour améliorer la qualité des réponses du modèle aux questions des utilisateurs ("invites").

Une technique populaire d'ingénierie des invites consiste à donner au modèle plus d'indications sur ce qui est attendu dans la réponse, soit en fournissant des _instructions_ (guidage explicite) soit en lui donnant quelques exemples (guidage implicite). Cela est appelé _apprentissage par peu d'exemples_, mais cela a deux limitations :

- Les limites de tokens du modèle peuvent restreindre le nombre d'exemples que vous pouvez donner, et limiter l'efficacité.
- Les coûts de tokens du modèle peuvent rendre coûteux l'ajout d'exemples à chaque invite, et limiter la flexibilité.

L'affinage est une pratique courante dans les systèmes d'apprentissage automatique où nous prenons un modèle pré-entraîné et le réentraînons avec de nouvelles données pour améliorer sa performance sur une tâche spécifique. Dans le contexte des modèles de langage, nous pouvons affiner le modèle pré-entraîné _avec un ensemble d'exemples sélectionnés pour une tâche ou un domaine d'application donné_ pour créer un **modèle personnalisé** qui peut être plus précis et pertinent pour cette tâche ou ce domaine spécifique. Un avantage secondaire de l'affinage est qu'il peut également réduire le nombre d'exemples nécessaires pour l'apprentissage par peu d'exemples - réduisant l'utilisation de tokens et les coûts associés.

## Quand et pourquoi devrions-nous affiner les modèles ?

Dans _ce_ contexte, lorsque nous parlons d'affinage, nous faisons référence à l'affinage **supervisé** où le réentraînement est effectué en **ajoutant de nouvelles données** qui ne faisaient pas partie du jeu de données d'entraînement initial. Cela diffère d'une approche d'affinage non supervisé où le modèle est réentraîné sur les données originales, mais avec des hyperparamètres différents.

La chose clé à retenir est que l'affinage est une technique avancée qui nécessite un certain niveau d'expertise pour obtenir les résultats souhaités. Si elle est mal réalisée, elle peut ne pas fournir les améliorations attendues, et peut même dégrader la performance du modèle pour votre domaine ciblé.

Donc, avant d'apprendre "comment" affiner les modèles de langage, vous devez savoir "pourquoi" vous devriez emprunter cette voie, et "quand" commencer le processus d'affinage. Commencez par vous poser ces questions :

- **Cas d'utilisation** : Quel est votre _cas d'utilisation_ pour l'affinage ? Quel aspect du modèle pré-entraîné actuel souhaitez-vous améliorer ?
- **Alternatives** : Avez-vous essayé _d'autres techniques_ pour atteindre les résultats souhaités ? Utilisez-les pour créer une référence pour la comparaison.
  - Ingénierie des invites : Essayez des techniques comme les invites avec peu d'exemples de réponses pertinentes. Évaluez la qualité des réponses.
  - Génération Augmentée par Récupération : Essayez d'augmenter les invites avec les résultats de requête récupérés en recherchant dans vos données. Évaluez la qualité des réponses.
- **Coûts** : Avez-vous identifié les coûts pour l'affinage ?
  - Possibilité d'affinage - le modèle pré-entraîné est-il disponible pour l'affinage ?
  - Effort - pour préparer les données d'entraînement, évaluer et affiner le modèle.
  - Calcul - pour exécuter les tâches d'affinage, et déployer le modèle affiné
  - Données - accès à des exemples de qualité suffisante pour un impact d'affinage
- **Avantages** : Avez-vous confirmé les avantages pour l'affinage ?
  - Qualité - le modèle affiné a-t-il surpassé la référence ?
  - Coût - réduit-il l'utilisation de tokens en simplifiant les invites ?
  - Extensibilité - pouvez-vous réutiliser le modèle de base pour de nouveaux domaines ?

En répondant à ces questions, vous devriez être en mesure de décider si l'affinage est la bonne approche pour votre cas d'utilisation. Idéalement, l'approche est valide uniquement si les avantages l'emportent sur les coûts. Une fois que vous décidez de procéder, il est temps de réfléchir à _comment_ vous pouvez affiner le modèle pré-entraîné.

Vous souhaitez obtenir plus d'informations sur le processus de prise de décision ? Regardez [Affiner ou ne pas affiner](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Comment pouvons-nous affiner un modèle pré-entraîné ?

Pour affiner un modèle pré-entraîné, vous devez avoir :

- un modèle pré-entraîné à affiner
- un jeu de données à utiliser pour l'affinage
- un environnement d'entraînement pour exécuter la tâche d'affinage
- un environnement d'hébergement pour déployer le modèle affiné

## Affinage en Action

Les ressources suivantes fournissent des tutoriels étape par étape pour vous guider à travers un exemple réel en utilisant un modèle sélectionné avec un jeu de données sélectionné. Pour suivre ces tutoriels, vous avez besoin d'un compte chez le fournisseur spécifique, ainsi que d'un accès au modèle et aux jeux de données pertinents.

| Fournisseur  | Tutoriel                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Comment affiner les modèles de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)         | Apprenez à affiner un `gpt-35-turbo` pour un domaine spécifique ("assistant de recette") en préparant les données d'entraînement, en exécutant la tâche d'affinage, et en utilisant le modèle affiné pour l'inférence.                                                                                                                                                                                                                                               |
| Azure OpenAI | [Tutoriel d'affinage GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Apprenez à affiner un modèle `gpt-35-turbo-0613` **sur Azure** en prenant des mesures pour créer et télécharger des données d'entraînement, exécuter la tâche d'affinage. Déployez et utilisez le nouveau modèle.                                                                                                                                                                                                                                                           |
| Hugging Face | [Affiner les LLMs avec Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Cet article de blog vous guide dans l'affinage d'un _LLM ouvert_ (ex : `CodeLlama 7B`) en utilisant la bibliothèque [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) avec des [jeux de données](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) ouverts sur Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Affiner les LLMs avec AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ou AutoTrain Advanced) est une bibliothèque python développée par Hugging Face qui permet l'affinage pour de nombreuses tâches différentes, y compris l'affinage de LLM. AutoTrain est une solution sans code et l'affinage peut être effectué dans votre propre cloud, sur Hugging Face Spaces ou localement. Il prend en charge une interface graphique web, une CLI et l'entraînement via des fichiers de configuration yaml.                                            |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Devoir

Sélectionnez l'un des tutoriels ci-dessus et suivez-les. _Nous pouvons reproduire une version de ces tutoriels dans des Jupyter Notebooks dans ce dépôt à titre de référence uniquement. Veuillez utiliser les sources originales directement pour obtenir les dernières versions_.

## Bon Travail ! Continuez Votre Apprentissage.

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances en IA générative !

Félicitations !! Vous avez terminé la dernière leçon de la série v2 de ce cours ! Ne cessez pas d'apprendre et de construire. **Consultez la page [RESSOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pour une liste de suggestions supplémentaires juste sur ce sujet.

Notre série de leçons v1 a également été mise à jour avec plus de devoirs et de concepts. Alors prenez une minute pour rafraîchir vos connaissances - et veuillez [partager vos questions et commentaires](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) pour nous aider à améliorer ces leçons pour la communauté.

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.