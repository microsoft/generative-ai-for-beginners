<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ea4bbe640847aafbbba14dae4625e9af",
  "translation_date": "2025-06-25T15:03:23+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "fr"
}
-->
# Construire des applications de chat alimentées par l'IA générative

[![Construire des applications de chat alimentées par l'IA générative](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.fr.png)](https://aka.ms/gen-ai-lessons7-gh?WT.mc_id=academic-105485-koreyst)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

Maintenant que nous avons vu comment nous pouvons créer des applications de génération de texte, examinons les applications de chat.

Les applications de chat se sont intégrées dans notre vie quotidienne, offrant bien plus qu'un simple moyen de conversation informelle. Elles sont des éléments essentiels du service client, du support technique et même des systèmes de conseil sophistiqués. Il est probable que vous ayez récemment reçu de l'aide d'une application de chat. À mesure que nous intégrons des technologies plus avancées comme l'IA générative dans ces plateformes, la complexité augmente, tout comme les défis.

Certaines questions auxquelles nous devons répondre sont :

- **Construire l'application**. Comment construisons-nous efficacement et intégrons-nous harmonieusement ces applications alimentées par l'IA pour des cas d'utilisation spécifiques ?
- **Surveillance**. Une fois déployées, comment pouvons-nous surveiller et garantir que les applications fonctionnent au plus haut niveau de qualité, tant en termes de fonctionnalité que de respect des [six principes de l'IA responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) ?

Alors que nous avançons dans une ère définie par l'automatisation et les interactions homme-machine fluides, comprendre comment l'IA générative transforme la portée, la profondeur et l'adaptabilité des applications de chat devient essentiel. Cette leçon examinera les aspects de l'architecture qui soutiennent ces systèmes complexes, explorera les méthodologies pour les affiner pour des tâches spécifiques à un domaine, et évaluera les métriques et considérations pertinentes pour garantir un déploiement responsable de l'IA.

## Introduction

Cette leçon couvre :

- Les techniques pour construire et intégrer efficacement des applications de chat.
- Comment appliquer la personnalisation et l'affinement aux applications.
- Les stratégies et considérations pour surveiller efficacement les applications de chat.

## Objectifs d'apprentissage

À la fin de cette leçon, vous serez capable de :

- Décrire les considérations pour construire et intégrer des applications de chat dans des systèmes existants.
- Personnaliser les applications de chat pour des cas d'utilisation spécifiques.
- Identifier les principales métriques et considérations pour surveiller et maintenir efficacement la qualité des applications de chat alimentées par l'IA.
- Assurer que les applications de chat exploitent l'IA de manière responsable.

## Intégrer l'IA générative dans les applications de chat

Améliorer les applications de chat grâce à l'IA générative ne consiste pas seulement à les rendre plus intelligentes ; il s'agit d'optimiser leur architecture, leur performance et leur interface utilisateur pour offrir une expérience utilisateur de qualité. Cela implique d'explorer les fondations architecturales, les intégrations API, et les considérations d'interface utilisateur. Cette section vise à vous offrir une feuille de route complète pour naviguer dans ces paysages complexes, que vous les intégriez dans des systèmes existants ou que vous les construisiez en tant que plateformes autonomes.

À la fin de cette section, vous serez équipé de l'expertise nécessaire pour construire et intégrer efficacement des applications de chat.

### Chatbot ou application de chat ?

Avant de plonger dans la construction d'applications de chat, comparons les "chatbots" aux "applications de chat alimentées par l'IA", qui ont des rôles et des fonctionnalités distincts. Le principal objectif d'un chatbot est d'automatiser des tâches conversationnelles spécifiques, telles que répondre à des questions fréquemment posées ou suivre un colis. Il est généralement régi par une logique basée sur des règles ou des algorithmes d'IA complexes. En revanche, une application de chat alimentée par l'IA est un environnement beaucoup plus vaste conçu pour faciliter diverses formes de communication numérique, telles que les discussions textuelles, vocales et vidéo entre utilisateurs humains. Sa caractéristique principale est l'intégration d'un modèle d'IA générative qui simule des conversations nuancées et humaines, générant des réponses basées sur une grande variété d'entrées et d'indices contextuels. Une application de chat alimentée par l'IA générative peut s'engager dans des discussions en domaine ouvert, s'adapter à des contextes conversationnels évolutifs, et même produire des dialogues créatifs ou complexes.

Le tableau ci-dessous présente les principales différences et similitudes pour nous aider à comprendre leurs rôles uniques dans la communication numérique.

| Chatbot                               | Application de chat alimentée par l'IA générative |
| ------------------------------------- | ------------------------------------------------ |
| Axé sur les tâches et basé sur des règles | Sensible au contexte                              |
| Souvent intégré dans des systèmes plus vastes | Peut héberger un ou plusieurs chatbots            |
| Limité aux fonctions programmées       | Intègre des modèles d'IA générative               |
| Interactions spécialisées et structurées | Capable de discussions en domaine ouvert          |

### Exploiter les fonctionnalités préconstruites avec les SDK et les API

Lors de la construction d'une application de chat, une première étape consiste à évaluer ce qui existe déjà. Utiliser les SDK et les API pour construire des applications de chat est une stratégie avantageuse pour diverses raisons. En intégrant des SDK et des API bien documentés, vous positionnez stratégiquement votre application pour un succès à long terme, en abordant les préoccupations de scalabilité et de maintenance.

- **Accélère le processus de développement et réduit les frais généraux** : S'appuyer sur des fonctionnalités préconstruites au lieu du processus coûteux de les construire vous-même vous permet de vous concentrer sur d'autres aspects de votre application que vous pouvez juger plus importants, comme la logique métier.
- **Meilleure performance** : Lors de la construction de fonctionnalités à partir de zéro, vous vous demanderez éventuellement "Comment cela évolue-t-il ? Cette application est-elle capable de gérer un afflux soudain d'utilisateurs ?" Les SDK et API bien entretenus ont souvent des solutions intégrées pour ces préoccupations.
- **Maintenance plus facile** : Les mises à jour et améliorations sont plus faciles à gérer car la plupart des API et SDK nécessitent simplement une mise à jour d'une bibliothèque lorsqu'une nouvelle version est publiée.
- **Accès à la technologie de pointe** : Exploiter des modèles qui ont été affinés et entraînés sur des ensembles de données étendus offre à votre application des capacités de langage naturel.

Accéder à la fonctionnalité d'un SDK ou d'une API implique généralement d'obtenir l'autorisation d'utiliser les services fournis, souvent par l'utilisation d'une clé unique ou d'un jeton d'authentification. Nous utiliserons la bibliothèque Python d'OpenAI pour explorer à quoi cela ressemble. Vous pouvez également l'essayer par vous-même dans le [carnet pour OpenAI](../../../07-building-chat-applications/python/oai-assignment.ipynb) ou le [carnet pour les services Azure OpenAI](../../../07-building-chat-applications/python/aoai-assignment.ipynb) pour cette leçon.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

L'exemple ci-dessus utilise le modèle GPT-3.5 Turbo pour compléter l'invite, mais remarquez que la clé API est définie avant de le faire. Vous recevriez une erreur si vous ne définissiez pas la clé.

## Expérience Utilisateur (UX)

Les principes généraux de l'UX s'appliquent aux applications de chat, mais voici quelques considérations supplémentaires qui deviennent particulièrement importantes en raison des composants d'apprentissage automatique impliqués.

- **Mécanisme pour traiter l'ambiguïté** : Les modèles d'IA générative génèrent occasionnellement des réponses ambiguës. Une fonctionnalité permettant aux utilisateurs de demander des éclaircissements peut être utile s'ils rencontrent ce problème.
- **Rétention du contexte** : Les modèles d'IA générative avancés ont la capacité de se souvenir du contexte dans une conversation, ce qui peut être un atout nécessaire pour l'expérience utilisateur. Donner aux utilisateurs la possibilité de contrôler et de gérer le contexte améliore l'expérience utilisateur, mais introduit le risque de conserver des informations sensibles sur les utilisateurs. Les considérations sur la durée de conservation de ces informations, comme l'introduction d'une politique de rétention, peuvent équilibrer le besoin de contexte avec la confidentialité.
- **Personnalisation** : Avec la capacité d'apprendre et de s'adapter, les modèles d'IA offrent une expérience individualisée pour un utilisateur. Adapter l'expérience utilisateur grâce à des fonctionnalités comme les profils utilisateurs non seulement fait en sorte que l'utilisateur se sente compris, mais cela l'aide aussi dans sa recherche de réponses spécifiques, créant une interaction plus efficace et satisfaisante.

Un exemple de personnalisation est les paramètres "Instructions personnalisées" dans ChatGPT d'OpenAI. Cela vous permet de fournir des informations sur vous-même qui peuvent être un contexte important pour vos invites. Voici un exemple d'instruction personnalisée.

![Paramètres d'instructions personnalisées dans ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.fr.png)

Ce "profil" incite ChatGPT à créer un plan de leçon sur les listes chaînées. Remarquez que ChatGPT prend en compte que l'utilisateur peut vouloir un plan de leçon plus approfondi en fonction de son expérience.

![Une invite dans ChatGPT pour un plan de leçon sur les listes chaînées](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.fr.png)

### Le cadre de message système de Microsoft pour les modèles de langage de grande taille

[Microsoft a fourni des conseils](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) pour rédiger des messages système efficaces lors de la génération de réponses à partir de LLMs, décomposés en 4 domaines :

1. Définir pour qui est le modèle, ainsi que ses capacités et ses limites.
2. Définir le format de sortie du modèle.
3. Fournir des exemples spécifiques qui démontrent le comportement souhaité du modèle.
4. Fournir des garde-fous comportementaux supplémentaires.

### Accessibilité

Qu'un utilisateur ait des déficiences visuelles, auditives, motrices ou cognitives, une application de chat bien conçue devrait être utilisable par tous. La liste suivante décompose les fonctionnalités spécifiques visant à améliorer l'accessibilité pour divers handicaps utilisateurs.

- **Fonctionnalités pour les déficiences visuelles** : Thèmes à contraste élevé et texte redimensionnable, compatibilité avec les lecteurs d'écran.
- **Fonctionnalités pour les déficiences auditives** : Fonctions de texte-à-parole et de parole-à-texte, indices visuels pour les notifications audio.
- **Fonctionnalités pour les déficiences motrices** : Support de navigation par clavier, commandes vocales.
- **Fonctionnalités pour les déficiences cognitives** : Options de langage simplifié.

## Personnalisation et Affinage pour les Modèles de Langage Spécifiques à un Domaine

Imaginez une application de chat qui comprend le jargon de votre entreprise et anticipe les requêtes spécifiques que ses utilisateurs posent fréquemment. Il existe quelques approches qui méritent d'être mentionnées :

- **Exploiter les modèles DSL**. DSL signifie langage spécifique au domaine. Vous pouvez exploiter un modèle DSL entraîné sur un domaine spécifique pour comprendre ses concepts et scénarios.
- **Appliquer l'affinage**. L'affinage est le processus de formation supplémentaire de votre modèle avec des données spécifiques.

## Personnalisation : Utiliser un DSL

Exploiter des modèles de langage spécifiques à un domaine (modèles DSL) peut améliorer l'engagement des utilisateurs en fournissant des interactions spécialisées et contextuellement pertinentes. C'est un modèle qui est entraîné ou affiné pour comprendre et générer du texte lié à un domaine, une industrie ou un sujet spécifique. Les options pour utiliser un modèle DSL peuvent varier de l'entraînement d'un modèle à partir de zéro à l'utilisation de modèles préexistants via des SDK et des API. Une autre option est l'affinage, qui consiste à prendre un modèle pré-entraîné existant et à l'adapter à un domaine spécifique.

## Personnalisation : Appliquer l'affinage

L'affinage est souvent envisagé lorsqu'un modèle pré-entraîné est insuffisant dans un domaine spécialisé ou une tâche spécifique.

Par exemple, les requêtes médicales sont complexes et nécessitent beaucoup de contexte. Lorsqu'un professionnel de la santé diagnostique un patient, il se base sur divers facteurs tels que le mode de vie ou les conditions préexistantes, et peut même s'appuyer sur des revues médicales récentes pour valider son diagnostic. Dans de tels scénarios nuancés, une application de chat IA à usage général ne peut pas être une source fiable.

### Scénario : une application médicale

Considérons une application de chat conçue pour aider les praticiens médicaux en fournissant des références rapides aux directives de traitement, aux interactions médicamenteuses ou aux découvertes de recherche récentes.

Un modèle à usage général pourrait être adéquat pour répondre à des questions médicales de base ou fournir des conseils généraux, mais il pourrait avoir des difficultés avec les points suivants :

- **Cas très spécifiques ou complexes**. Par exemple, un neurologue pourrait demander à l'application : "Quelles sont les meilleures pratiques actuelles pour gérer l'épilepsie résistante aux médicaments chez les patients pédiatriques ?"
- **Manque d'avancées récentes**. Un modèle à usage général pourrait avoir du mal à fournir une réponse actuelle qui intègre les avancées les plus récentes en neurologie et en pharmacologie.

Dans de tels cas, affiner le modèle avec un ensemble de données médicales spécialisées peut considérablement améliorer sa capacité à gérer ces demandes médicales complexes de manière plus précise et fiable. Cela nécessite l'accès à un ensemble de données large et pertinent qui représente les défis et questions spécifiques au domaine qui doivent être abordés.

## Considérations pour une expérience de chat IA de haute qualité

Cette section décrit les critères pour des applications de chat de "haute qualité", qui incluent la capture de métriques exploitables et l'adhésion à un cadre qui exploite la technologie IA de manière responsable.

### Principales métriques

Pour maintenir la performance de haute qualité d'une application, il est essentiel de suivre les principales métriques et considérations. Ces mesures garantissent non seulement la fonctionnalité de l'application, mais évaluent également la qualité du modèle IA et l'expérience utilisateur. Voici une liste qui couvre les métriques de base, d'IA et d'expérience utilisateur à considérer.

| Métrique                       | Définition                                                                                                             | Considérations pour le développeur de chat                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Disponibilité**              | Mesure le temps pendant lequel l'application est opérationnelle et accessible par les utilisateurs.                     | Comment minimiserez-vous les temps d'arrêt ?                              |
| **Temps de réponse**           | Le temps pris par l'application pour répondre à la requête d'un utilisateur.                                           | Comment pouvez-vous optimiser le traitement des requêtes pour améliorer le temps de réponse ? |
| **Précision**                  | Le ratio des prédictions positives vraies par rapport au nombre total de prédictions positives.                        | Comment validerez-vous la précision de votre modèle ?                     |
| **Rappel (Sensibilité)**       | Le ratio des prédictions positives vraies par rapport au nombre réel de positifs.                                      | Comment mesurerez-vous et améliorerez-vous le rappel ?                    |
| **Score F1**                   | La moyenne harmonique de la précision et du rappel, qui équilibre le compromis entre les deux.                         | Quel est votre objectif de score F1 ? Comment équilibrerez-vous la précision et le rappel ? |
| **Perplexité**                 | Mesure dans quelle mesure la distribution de probabilité prédite par le modèle s'aligne avec la distribution réelle des données. | Comment minimiserez-vous la perplexité ?                                  |
| **Métriques de satisfaction utilisateur** | Mesure la perception de l'utilisateur de l'application. Souvent capturée par des enquêtes.                           | À quelle fréquence collecterez-vous les retours des utilisateurs ? Comment vous adapterez-vous en fonction de cela ? |
| **Taux d'erreur**              | Le taux auquel le modèle fait des erreurs dans la compréhension ou la sortie.                                           | Quelles stratégies avez-vous en place pour réduire les taux d'erreur ?    |
| **Cycles de réentraînement**   | La fréquence à laquelle le modèle est mis à jour pour intégrer de nouvelles données et idées.                           | À quelle fréquence réentraînerez-vous le modèle ? Qu'est-ce qui déclenche un cycle de réentraînement ? |
| **Détection d'anomalies**      | Outils et techniques pour identifier des motifs inhabituels qui ne se conforment pas au comportement attendu.          | Comment répondrez-vous aux anomalies ?                                    |

### Mise en œuvre des pratiques d'IA responsable dans les applications de chat

L'approche de Microsoft en matière d'IA responsable a identifié six principes qui devraient guider le développement et l'utilisation de l'IA. Voici les principes, leur définition, et ce qu'un développeur de chat devrait considérer et pourquoi ils devraient les prendre au sérieux.

| Principes              | Définition de Microsoft                                   | Considérations pour le développeur de chat                                | Pourquoi c'est important                                                    |
| ---------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Équité                 | Les systèmes d'IA doivent traiter toutes les personnes de manière équitable. | Assurez-vous que l'application de chat ne discrimine pas sur la base des données utilisateur. | Pour construire la confiance et l'inclusivité parmi les utilisateurs ; évite les conséquences légales. |
| Fiabilité et Sécurité  | Les systèmes d'IA doivent fonctionner de manière fiable et sûre. | Mettez en œuvre des tests et des dispositifs de sécurité pour minimiser les erreurs et les risques. | Assure la satisfaction des utilisateurs et prévient les dommages potentiels. |
| Confidentialité et Sécurité | Les systèmes d'IA doivent être sécurisés et respecter la vie privée. | Mettez en œuvre des mesures de protection des données et de chiffrement solides. | Pour protéger les données sensibles des utilisateurs et se conformer aux lois sur la confidentialité. |
| Inclusion              | Les systèmes d'IA doivent autonomiser tout le monde et engager les gens. | Concevez une interface utilisateur/expérience utilisateur accessible et facile à utiliser pour des publics divers. | Assure qu'un large éventail de personnes peut utiliser l'application efficacement. |
| Transparence           | Les systèmes d'IA doivent être compréhensibles.           | Fournissez une documentation claire et une explication des réponses de l'IA. | Les utilisateurs sont plus susceptibles de faire confiance à un système s'ils peuvent comprendre comment les décisions sont prises

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.