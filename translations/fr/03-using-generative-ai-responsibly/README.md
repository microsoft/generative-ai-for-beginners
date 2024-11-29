# Utiliser l'IA Générative de Manière Responsable

[![Utiliser l'IA Générative de Manière Responsable](../../../translated_images/03-lesson-banner.png?WT.b0b917735411b39a55748e827c5c3121004890110b27f306bfe685c450c81ff9.fr.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson3-gh?WT.mc_id=academic-105485-koreyst)

> _Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon_

Il est facile d'être fasciné par l'IA et en particulier par l'IA générative, mais il est important de réfléchir à la manière de l'utiliser de manière responsable. Il faut considérer des aspects tels que la garantie que les résultats soient équitables, non-nuisibles, et plus encore. Ce chapitre vise à vous fournir le contexte mentionné, ce qu'il faut prendre en compte, et comment prendre des mesures actives pour améliorer votre utilisation de l'IA.

## Introduction

Cette leçon couvrira :

- Pourquoi vous devriez donner la priorité à l'IA Responsable lors de la création d'applications d'IA Générative.
- Les principes fondamentaux de l'IA Responsable et leur relation avec l'IA Générative.
- Comment mettre en pratique ces principes de l'IA Responsable grâce à des stratégies et des outils.

## Objectifs d'Apprentissage

Après avoir complété cette leçon, vous saurez :

- L'importance de l'IA Responsable lors de la création d'applications d'IA Générative.
- Quand réfléchir et appliquer les principes fondamentaux de l'IA Responsable lors de la création d'applications d'IA Générative.
- Quels outils et stratégies sont à votre disposition pour mettre en pratique le concept de l'IA Responsable.

## Principes de l'IA Responsable

L'engouement pour l'IA Générative n'a jamais été aussi fort. Cet enthousiasme a attiré de nombreux nouveaux développeurs, de l'attention et des financements dans ce domaine. Bien que cela soit très positif pour quiconque cherche à construire des produits et des entreprises utilisant l'IA Générative, il est également important de procéder de manière responsable.

Tout au long de ce cours, nous nous concentrons sur la construction de notre startup et de notre produit éducatif basé sur l'IA. Nous utiliserons les principes de l'IA Responsable : Équité, Inclusivité, Fiabilité/Sécurité, Sécurité & Confidentialité, Transparence et Responsabilité. Avec ces principes, nous explorerons comment ils se rapportent à notre utilisation de l'IA Générative dans nos produits.

## Pourquoi Prioriser l'IA Responsable

Lors de la création d'un produit, adopter une approche centrée sur l'humain en gardant à l'esprit l'intérêt de votre utilisateur conduit aux meilleurs résultats.

La particularité de l'IA Générative est son pouvoir de créer des réponses utiles, des informations, des conseils et du contenu pour les utilisateurs. Cela peut se faire sans de nombreuses étapes manuelles, ce qui peut conduire à des résultats très impressionnants. Sans planification et stratégies appropriées, cela peut malheureusement entraîner des résultats nuisibles pour vos utilisateurs, votre produit et la société dans son ensemble.

Examinons certains (mais pas tous) de ces résultats potentiellement nuisibles :

### Hallucinations

Les hallucinations sont un terme utilisé pour décrire lorsque un LLM produit un contenu qui est soit complètement insensé, soit quelque chose que nous savons être factuellement incorrect basé sur d'autres sources d'information.

Prenons par exemple le cas où nous développons une fonctionnalité pour notre startup qui permet aux étudiants de poser des questions historiques à un modèle. Un étudiant pose la question `Who was the sole survivor of Titanic?`

Le modèle produit une réponse telle que celle ci-dessous :

![Demande disant "Qui était le seul survivant du Titanic"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Source: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

C'est une réponse très confiante et détaillée. Malheureusement, elle est incorrecte. Même avec un minimum de recherche, on découvrirait qu'il y avait plus d'un survivant de la catastrophe du Titanic. Pour un étudiant qui commence juste à faire des recherches sur ce sujet, cette réponse peut être suffisamment persuasive pour ne pas être remise en question et traitée comme un fait. Les conséquences de cela peuvent conduire à ce que le système d'IA soit peu fiable et impacte négativement la réputation de notre startup.

Avec chaque itération d'un LLM donné, nous avons observé des améliorations de performance pour minimiser les hallucinations. Même avec cette amélioration, nous, en tant que développeurs d'applications et utilisateurs, devons rester conscients de ces limitations.

### Contenu Nuisible

Nous avons couvert dans la section précédente lorsque un LLM produit des réponses incorrectes ou insensées. Un autre risque dont nous devons être conscients est lorsque un modèle répond avec du contenu nuisible.

Le contenu nuisible peut être défini comme :

- Fournir des instructions ou encourager l'auto-mutilation ou le mal envers certains groupes.
- Contenu haineux ou dégradant.
- Orienter la planification de toute attaque ou acte violent.
- Fournir des instructions sur comment trouver du contenu illégal ou commettre des actes illégaux.
- Afficher du contenu sexuellement explicite.

Pour notre startup, nous voulons nous assurer que nous avons les bons outils et stratégies en place pour empêcher ce type de contenu d'être vu par les étudiants.

### Manque d'Équité

L'équité est définie comme "assurer qu'un système d'IA est exempt de biais et de discrimination et qu'il traite tout le monde de manière équitable et égale." Dans le monde de l'IA Générative, nous voulons nous assurer que les visions du monde exclusionnaires des groupes marginalisés ne sont pas renforcées par les résultats du modèle.

Ces types de résultats ne sont pas seulement destructeurs pour construire des expériences produits positives pour nos utilisateurs, mais ils causent également des dommages sociétaux supplémentaires. En tant que développeurs d'applications, nous devrions toujours garder à l'esprit une base d'utilisateurs large et diversifiée lors de la construction de solutions avec l'IA Générative.

## Comment Utiliser l'IA Générative de Manière Responsable

Maintenant que nous avons identifié l'importance de l'IA Générative Responsable, examinons 4 étapes que nous pouvons suivre pour construire nos solutions d'IA de manière responsable :

![Cycle de Mitigation](../../../translated_images/mitigate-cycle.png?WT.ffc987e1880649a302a311432b78f49faa64e46f65df6350c9c409b5ed79549b.fr.mc_id=academic-105485-koreyst)

### Mesurer les Dommages Potentiels

Dans les tests logiciels, nous testons les actions attendues d'un utilisateur sur une application. De la même manière, tester un ensemble diversifié de prompts que les utilisateurs sont le plus susceptibles d'utiliser est un bon moyen de mesurer les dommages potentiels.

Puisque notre startup développe un produit éducatif, il serait bon de préparer une liste de prompts liés à l'éducation. Cela pourrait être pour couvrir un certain sujet, des faits historiques, et des prompts sur la vie étudiante.

### Atténuer les Dommages Potentiels

Il est maintenant temps de trouver des moyens où nous pouvons prévenir ou limiter les dommages potentiels causés par le modèle et ses réponses. Nous pouvons examiner cela en 4 couches différentes :

![Couches de Mitigation](../../../translated_images/mitigation-layers.png?WT.cb109f48e143f1ff4dee760b4b0c9477c7d11c2fe57f3efdd89f68c1109f2de6.fr.mc_id=academic-105485-koreyst)

- **Modèle**. Choisir le bon modèle pour le bon cas d'utilisation. Des modèles plus grands et plus complexes comme GPT-4 peuvent causer plus de risques de contenu nuisible lorsqu'ils sont appliqués à des cas d'utilisation plus petits et plus spécifiques. Utiliser vos données d'entraînement pour affiner réduit également le risque de contenu nuisible.

- **Système de Sécurité**. Un système de sécurité est un ensemble d'outils et de configurations sur la plateforme servant le modèle qui aident à atténuer les dommages. Un exemple de ceci est le système de filtrage de contenu sur le service Azure OpenAI. Les systèmes devraient également détecter les attaques de jailbreak et les activités indésirables comme les requêtes de bots.

- **Métaprompt**. Les métaprompts et l'ancrage sont des moyens de diriger ou de limiter le modèle basé sur certains comportements et informations. Cela pourrait être l'utilisation d'entrées système pour définir certaines limites du modèle. De plus, fournir des résultats plus pertinents pour le domaine ou le champ d'application du système.

Cela peut également être l'utilisation de techniques comme la Génération Augmentée par Récupération (RAG) pour que le modèle ne tire des informations que d'une sélection de sources fiables. Il y a une leçon plus tard dans ce cours pour [construire des applications de recherche](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Expérience Utilisateur**. La couche finale est celle où l'utilisateur interagit directement avec le modèle via l'interface de notre application d'une certaine manière. De cette façon, nous pouvons concevoir l'UI/UX pour limiter l'utilisateur sur les types d'entrées qu'ils peuvent envoyer au modèle ainsi que le texte ou les images affichés à l'utilisateur. Lors du déploiement de l'application d'IA, nous devons également être transparents sur ce que notre application d'IA Générative peut et ne peut pas faire.

Nous avons une leçon entière dédiée à [Concevoir l'UX pour les Applications d'IA](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Évaluer le modèle**. Travailler avec des LLMs peut être difficile car nous n'avons pas toujours le contrôle sur les données sur lesquelles le modèle a été formé. Néanmoins, nous devrions toujours évaluer les performances et les résultats du modèle. Il est toujours important de mesurer la précision du modèle, la similarité, l'ancrage et la pertinence du résultat. Cela aide à fournir transparence et confiance aux parties prenantes et aux utilisateurs.

### Opérer une Solution d'IA Générative Responsable

Construire une pratique opérationnelle autour de vos applications d'IA est la dernière étape. Cela inclut de s'associer avec d'autres parties de notre startup comme le service juridique et la sécurité pour s'assurer que nous sommes conformes à toutes les politiques réglementaires. Avant le lancement, nous voulons également élaborer des plans autour de la livraison, de la gestion des incidents et du retour en arrière pour prévenir tout dommage à nos utilisateurs à mesure que nous grandissons.

## Outils

Bien que le travail de développement de solutions d'IA Responsable puisse sembler important, c'est un travail qui en vaut la peine. À mesure que le domaine de l'IA Générative se développe, plus d'outils pour aider les développeurs à intégrer efficacement la responsabilité dans leurs flux de travail mûriront. Par exemple, le [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) peut aider à détecter le contenu et les images nuisibles via une requête API.

## Vérification des Connaissances

Quels sont certains des aspects dont vous devez vous soucier pour garantir une utilisation responsable de l'IA ?

1. Que la réponse soit correcte.
2. Usage nuisible, que l'IA ne soit pas utilisée à des fins criminelles.
3. S'assurer que l'IA est exempte de biais et de discrimination.

R : 2 et 3 sont corrects. L'IA Responsable vous aide à réfléchir à la manière d'atténuer les effets nuisibles et les biais et plus encore.

## 🚀 Défi

Informez-vous sur [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) et voyez ce que vous pouvez adopter pour votre usage.

## Excellent Travail, Continuez Votre Apprentissage

Après avoir complété cette leçon, consultez notre [collection d'apprentissage sur l'IA Générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances sur l'IA Générative !

Rendez-vous à la Leçon 4 où nous examinerons les [Fondamentaux de l'Ingénierie des Prompts](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) !

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisés par IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.