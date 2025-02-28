# Introduction à l'IA générative et aux modèles de langage de grande taille

[![Introduction à l'IA générative et aux modèles de langage de grande taille](../../../translated_images/01-lesson-banner.png?WT.e847a56bbd30dfd9341d21c4e957c3bcd9de94d06aa5bc91692a69cb1af2c994.fr.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson-1-gh?WT.mc_id=academic-105485-koreyst)

_(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

L'IA générative est une intelligence artificielle capable de générer du texte, des images et d'autres types de contenu. Ce qui la rend fantastique, c'est qu'elle démocratise l'IA : tout le monde peut l'utiliser avec aussi peu qu'une invite textuelle, une phrase écrite dans un langage naturel. Il n'est pas nécessaire d'apprendre un langage comme Java ou SQL pour accomplir quelque chose d'utile, il suffit d'utiliser votre langue, d'exprimer ce que vous voulez, et une suggestion d'un modèle d'IA apparaît. Les applications et l'impact sont énormes : vous pouvez rédiger ou comprendre des rapports, écrire des applications et bien plus encore, le tout en quelques secondes.

Dans ce programme, nous explorerons comment notre startup exploite l'IA générative pour ouvrir de nouveaux scénarios dans le monde de l'éducation et comment nous relevons les défis inévitables associés aux implications sociales de son application et aux limitations technologiques.

## Introduction

Cette leçon couvrira :

- Introduction au scénario commercial : notre idée de startup et notre mission.
- L'IA générative et comment nous avons atteint le paysage technologique actuel.
- Fonctionnement interne d'un modèle de langage de grande taille.
- Principales capacités et cas d'utilisation pratiques des modèles de langage de grande taille.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous comprendrez :

- Ce qu'est l'IA générative et comment fonctionnent les modèles de langage de grande taille.
- Comment vous pouvez exploiter les modèles de langage de grande taille pour différents cas d'utilisation, en mettant l'accent sur les scénarios éducatifs.

## Scénario : notre startup éducative

L'intelligence artificielle générative (IA) représente le sommet de la technologie IA, repoussant les limites de ce que l'on pensait autrefois impossible. Les modèles d'IA générative ont plusieurs capacités et applications, mais pour ce programme, nous explorerons comment elle révolutionne l'éducation grâce à une startup fictive. Nous désignerons cette startup comme _notre startup_. Notre startup travaille dans le domaine de l'éducation avec la mission ambitieuse de

> _améliorer l'accessibilité à l'apprentissage à l'échelle mondiale, en garantissant un accès équitable à l'éducation et en offrant des expériences d'apprentissage personnalisées à chaque apprenant, selon ses besoins_.

L'équipe de notre startup est consciente que nous ne pourrons pas atteindre cet objectif sans exploiter l'un des outils les plus puissants de notre époque – les modèles de langage de grande taille (LLM).

L'IA générative devrait révolutionner notre façon d'apprendre et d'enseigner aujourd'hui, avec des étudiants disposant de professeurs virtuels 24 heures sur 24 qui fournissent d'énormes quantités d'informations et d'exemples, et des enseignants capables d'utiliser des outils innovants pour évaluer leurs étudiants et donner des retours.

![Cinq jeunes étudiants regardant un moniteur - image par DALLE2](../../../translated_images/students-by-DALLE2.png?WT.540d623be2689660f18d0c126177502c651e2269597164cc09b60d7d90b830cf.fr.mc_id=academic-105485-koreyst)

Pour commencer, définissons quelques concepts de base et la terminologie que nous utiliserons tout au long du programme.

## Comment avons-nous obtenu l'IA générative ?

Malgré le _battage médiatique_ extraordinaire créé récemment par l'annonce des modèles d'IA générative, cette technologie est en développement depuis des décennies, avec les premiers efforts de recherche remontant aux années 60. Nous sommes maintenant à un point où l'IA a des capacités cognitives humaines, comme la conversation, comme le montrent par exemple [OpenAI ChatGPT](https://openai.com/chatgpt) ou [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), qui utilise également un modèle GPT pour les conversations de recherche web Bing.

Pour revenir un peu en arrière, les tout premiers prototypes d'IA consistaient en des chatbots dactylographiés, s'appuyant sur une base de connaissances extraite d'un groupe d'experts et représentée dans un ordinateur. Les réponses dans la base de connaissances étaient déclenchées par des mots-clés apparaissant dans le texte d'entrée.
Cependant, il est rapidement devenu clair qu'une telle approche, utilisant des chatbots dactylographiés, ne se généralisait pas bien.

### Une approche statistique de l'IA : l'apprentissage automatique

Un tournant est arrivé dans les années 90, avec l'application d'une approche statistique à l'analyse de texte. Cela a conduit au développement de nouveaux algorithmes – connus sous le nom d'apprentissage automatique – capables d'apprendre des motifs à partir de données, sans être explicitement programmés. Cette approche permet à une machine de simuler la compréhension du langage humain : un modèle statistique est entraîné sur des appariements texte-étiquette, permettant au modèle de classer un texte d'entrée inconnu avec une étiquette prédéfinie représentant l'intention du message.

### Réseaux neuronaux et assistants virtuels modernes

Plus récemment, l'évolution technologique du matériel, capable de gérer de plus grandes quantités de données et des calculs plus complexes, a encouragé la recherche dans les domaines de l'IA, conduisant au développement d'algorithmes d'apprentissage automatique avancés – appelés réseaux neuronaux ou algorithmes d'apprentissage profond.

Les réseaux neuronaux (et en particulier les réseaux neuronaux récurrents – RNNs) ont considérablement amélioré le traitement du langage naturel, permettant de représenter le sens du texte de manière plus significative, en valorisant le contexte d'un mot dans une phrase.

C'est la technologie qui a alimenté les assistants virtuels nés dans la première décennie du nouveau siècle, très compétents pour interpréter le langage humain, identifier un besoin et effectuer une action pour le satisfaire – comme répondre avec un script prédéfini ou consommer un service tiers.

### Aujourd'hui, l'IA générative

C'est ainsi que nous sommes arrivés à l'IA générative aujourd'hui, qui peut être considérée comme un sous-ensemble de l'apprentissage profond.

![IA, ML, DL et IA générative](../../../translated_images/AI-diagram.png?WT.e126d57e1a443697cd851d5d04d66753225b4d910f4aff65f9f28215b528471a.fr.mc_id=academic-105485-koreyst)

Après des décennies de recherche dans le domaine de l'IA, une nouvelle architecture de modèle – appelée _Transformer_ – a surmonté les limites des RNNs, étant capable de prendre en entrée des séquences de texte beaucoup plus longues. Les Transformers sont basés sur le mécanisme d'attention, permettant au modèle de donner des poids différents aux entrées qu'il reçoit, en 'prêtant plus d'attention' là où se concentre l'information la plus pertinente, indépendamment de leur ordre dans la séquence de texte.

La plupart des modèles d'IA générative récents – également connus sous le nom de modèles de langage de grande taille (LLM), car ils fonctionnent avec des entrées et sorties textuelles – sont en effet basés sur cette architecture. Ce qui est intéressant à propos de ces modèles – entraînés sur une énorme quantité de données non étiquetées provenant de sources diverses comme des livres, des articles et des sites Web – c'est qu'ils peuvent être adaptés à une grande variété de tâches et générer un texte grammaticalement correct avec une apparence de créativité. Ainsi, non seulement ils ont incroyablement amélioré la capacité d'une machine à 'comprendre' un texte d'entrée, mais ils ont également permis à leur capacité de générer une réponse originale en langage humain.

## Comment fonctionnent les modèles de langage de grande taille ?

Dans le prochain chapitre, nous allons explorer différents types de modèles d'IA générative, mais pour l'instant, examinons comment fonctionnent les modèles de langage de grande taille, en mettant l'accent sur les modèles GPT (Generative Pre-trained Transformer) d'OpenAI.

- **Tokenizer, texte en chiffres** : Les modèles de langage de grande taille reçoivent un texte en entrée et génèrent un texte en sortie. Cependant, étant des modèles statistiques, ils fonctionnent beaucoup mieux avec des chiffres que des séquences de texte. C'est pourquoi chaque entrée au modèle est traitée par un tokenizer, avant d'être utilisée par le modèle principal. Un token est un morceau de texte – composé d'un nombre variable de caractères, donc la tâche principale du tokenizer est de diviser l'entrée en un tableau de tokens. Ensuite, chaque token est mappé avec un index de token, qui est le codage entier du morceau de texte original.

![Exemple de tokenisation](../../../translated_images/tokenizer-example.png?WT.3b4be927057ceb39216ffc617cde2fd4d843e0d7557fc81d08a0018831f601ed.fr.mc_id=academic-105485-koreyst)

- **Prédiction des tokens de sortie** : Étant donné n tokens en entrée (avec un maximum de n variant d'un modèle à l'autre), le modèle est capable de prédire un token en sortie. Ce token est ensuite incorporé dans l'entrée de l'itération suivante, dans un schéma de fenêtre élargissante, permettant une meilleure expérience utilisateur d'obtenir une (ou plusieurs) phrase(s) en réponse. Cela explique pourquoi, si vous avez déjà joué avec ChatGPT, vous avez peut-être remarqué qu'il semble parfois s'arrêter au milieu d'une phrase.

- **Processus de sélection, distribution de probabilité** : Le token de sortie est choisi par le modèle en fonction de sa probabilité d'apparaître après la séquence de texte actuelle. Cela est dû au fait que le modèle prédit une distribution de probabilité sur tous les 'tokens suivants' possibles, calculée en fonction de son entraînement. Cependant, le token ayant la probabilité la plus élevée n'est pas toujours choisi à partir de la distribution résultante. Un degré de hasard est ajouté à ce choix, de sorte que le modèle agit de manière non déterministe - nous n'obtenons pas exactement la même sortie pour la même entrée. Ce degré de hasard est ajouté pour simuler le processus de pensée créative et il peut être ajusté à l'aide d'un paramètre de modèle appelé température.

## Comment notre startup peut-elle tirer parti des modèles de langage de grande taille ?

Maintenant que nous avons une meilleure compréhension du fonctionnement interne d'un modèle de langage de grande taille, voyons quelques exemples pratiques des tâches les plus courantes qu'ils peuvent accomplir avec succès, en gardant un œil sur notre scénario commercial.
Nous avons dit que la principale capacité d'un modèle de langage de grande taille est _de générer un texte à partir de zéro, à partir d'une entrée textuelle, écrite en langage naturel_.

Mais quel type d'entrée et de sortie textuelles ?
L'entrée d'un modèle de langage de grande taille est connue sous le nom de prompt, tandis que la sortie est connue sous le nom de completion, un terme qui fait référence au mécanisme du modèle de génération du prochain token pour compléter l'entrée actuelle. Nous allons approfondir ce qu'est un prompt et comment le concevoir de manière à tirer le meilleur parti de notre modèle. Mais pour l'instant, disons simplement qu'un prompt peut inclure :

- Une **instruction** spécifiant le type de sortie que nous attendons du modèle. Cette instruction peut parfois inclure des exemples ou des données supplémentaires.

  1. Résumé d'un article, d'un livre, d'avis sur des produits et plus encore, ainsi que l'extraction d'informations à partir de données non structurées.
    
    ![Exemple de résumé](../../../translated_images/summarization-example.png?WT.cf0bac4d43b9de29ec37e1b7707d9bd67e030f4e884a0ae778c6a3c36be77d79.fr.mc_id=academic-105485-koreyst)
  
  2. Idéation créative et conception d'un article, d'un essai, d'une tâche ou plus encore.
      
     ![Exemple d'écriture créative](../../../translated_images/creative-writing-example.png?WT.04b03c92f46ed96df1138828e37760ac81e06eaa8602de8c4b175a9c514c9a14.fr.mc_id=academic-105485-koreyst)

- Une **question**, posée sous la forme d'une conversation avec un agent.
  
  ![Exemple de conversation](../../../translated_images/conversation-example.png?WT.f904fd4c48fbf695b8e5d334e1ec02d66830bbc679ad4b5195f1c563e9bfbdc1.fr.mc_id=academic-105485-koreyst)

- Un morceau de **texte à compléter**, ce qui constitue implicitement une demande d'assistance à l'écriture.
  
  ![Exemple de complétion de texte](../../../translated_images/text-completion-example.png?WT.9a641431b14ebbbcaa7d22def9729cf8cc7ab358b1dbc948653e43af47e41f73.fr.mc_id=academic-105485-koreyst)

- Un morceau de **code** accompagné de la demande de l'expliquer et de le documenter, ou un commentaire demandant de générer un morceau de code effectuant une tâche spécifique.
  
  ![Exemple de codage](../../../translated_images/coding-example.png?WT.75933a45164ffb74ffbb4a72c8f77b0f76ebcdc676a58ad2871de5d32db63515.fr.mc_id=academic-105485-koreyst)

Les exemples ci-dessus sont assez simples et ne prétendent pas être une démonstration exhaustive des capacités des modèles de langage de grande taille. Ils veulent juste montrer le potentiel de l'utilisation de l'IA générative, en particulier mais pas uniquement dans le contexte éducatif.

De plus, la sortie d'un modèle d'IA générative n'est pas parfaite et parfois la créativité du modèle peut jouer contre lui, entraînant une sortie qui est une combinaison de mots que l'utilisateur humain peut interpréter comme une mystification de la réalité, ou elle peut être offensante. L'IA générative n'est pas intelligente - du moins dans la définition plus complète de l'intelligence, incluant le raisonnement critique et créatif ou l'intelligence émotionnelle ; elle n'est pas déterministe, et elle n'est pas fiable, car des fabrications, telles que des références erronées, du contenu et des déclarations, peuvent être combinées avec des informations correctes, et présentées de manière persuasive et confiante. Dans les leçons suivantes, nous aborderons toutes ces limitations et verrons ce que nous pouvons faire pour les atténuer.

## Devoir

Votre devoir est de lire davantage sur [l'IA générative](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) et d'essayer d'identifier un domaine où vous ajouteriez l'IA générative aujourd'hui qui ne l'a pas. En quoi l'impact serait-il différent de le faire à l'ancienne, pouvez-vous faire quelque chose que vous ne pouviez pas faire auparavant, ou êtes-vous plus rapide ? Écrivez un résumé de 300 mots sur ce à quoi ressemblerait votre startup IA de rêve et incluez des titres comme "Problème", "Comment j'utiliserais l'IA", "Impact" et éventuellement un plan d'affaires.

Si vous avez accompli cette tâche, vous pourriez même être prêt à postuler à l'incubateur de Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst), nous offrons des crédits pour Azure, OpenAI, du mentorat et bien plus encore, allez voir !

## Vérification des connaissances

Qu'est-ce qui est vrai à propos des modèles de langage de grande taille ?

1. Vous obtenez la même réponse exacte à chaque fois.
1. Il fait les choses parfaitement, excellent pour additionner des chiffres, produire du code fonctionnel, etc.
1. La réponse peut varier malgré l'utilisation du même prompt. Il est également excellent pour vous donner une première ébauche de quelque chose, que ce soit du texte ou du code. Mais vous devez améliorer les résultats.

R : 3, un LLM est non déterministe, la réponse varie, cependant, vous pouvez contrôler sa variance via un réglage de température. Vous ne devriez pas non plus vous attendre à ce qu'il fasse les choses parfaitement, il est là pour faire le gros du travail pour vous, ce qui signifie souvent que vous obtenez une bonne première tentative de quelque chose que vous devez améliorer progressivement.

## Bon travail ! Continuez le voyage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à améliorer vos connaissances en IA générative !

Rendez-vous à la leçon 2 où nous verrons comment [explorer et comparer différents types de LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst) !

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée par intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l'utilisation de cette traduction.