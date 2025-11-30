<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T22:42:05+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "fr"
}
-->
[![Modèles Open Source](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.fr.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Affiner votre LLM

Utiliser des modèles de langage étendus pour créer des applications d'IA générative présente de nouveaux défis. Un problème clé est de garantir la qualité des réponses (précision et pertinence) dans le contenu généré par le modèle pour une demande utilisateur donnée. Dans les leçons précédentes, nous avons discuté de techniques telles que l'ingénierie des invites et la génération augmentée par la récupération, qui tentent de résoudre le problème en _modifiant l'entrée de l'invite_ du modèle existant.

Dans la leçon d'aujourd'hui, nous abordons une troisième technique, **l'affinage**, qui tente de relever le défi en _réentraînant le modèle lui-même_ avec des données supplémentaires. Plongeons dans les détails.

## Objectifs d'apprentissage

Cette leçon introduit le concept d'affinage pour les modèles de langage pré-entraînés, explore les avantages et les défis de cette approche, et fournit des conseils sur quand et comment utiliser l'affinage pour améliorer les performances de vos modèles d'IA générative.

À la fin de cette leçon, vous devriez être en mesure de répondre aux questions suivantes :

- Qu'est-ce que l'affinage des modèles de langage ?
- Quand, et pourquoi, l'affinage est-il utile ?
- Comment puis-je affiner un modèle pré-entraîné ?
- Quelles sont les limites de l'affinage ?

Prêt ? C'est parti.

## Guide illustré

Vous voulez avoir une vue d'ensemble de ce que nous allons couvrir avant de plonger dans les détails ? Consultez ce guide illustré qui décrit le parcours d'apprentissage de cette leçon - depuis l'apprentissage des concepts de base et la motivation pour l'affinage, jusqu'à la compréhension du processus et des meilleures pratiques pour exécuter la tâche d'affinage. C'est un sujet fascinant à explorer, alors n'oubliez pas de consulter la page [Ressources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) pour des liens supplémentaires qui soutiendront votre parcours d'apprentissage autonome !

![Guide illustré pour l'affinage des modèles de langage](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.fr.png)

## Qu'est-ce que l'affinage des modèles de langage ?

Par définition, les modèles de langage étendus sont _pré-entraînés_ sur de grandes quantités de texte provenant de diverses sources, y compris Internet. Comme nous l'avons appris dans les leçons précédentes, nous avons besoin de techniques comme _l'ingénierie des invites_ et _la génération augmentée par la récupération_ pour améliorer la qualité des réponses du modèle aux questions des utilisateurs ("invites").

Une technique populaire d'ingénierie des invites consiste à donner au modèle plus de directives sur ce qui est attendu dans la réponse, soit en fournissant des _instructions_ (guidage explicite), soit en _donnant quelques exemples_ (guidage implicite). Cela est appelé _apprentissage par quelques exemples_, mais cela présente deux limites :

- Les limites de tokens du modèle peuvent restreindre le nombre d'exemples que vous pouvez fournir et limiter l'efficacité.
- Les coûts des tokens du modèle peuvent rendre coûteux l'ajout d'exemples à chaque invite et limiter la flexibilité.

L'affinage est une pratique courante dans les systèmes d'apprentissage automatique où nous prenons un modèle pré-entraîné et le réentraînons avec de nouvelles données pour améliorer ses performances sur une tâche spécifique. Dans le contexte des modèles de langage, nous pouvons affiner le modèle pré-entraîné _avec un ensemble d'exemples soigneusement sélectionnés pour une tâche ou un domaine d'application donné_ afin de créer un **modèle personnalisé** qui peut être plus précis et pertinent pour cette tâche ou ce domaine spécifique. Un avantage secondaire de l'affinage est qu'il peut également réduire le nombre d'exemples nécessaires pour l'apprentissage par quelques exemples - réduisant ainsi l'utilisation des tokens et les coûts associés.

## Quand et pourquoi devrions-nous affiner les modèles ?

Dans _ce_ contexte, lorsque nous parlons d'affinage, nous faisons référence à l'affinage **supervisé**, où le réentraînement est effectué en **ajoutant de nouvelles données** qui ne faisaient pas partie du jeu de données d'entraînement original. Cela diffère d'une approche d'affinage non supervisé où le modèle est réentraîné sur les données originales, mais avec des hyperparamètres différents.

La chose clé à retenir est que l'affinage est une technique avancée qui nécessite un certain niveau d'expertise pour obtenir les résultats souhaités. Si elle est mal réalisée, elle peut ne pas fournir les améliorations attendues et peut même dégrader les performances du modèle pour votre domaine ciblé.

Donc, avant d'apprendre "comment" affiner les modèles de langage, vous devez savoir "pourquoi" vous devriez emprunter cette voie et "quand" commencer le processus d'affinage. Commencez par vous poser ces questions :

- **Cas d'utilisation** : Quel est votre _cas d'utilisation_ pour l'affinage ? Quel aspect du modèle pré-entraîné actuel souhaitez-vous améliorer ?
- **Alternatives** : Avez-vous essayé _d'autres techniques_ pour atteindre les résultats souhaités ? Utilisez-les pour créer une base de comparaison.
  - Ingénierie des invites : Essayez des techniques comme les invites par quelques exemples avec des exemples de réponses pertinentes. Évaluez la qualité des réponses.
  - Génération augmentée par la récupération : Essayez d'augmenter les invites avec des résultats de requête récupérés en recherchant vos données. Évaluez la qualité des réponses.
- **Coûts** : Avez-vous identifié les coûts de l'affinage ?
  - Adaptabilité - le modèle pré-entraîné est-il disponible pour l'affinage ?
  - Effort - pour préparer les données d'entraînement, évaluer et affiner le modèle.
  - Calcul - pour exécuter les tâches d'affinage et déployer le modèle affiné.
  - Données - accès à des exemples de qualité suffisante pour un impact d'affinage.
- **Avantages** : Avez-vous confirmé les avantages de l'affinage ?
  - Qualité - le modèle affiné a-t-il surpassé la base de comparaison ?
  - Coût - réduit-il l'utilisation des tokens en simplifiant les invites ?
  - Extensibilité - pouvez-vous réutiliser le modèle de base pour de nouveaux domaines ?

En répondant à ces questions, vous devriez être en mesure de décider si l'affinage est la bonne approche pour votre cas d'utilisation. Idéalement, l'approche est valide uniquement si les avantages dépassent les coûts. Une fois que vous décidez de procéder, il est temps de réfléchir à _comment_ vous pouvez affiner le modèle pré-entraîné.

Vous voulez en savoir plus sur le processus de prise de décision ? Regardez [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Comment pouvons-nous affiner un modèle pré-entraîné ?

Pour affiner un modèle pré-entraîné, vous devez disposer de :

- un modèle pré-entraîné à affiner
- un jeu de données à utiliser pour l'affinage
- un environnement d'entraînement pour exécuter la tâche d'affinage
- un environnement d'hébergement pour déployer le modèle affiné

## Affinage en action

Les ressources suivantes fournissent des tutoriels étape par étape pour vous guider à travers un exemple réel en utilisant un modèle sélectionné avec un jeu de données soigneusement préparé. Pour suivre ces tutoriels, vous avez besoin d'un compte chez le fournisseur spécifique, ainsi que d'un accès au modèle et aux jeux de données pertinents.

| Fournisseur  | Tutoriel                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Comment affiner les modèles de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)         | Apprenez à affiner un `gpt-35-turbo` pour un domaine spécifique ("assistant de recettes") en préparant des données d'entraînement, en exécutant la tâche d'affinage et en utilisant le modèle affiné pour l'inférence.                                                                                                                                                                                                             |
| Azure OpenAI | [Tutoriel d'affinage GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Apprenez à affiner un modèle `gpt-35-turbo-0613` **sur Azure** en prenant des mesures pour créer et télécharger des données d'entraînement, exécuter la tâche d'affinage. Déployez et utilisez le nouveau modèle.                                                                                                                                                                                                                                                         |
| Hugging Face | [Affiner les LLMs avec Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Ce billet de blog vous guide dans l'affinage d'un _LLM ouvert_ (ex : `CodeLlama 7B`) en utilisant la bibliothèque [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) et [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) avec des [jeux de données ouverts](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) sur Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Affiner les LLMs avec AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (ou AutoTrain Advanced) est une bibliothèque Python développée par Hugging Face qui permet l'affinage pour de nombreuses tâches différentes, y compris l'affinage des LLM. AutoTrain est une solution sans code et l'affinage peut être effectué dans votre propre cloud, sur Hugging Face Spaces ou localement. Il prend en charge une interface graphique web, une interface en ligne de commande et un entraînement via des fichiers de configuration yaml.             |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Devoir

Sélectionnez l'un des tutoriels ci-dessus et suivez-le. _Nous pourrions reproduire une version de ces tutoriels dans des Jupyter Notebooks dans ce dépôt à titre de référence uniquement. Veuillez utiliser directement les sources originales pour obtenir les dernières versions_.

## Bon travail ! Continuez votre apprentissage.

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances en IA générative !

Félicitations !! Vous avez terminé la dernière leçon de la série v2 de ce cours ! Ne cessez pas d'apprendre et de construire. \*\*Consultez la page [RESSOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) pour une liste de suggestions supplémentaires sur ce sujet.

Notre série de leçons v1 a également été mise à jour avec plus de devoirs et de concepts. Prenez donc une minute pour rafraîchir vos connaissances - et n'hésitez pas à [partager vos questions et commentaires](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) pour nous aider à améliorer ces leçons pour la communauté.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.