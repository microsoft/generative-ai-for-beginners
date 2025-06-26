<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-06-25T20:08:16+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "fr"
}
-->
# Concevoir l'expérience utilisateur pour les applications d'IA

[![Concevoir l'expérience utilisateur pour les applications d'IA](../../../translated_images/12-lesson-banner.c53c3c7c802e8f563953ce388f6a987ca493472c724d924b060be470951c53c8.fr.png)](https://aka.ms/gen-ai-lesson12-gh?WT.mc_id=academic-105485-koreyst)

> _(Cliquez sur l'image ci-dessus pour visionner la vidéo de cette leçon)_

L'expérience utilisateur est un aspect très important de la création d'applications. Les utilisateurs doivent pouvoir utiliser votre application de manière efficace pour accomplir des tâches. Être efficace est une chose, mais il faut aussi concevoir des applications qui peuvent être utilisées par tout le monde, pour les rendre _accessibles_. Ce chapitre se concentrera sur cet aspect afin que vous puissiez concevoir une application que les gens peuvent et veulent utiliser.

## Introduction

L'expérience utilisateur est la manière dont un utilisateur interagit avec et utilise un produit ou un service spécifique, qu'il s'agisse d'un système, d'un outil ou d'un design. Lors du développement d'applications d'IA, les développeurs se concentrent non seulement sur l'efficacité de l'expérience utilisateur mais aussi sur son aspect éthique. Dans cette leçon, nous abordons comment créer des applications d'intelligence artificielle (IA) qui répondent aux besoins des utilisateurs.

La leçon couvrira les domaines suivants :

- Introduction à l'expérience utilisateur et compréhension des besoins des utilisateurs
- Concevoir des applications d'IA pour la confiance et la transparence
- Concevoir des applications d'IA pour la collaboration et le retour d'information

## Objectifs d'apprentissage

Après avoir suivi cette leçon, vous serez capable de :

- Comprendre comment créer des applications d'IA qui répondent aux besoins des utilisateurs.
- Concevoir des applications d'IA qui favorisent la confiance et la collaboration.

### Prérequis

Prenez le temps de lire davantage sur [l'expérience utilisateur et la pensée design.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introduction à l'expérience utilisateur et compréhension des besoins des utilisateurs

Dans notre startup éducative fictive, nous avons deux utilisateurs principaux, les enseignants et les étudiants. Chacun des deux utilisateurs a des besoins uniques. Un design centré sur l'utilisateur donne la priorité à l'utilisateur en s'assurant que les produits sont pertinents et bénéfiques pour ceux auxquels ils sont destinés.

L'application doit être **utile, fiable, accessible et agréable** pour offrir une bonne expérience utilisateur.

### Utilité

Être utile signifie que l'application a des fonctionnalités qui correspondent à son objectif, comme automatiser le processus de notation ou générer des cartes mémoire pour la révision. Une application qui automatise le processus de notation doit être capable d'attribuer des notes avec précision et efficacité au travail des étudiants en fonction de critères prédéfinis. De même, une application qui génère des cartes mémoire de révision doit pouvoir créer des questions pertinentes et diversifiées à partir de ses données.

### Fiabilité

Être fiable signifie que l'application peut accomplir sa tâche de manière cohérente et sans erreurs. Cependant, l'IA, tout comme les humains, n'est pas parfaite et peut être sujette à des erreurs. Les applications peuvent rencontrer des erreurs ou des situations inattendues nécessitant une intervention ou une correction humaine. Comment gérez-vous les erreurs ? Dans la dernière section de cette leçon, nous aborderons comment les systèmes et applications d'IA sont conçus pour la collaboration et le retour d'information.

### Accessibilité

Être accessible signifie étendre l'expérience utilisateur à des utilisateurs ayant diverses capacités, y compris ceux ayant des handicaps, afin de s'assurer que personne n'est laissé de côté. En suivant les directives et principes d'accessibilité, les solutions d'IA deviennent plus inclusives, utilisables et bénéfiques pour tous les utilisateurs.

### Agréable

Être agréable signifie que l'application est plaisante à utiliser. Une expérience utilisateur attrayante peut avoir un impact positif sur l'utilisateur, l'encourageant à revenir à l'application et augmentant ainsi les revenus de l'entreprise.

![image illustrant les considérations UX dans l'IA](../../../translated_images/uxinai.d5b4ed690f5cefff0c53ffcc01b480cdc1828402e1fdbc980490013a3c50935a.fr.png)

Tous les défis ne peuvent pas être résolus avec l'IA. L'IA vient améliorer votre expérience utilisateur, que ce soit en automatisant des tâches manuelles ou en personnalisant les expériences utilisateur.

## Concevoir des applications d'IA pour la confiance et la transparence

Construire la confiance est essentiel lors de la conception d'applications d'IA. La confiance assure à l'utilisateur que l'application accomplira le travail, fournira des résultats de manière cohérente et que les résultats correspondent à ses besoins. Un risque dans ce domaine est la méfiance et la confiance excessive. La méfiance se produit lorsqu'un utilisateur a peu ou pas de confiance dans un système d'IA, ce qui conduit l'utilisateur à rejeter votre application. La confiance excessive se produit lorsqu'un utilisateur surestime la capacité d'un système d'IA, ce qui amène les utilisateurs à trop faire confiance au système d'IA. Par exemple, un système de notation automatisé en cas de confiance excessive pourrait amener l'enseignant à ne pas vérifier certains des devoirs pour s'assurer que le système de notation fonctionne bien. Cela pourrait entraîner des notes injustes ou inexactes pour les étudiants, ou des occasions manquées de retour d'information et d'amélioration.

Deux façons de s'assurer que la confiance est placée au centre de la conception sont l'explicabilité et le contrôle.

### Explicabilité

Lorsque l'IA aide à informer des décisions telles que transmettre des connaissances aux générations futures, il est essentiel que les enseignants et les parents comprennent comment les décisions de l'IA sont prises. C'est l'explicabilité - comprendre comment les applications d'IA prennent des décisions. Concevoir pour l'explicabilité inclut d'ajouter des détails d'exemples de ce qu'une application d'IA peut faire. Par exemple, au lieu de "Commencez avec l'enseignant IA", le système peut utiliser : "Résumez vos notes pour une révision plus facile grâce à l'IA."

![une page d'accueil d'application avec une illustration claire de l'explicabilité dans les applications d'IA](../../../translated_images/explanability-in-ai.134426a96b498fbfdc80c75ae0090aedc0fc97424ae0734fccf7fb00a59a20d9.fr.png)

Un autre exemple est la façon dont l'IA utilise les données utilisateur et personnelles. Par exemple, un utilisateur avec le persona étudiant peut avoir des limitations basées sur son persona. L'IA peut ne pas être en mesure de révéler les réponses aux questions mais peut aider à guider l'utilisateur à réfléchir à comment résoudre un problème.

![L'IA répondant aux questions en fonction du persona](../../../translated_images/solving-questions.b7dea1604de0cbd2e9c5fa00b1a68a0ed77178a035b94b9213196b9d125d0be8.fr.png)

Une dernière partie clé de l'explicabilité est la simplification des explications. Les étudiants et les enseignants peuvent ne pas être des experts en IA, par conséquent, les explications de ce que l'application peut ou ne peut pas faire devraient être simplifiées et faciles à comprendre.

![explications simplifiées sur les capacités de l'IA](../../../translated_images/simplified-explanations.4679508a406c3621fa22bad4673e717fbff02f8b8d58afcab8cb6f1aa893a82f.fr.png)

### Contrôle

L'IA générative crée une collaboration entre l'IA et l'utilisateur, où par exemple un utilisateur peut modifier les invites pour obtenir différents résultats. De plus, une fois qu'un résultat est généré, les utilisateurs devraient pouvoir modifier les résultats leur donnant un sentiment de contrôle. Par exemple, lors de l'utilisation de Bing, vous pouvez adapter votre invite en fonction du format, du ton et de la longueur. De plus, vous pouvez apporter des modifications à votre résultat et modifier le résultat comme indiqué ci-dessous :

![Résultats de recherche Bing avec options pour modifier l'invite et le résultat](../../../translated_images/bing1.293ae8527dbe2789b675c8591c9fb3cb1aa2ada75c2877f9aa9edc059f7a8b1c.fr.png)

Une autre fonctionnalité dans Bing qui permet à un utilisateur de contrôler l'application est la capacité de choisir d'activer ou de désactiver les données utilisées par l'IA. Pour une application scolaire, un étudiant pourrait vouloir utiliser ses notes ainsi que les ressources des enseignants comme matériel de révision.

![Résultats de recherche Bing avec options pour modifier l'invite et le résultat](../../../translated_images/bing2.309f4845528a88c28c1c9739fb61d91fd993dc35ebe6fc92c66791fb04fceb4d.fr.png)

> Lors de la conception d'applications d'IA, l'intentionnalité est essentielle pour s'assurer que les utilisateurs ne font pas une confiance excessive, créant des attentes irréalistes quant à ses capacités. Une façon de le faire est de créer une friction entre les invites et les résultats. Rappeler à l'utilisateur que c'est de l'IA et non un être humain

## Concevoir des applications d'IA pour la collaboration et le retour d'information

Comme mentionné précédemment, l'IA générative crée une collaboration entre l'utilisateur et l'IA. La plupart des interactions se font avec un utilisateur saisissant une invite et l'IA générant un résultat. Que faire si le résultat est incorrect ? Comment l'application gère-t-elle les erreurs si elles se produisent ? L'IA blâme-t-elle l'utilisateur ou prend-elle le temps d'expliquer l'erreur ?

Les applications d'IA devraient être conçues pour recevoir et donner des retours d'information. Cela aide non seulement le système d'IA à s'améliorer, mais renforce également la confiance des utilisateurs. Une boucle de rétroaction devrait être incluse dans la conception, un exemple peut être un simple pouce levé ou baissé sur le résultat.

Une autre façon de gérer cela est de communiquer clairement les capacités et les limites du système. Lorsqu'un utilisateur commet une erreur en demandant quelque chose au-delà des capacités de l'IA, il devrait également y avoir un moyen de gérer cela, comme indiqué ci-dessous.

![Donner un retour d'information et gérer les erreurs](../../../translated_images/feedback-loops.7955c134429a94663443ad74d59044f8dc4ce354577f5b79b4bd2533f2cafc6f.fr.png)

Les erreurs système sont courantes avec les applications où l'utilisateur pourrait avoir besoin d'aide avec des informations en dehors du champ d'application de l'IA ou l'application peut avoir une limite sur le nombre de questions/sujets qu'un utilisateur peut générer des résumés. Par exemple, une application d'IA formée avec des données sur des sujets limités, par exemple, l'Histoire et les Mathématiques, peut ne pas être en mesure de gérer des questions autour de la Géographie. Pour atténuer cela, le système d'IA peut donner une réponse comme : "Désolé, notre produit a été formé avec des données dans les sujets suivants....., je ne peux pas répondre à la question que vous avez posée."

Les applications d'IA ne sont pas parfaites, elles sont donc susceptibles de faire des erreurs. Lors de la conception de vos applications, vous devriez vous assurer de créer de l'espace pour le retour d'information des utilisateurs et la gestion des erreurs d'une manière simple et facilement explicable.

## Devoir

Prenez toutes les applications d'IA que vous avez créées jusqu'à présent, envisagez de mettre en œuvre les étapes ci-dessous dans votre application :

- **Agréable :** Réfléchissez à la façon dont vous pouvez rendre votre application plus agréable. Ajoutez-vous des explications partout ? Encouragez-vous l'utilisateur à explorer ? Comment formulez-vous vos messages d'erreur ?

- **Utilité :** Construire une application web. Assurez-vous que votre application est navigable à la fois par la souris et le clavier.

- **Confiance et transparence :** Ne faites pas totalement confiance à l'IA et à ses résultats, réfléchissez à la façon dont vous ajouteriez un humain au processus pour vérifier les résultats. Envisagez également d'autres moyens d'atteindre la confiance et la transparence.

- **Contrôle :** Donnez à l'utilisateur le contrôle des données qu'il fournit à l'application. Mettez en œuvre un moyen pour un utilisateur de choisir d'activer ou de désactiver la collecte de données dans l'application d'IA.

## Continuez votre apprentissage !

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à améliorer vos connaissances en IA générative !

Rendez-vous à la leçon 13, où nous verrons comment [sécuriser les applications d'IA](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) !

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue maternelle doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.