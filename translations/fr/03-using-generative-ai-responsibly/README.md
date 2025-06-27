<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:10:09+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "fr"
}
-->
# Utiliser l'IA Générative de Manière Responsable

> _Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon_

Il est facile d'être fasciné par l'IA, et l'IA générative en particulier, mais il est essentiel de réfléchir à la manière de l'utiliser de manière responsable. Vous devez envisager des éléments tels que garantir que le résultat est équitable, non nuisible, et plus encore. Ce chapitre vise à vous fournir le contexte mentionné, ce qu'il faut prendre en compte, et comment prendre des mesures actives pour améliorer votre utilisation de l'IA.

## Introduction

Cette leçon couvrira :

- Pourquoi vous devriez donner la priorité à l'IA Responsable lors de la création d'applications d'IA Générative.
- Les principes fondamentaux de l'IA Responsable et leur lien avec l'IA Générative.
- Comment mettre ces principes de l'IA Responsable en pratique grâce à des stratégies et des outils.

## Objectifs d'Apprentissage

Après avoir terminé cette leçon, vous saurez :

- L'importance de l'IA Responsable lors de la création d'applications d'IA Générative.
- Quand réfléchir et appliquer les principes fondamentaux de l'IA Responsable lors de la création d'applications d'IA Générative.
- Quels outils et stratégies sont à votre disposition pour mettre le concept de l'IA Responsable en pratique.

## Principes de l'IA Responsable

L'excitation autour de l'IA Générative n'a jamais été aussi forte. Cette excitation a attiré de nombreux nouveaux développeurs, de l'attention et des financements dans cet espace. Bien que cela soit très positif pour quiconque cherche à construire des produits et des entreprises utilisant l'IA Générative, il est également important de procéder de manière responsable.

Tout au long de ce cours, nous nous concentrons sur la création de notre startup et de notre produit éducatif d'IA. Nous utiliserons les principes de l'IA Responsable : Équité, Inclusion, Fiabilité/Sécurité, Sécurité & Confidentialité, Transparence et Responsabilité. Avec ces principes, nous explorerons leur relation avec notre utilisation de l'IA Générative dans nos produits.

## Pourquoi Prioriser l'IA Responsable

Lors de la création d'un produit, adopter une approche centrée sur l'humain en gardant à l'esprit l'intérêt de l'utilisateur mène aux meilleurs résultats.

L'unicité de l'IA Générative réside dans sa capacité à créer des réponses, des informations, des conseils et du contenu utiles pour les utilisateurs. Cela peut se faire sans de nombreuses étapes manuelles, ce qui peut conduire à des résultats très impressionnants. Sans planification et stratégies adéquates, cela peut également malheureusement conduire à des résultats nuisibles pour vos utilisateurs, votre produit, et la société dans son ensemble.

Examinons certains (mais pas tous) de ces résultats potentiellement nuisibles :

### Hallucinations

Les hallucinations sont un terme utilisé pour décrire quand un modèle de langage produit du contenu qui est soit complètement insensé, soit quelque chose que nous savons être factuellement incorrect basé sur d'autres sources d'information.

Prenons par exemple que nous construisons une fonctionnalité pour notre startup qui permet aux étudiants de poser des questions historiques à un modèle. Un étudiant pose la question `Who was the sole survivor of Titanic?`

Le modèle produit une réponse telle que celle ci-dessous :

Cette réponse est très confiante et détaillée. Malheureusement, elle est incorrecte. Même avec un minimum de recherche, on découvrirait qu'il y avait plus d'un survivant du désastre du Titanic. Pour un étudiant qui commence tout juste à rechercher ce sujet, cette réponse peut être suffisamment persuasive pour ne pas être remise en question et traitée comme un fait. Les conséquences de cela peuvent conduire à ce que le système d'IA soit peu fiable et nuise à la réputation de notre startup.

Avec chaque itération d'un modèle de langage donné, nous avons constaté des améliorations de performance pour minimiser les hallucinations. Même avec cette amélioration, nous, en tant que développeurs d'applications et utilisateurs, devons rester conscients de ces limitations.

### Contenu Nuisible

Nous avons couvert dans la section précédente lorsque un modèle de langage produit des réponses incorrectes ou insensées. Un autre risque dont nous devons être conscients est lorsque un modèle répond avec du contenu nuisible.

Le contenu nuisible peut être défini comme :

- Fournir des instructions ou encourager l'automutilation ou le préjudice à certains groupes.
- Contenu haineux ou dégradant.
- Guider la planification de toute attaque ou acte violent.
- Fournir des instructions sur la manière de trouver du contenu illégal ou de commettre des actes illégaux.
- Afficher du contenu sexuellement explicite.

Pour notre startup, nous voulons nous assurer que nous avons les bons outils et stratégies en place pour empêcher ce type de contenu d'être vu par les étudiants.

### Manque d'Équité

L'équité est définie comme "garantir qu'un système d'IA est exempt de biais et de discrimination et qu'il traite tout le monde de manière équitable et égale." Dans le monde de l'IA Générative, nous voulons nous assurer que les visions du monde exclusionnaires des groupes marginalisés ne sont pas renforcées par la sortie du modèle.

Ces types de sorties ne sont pas seulement destructeurs pour construire des expériences de produit positives pour nos utilisateurs, mais ils causent également des dommages sociétaux supplémentaires. En tant que développeurs d'applications, nous devrions toujours garder à l'esprit une base d'utilisateurs large et diversifiée lors de la création de solutions avec l'IA Générative.

## Comment Utiliser l'IA Générative de Manière Responsable

Maintenant que nous avons identifié l'importance de l'IA Générative Responsable, examinons 4 étapes que nous pouvons suivre pour construire nos solutions d'IA de manière responsable :

### Mesurer les Potentiels Préjudices

Dans les tests logiciels, nous testons les actions attendues d'un utilisateur sur une application. De la même manière, tester un ensemble diversifié de prompts que les utilisateurs sont le plus susceptibles d'utiliser est un bon moyen de mesurer les préjudices potentiels.

Étant donné que notre startup construit un produit éducatif, il serait bon de préparer une liste de prompts liés à l'éducation. Cela pourrait couvrir un certain sujet, des faits historiques, et des prompts sur la vie étudiante.

### Atténuer les Potentiels Préjudices

Il est maintenant temps de trouver des moyens où nous pouvons prévenir ou limiter le préjudice potentiel causé par le modèle et ses réponses. Nous pouvons examiner cela en 4 couches différentes :

- **Modèle**. Choisir le bon modèle pour le bon cas d'utilisation. Les modèles plus grands et plus complexes comme GPT-4 peuvent causer plus de risque de contenu nuisible lorsqu'ils sont appliqués à des cas d'utilisation plus petits et plus spécifiques. Utiliser vos données d'entraînement pour un ajustement fin réduit également le risque de contenu nuisible.

- **Système de Sécurité**. Un système de sécurité est un ensemble d'outils et de configurations sur la plateforme servant le modèle qui aide à atténuer le préjudice. Un exemple de cela est le système de filtrage de contenu sur le service Azure OpenAI. Les systèmes devraient également détecter les attaques par jailbreak et les activités indésirables comme les demandes de bots.

- **Métaprompt**. Les métaprompts et l'ancrage sont des moyens de diriger ou de limiter le modèle en fonction de certains comportements et informations. Cela pourrait être l'utilisation d'entrées système pour définir certaines limites du modèle. De plus, fournir des sorties qui sont plus pertinentes pour le domaine ou le périmètre du système.

Cela peut également être l'utilisation de techniques comme la génération augmentée par récupération (RAG) pour que le modèle ne tire des informations que d'une sélection de sources fiables. Il y a une leçon plus tard dans ce cours pour [construire des applications de recherche](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Expérience Utilisateur**. La couche finale est là où l'utilisateur interagit directement avec le modèle via l'interface de notre application d'une certaine manière. De cette manière, nous pouvons concevoir l'UI/UX pour limiter l'utilisateur sur les types d'entrées qu'il peut envoyer au modèle ainsi que le texte ou les images affichés à l'utilisateur. Lors du déploiement de l'application d'IA, nous devons également être transparents sur ce que notre application d'IA Générative peut et ne peut pas faire.

Nous avons une leçon entière dédiée à [Concevoir l'UX pour les Applications d'IA](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Évaluer le modèle**. Travailler avec des modèles de langage peut être difficile car nous n'avons pas toujours le contrôle sur les données sur lesquelles le modèle a été entraîné. Néanmoins, nous devrions toujours évaluer la performance et les sorties du modèle. Il est toujours important de mesurer la précision, la similarité, l'ancrage, et la pertinence de la sortie du modèle. Cela aide à fournir de la transparence et de la confiance aux parties prenantes et aux utilisateurs.

### Opérer une Solution d'IA Générative Responsable

Construire une pratique opérationnelle autour de vos applications d'IA est la dernière étape. Cela inclut de collaborer avec d'autres parties de notre startup comme le service juridique et la sécurité pour garantir que nous sommes conformes à toutes les politiques réglementaires. Avant le lancement, nous voulons également élaborer des plans autour de la livraison, de la gestion des incidents, et du retour en arrière pour éviter tout préjudice à nos utilisateurs.

## Outils

Bien que le travail de développement de solutions d'IA Responsable puisse sembler beaucoup, c'est un travail qui vaut bien l'effort. À mesure que le domaine de l'IA Générative se développe, davantage d'outils pour aider les développeurs à intégrer efficacement la responsabilité dans leurs flux de travail se développeront. Par exemple, le [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) peut aider à détecter du contenu et des images nuisibles via une requête API.

## Vérification des Connaissances

Quelles sont certaines des choses dont vous devez vous soucier pour garantir une utilisation responsable de l'IA ?

1. Que la réponse est correcte.
1. L'utilisation nuisible, que l'IA n'est pas utilisée à des fins criminelles.
1. Garantir que l'IA est exempte de biais et de discrimination.

A: 2 et 3 sont corrects. L'IA Responsable vous aide à réfléchir à comment atténuer les effets nuisibles et les biais, et plus encore.

## 🚀 Défi

Renseignez-vous sur [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) et voyez ce que vous pouvez adopter pour votre usage.

## Excellent Travail, Continuez Votre Apprentissage

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA Générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à développer vos connaissances en IA Générative !

Rendez-vous à la Leçon 4 où nous examinerons les [Fondamentaux de l'Ingénierie de Prompts](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) !

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle humaine est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.