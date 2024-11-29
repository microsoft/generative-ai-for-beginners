# Concevoir l'expérience utilisateur pour les applications d'IA

[![Concevoir l'expérience utilisateur pour les applications d'IA](../../../translated_images/12-lesson-banner.png?WT.998ee992c9acfb5c1b2802fb3817b9a1a704886f30157b28dff34cd9c2ee598b.fr.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson12-gh?WT.mc_id=academic-105485-koreyst)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

L'expérience utilisateur est un aspect très important dans la création d'applications. Les utilisateurs doivent pouvoir utiliser votre application de manière efficace pour réaliser des tâches. Être efficace est une chose, mais il faut aussi concevoir des applications pour qu'elles soient utilisables par tout le monde, afin de les rendre _accessibles_. Ce chapitre se concentrera sur cet aspect afin que vous puissiez concevoir une application que les gens peuvent et veulent utiliser.

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

Prenez le temps de lire davantage sur [l'expérience utilisateur et le design thinking.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introduction à l'expérience utilisateur et compréhension des besoins des utilisateurs

Dans notre startup fictive dans le domaine de l'éducation, nous avons deux utilisateurs principaux, les enseignants et les étudiants. Chacun de ces utilisateurs a des besoins uniques. Un design centré sur l'utilisateur priorise l'utilisateur en s'assurant que les produits sont pertinents et bénéfiques pour ceux auxquels ils sont destinés.

L'application doit être **utile, fiable, accessible et agréable** pour offrir une bonne expérience utilisateur.

### Utilité

Être utile signifie que l'application a des fonctionnalités qui correspondent à son objectif prévu, comme automatiser le processus de notation ou générer des fiches de révision. Une application qui automatise le processus de notation doit être capable d'attribuer des notes aux travaux des étudiants de manière précise et efficace en fonction de critères prédéfinis. De même, une application qui génère des fiches de révision doit être capable de créer des questions pertinentes et variées en fonction de ses données.

### Fiabilité

Être fiable signifie que l'application peut accomplir sa tâche de manière cohérente et sans erreurs. Cependant, l'IA, tout comme les humains, n'est pas parfaite et peut être sujette à des erreurs. Les applications peuvent rencontrer des erreurs ou des situations inattendues qui nécessitent une intervention ou une correction humaine. Comment gérez-vous les erreurs ? Dans la dernière section de cette leçon, nous aborderons comment les systèmes et applications d'IA sont conçus pour la collaboration et le retour d'information.

### Accessibilité

Être accessible signifie étendre l'expérience utilisateur à des utilisateurs ayant diverses capacités, y compris ceux ayant des handicaps, en s'assurant que personne n'est laissé de côté. En suivant les directives et principes d'accessibilité, les solutions d'IA deviennent plus inclusives, utilisables et bénéfiques pour tous les utilisateurs.

### Agréable

Être agréable signifie que l'application est plaisante à utiliser. Une expérience utilisateur attrayante peut avoir un impact positif sur l'utilisateur, l'encourageant à revenir à l'application et augmentant les revenus de l'entreprise.

![image illustrant les considérations UX dans l'IA](../../../translated_images/uxinai.png?WT.00d77ed86b53127e3860f8ee713e684370fe08c450c8a1e496beb82e96c59355.fr.mc_id=academic-105485-koreyst)

Tous les défis ne peuvent pas être résolus avec l'IA. L'IA intervient pour améliorer votre expérience utilisateur, qu'il s'agisse d'automatiser des tâches manuelles ou de personnaliser les expériences utilisateur.

## Concevoir des applications d'IA pour la confiance et la transparence

Établir la confiance est essentiel lors de la conception d'applications d'IA. La confiance assure qu'un utilisateur est confiant que l'application accomplira le travail, livrera des résultats de manière cohérente et que les résultats sont ce dont l'utilisateur a besoin. Un risque dans ce domaine est la méfiance et la surconfiance. La méfiance se produit lorsqu'un utilisateur a peu ou pas de confiance dans un système d'IA, ce qui conduit l'utilisateur à rejeter votre application. La surconfiance se produit lorsqu'un utilisateur surestime la capacité d'un système d'IA, conduisant les utilisateurs à trop faire confiance au système d'IA. Par exemple, un système de notation automatisé en cas de surconfiance pourrait amener l'enseignant à ne pas vérifier certains des travaux pour s'assurer que le système de notation fonctionne bien. Cela pourrait entraîner des notes injustes ou inexactes pour les étudiants, ou des occasions manquées pour des retours d'information et des améliorations.

Deux moyens d'assurer que la confiance est placée au centre du design sont l'explicabilité et le contrôle.

### Explicabilité

Lorsque l'IA aide à informer des décisions telles que transmettre des connaissances aux générations futures, il est essentiel que les enseignants et les parents comprennent comment les décisions de l'IA sont prises. C'est l'explicabilité - comprendre comment les applications d'IA prennent des décisions. Concevoir pour l'explicabilité inclut d'ajouter des détails et des exemples de ce qu'une application d'IA peut faire. Par exemple, au lieu de "Commencer avec l'enseignant IA", le système peut utiliser : "Résumez vos notes pour une révision plus facile grâce à l'IA."

![une page d'accueil d'application avec une illustration claire de l'explicabilité dans les applications d'IA](../../../translated_images/explanability-in-ai.png?WT.e66323dd42a976cd7fb15d79304f70a3d625eac6607ec395311a772915a45ffa.fr.mc_id=academic-105485-koreyst)

Un autre exemple est la façon dont l'IA utilise les données utilisateur et personnelles. Par exemple, un utilisateur avec la persona étudiant peut avoir des limitations basées sur leur persona. L'IA peut ne pas être en mesure de révéler les réponses aux questions mais peut aider à guider l'utilisateur à réfléchir à la façon dont ils peuvent résoudre un problème.

![L'IA répondant à des questions basées sur la persona](../../../translated_images/solving-questions.png?WT.f7c41f8c20cb98ec5d456d1e14e7fee2b11b7adc77c23421645a82495b51208d.fr.mc_id=academic-105485-koreyst)

Une dernière partie clé de l'explicabilité est la simplification des explications. Les étudiants et les enseignants peuvent ne pas être des experts en IA, donc les explications de ce que l'application peut ou ne peut pas faire devraient être simplifiées et faciles à comprendre.

![explications simplifiées sur les capacités de l'IA](../../../translated_images/simplified-explanations.png?WT.58904786757a91a1365e98cac5f9088bb16c9241e312463921a9a1733a85adc0.fr.mc_id=academic-105485-koreyst)

### Contrôle

L'IA générative crée une collaboration entre l'IA et l'utilisateur, où par exemple un utilisateur peut modifier des invites pour différents résultats. De plus, une fois qu'un résultat est généré, les utilisateurs devraient pouvoir modifier les résultats leur donnant un sentiment de contrôle. Par exemple, lors de l'utilisation de Bing, vous pouvez adapter votre invite en fonction du format, du ton et de la longueur. De plus, vous pouvez ajouter des modifications à votre résultat et le modifier comme illustré ci-dessous :

![Résultats de recherche Bing avec des options pour modifier l'invite et le résultat](../../../translated_images/bing1.png?WT.02e610458eee0b4aa9ea52956d1077ed067d030d214834cd654aa21764980e03.fr.mc_id=academic-105485-koreyst "résultats de recherche bing avec des options pour modifier l'invite et le résultat")

Une autre fonctionnalité dans Bing qui permet à un utilisateur de contrôler l'application est la possibilité de choisir de participer ou non aux données utilisées par l'IA. Pour une application scolaire, un étudiant pourrait vouloir utiliser ses notes ainsi que les ressources des enseignants comme matériel de révision.

![Résultats de recherche Bing avec des options pour modifier l'invite et le résultat](../../../translated_images/bing2.png?WT.ef2560baaf643e77c593b7c036c42c5a787a46f2cd3c2b4118d06349973c79f1.fr.mc_id=academic-105485-koreyst "résultats de recherche bing avec des options pour modifier l'invite et le résultat")

> Lors de la conception d'applications d'IA, l'intentionnalité est essentielle pour s'assurer que les utilisateurs ne font pas une confiance excessive en fixant des attentes irréalistes quant à ses capacités. Une façon de faire cela est de créer une friction entre les invites et les résultats. Rappelant à l'utilisateur que c'est de l'IA et non un être humain

## Concevoir des applications d'IA pour la collaboration et le retour d'information

Comme mentionné précédemment, l'IA générative crée une collaboration entre l'utilisateur et l'IA. La plupart des interactions consistent en un utilisateur saisissant une invite et l'IA générant un résultat. Que se passe-t-il si le résultat est incorrect ? Comment l'application gère-t-elle les erreurs si elles se produisent ? L'IA blâme-t-elle l'utilisateur ou prend-elle le temps d'expliquer l'erreur ?

Les applications d'IA devraient être conçues pour recevoir et donner des retours d'information. Cela aide non seulement le système d'IA à s'améliorer mais aussi à instaurer la confiance avec les utilisateurs. Une boucle de rétroaction devrait être incluse dans le design, un exemple peut être un simple pouce levé ou baissé sur le résultat.

Une autre façon de gérer cela est de communiquer clairement les capacités et les limitations du système. Lorsqu'un utilisateur fait une erreur en demandant quelque chose au-delà des capacités de l'IA, il devrait également y avoir un moyen de gérer cela, comme illustré ci-dessous.

![Donner un retour d'information et gérer les erreurs](../../../translated_images/feedback-loops.png?WT.ee4d8df7b207adf073487e9a9617e4f901a404fc4b826152a56435fb5bd32705.fr.mc_id=academic-105485-koreyst)

Les erreurs système sont courantes avec les applications où l'utilisateur pourrait avoir besoin d'aide avec des informations en dehors du champ d'application de l'IA ou l'application peut avoir une limite du nombre de questions/sujets qu'un utilisateur peut générer des résumés. Par exemple, une application d'IA formée avec des données sur des sujets limités, par exemple, Histoire et Mathématiques, pourrait ne pas être capable de gérer des questions sur la Géographie. Pour atténuer cela, le système d'IA peut donner une réponse comme : "Désolé, notre produit a été formé avec des données dans les sujets suivants....., je ne peux pas répondre à la question que vous avez posée."

Les applications d'IA ne sont pas parfaites, par conséquent, elles sont susceptibles de faire des erreurs. Lors de la conception de vos applications, vous devriez vous assurer de créer un espace pour le retour d'information des utilisateurs et la gestion des erreurs d'une manière simple et facilement explicable.

## Devoir

Prenez toutes les applications d'IA que vous avez construites jusqu'à présent, envisagez de mettre en œuvre les étapes ci-dessous dans votre application :

- **Agréable :** Réfléchissez à la façon dont vous pouvez rendre votre application plus agréable. Ajoutez-vous des explications partout, encouragez-vous l'utilisateur à explorer ? Comment formulez-vous vos messages d'erreur ?

- **Utilité :** Construisez une application web. Assurez-vous que votre application est navigable à la fois par la souris et le clavier.

- **Confiance et transparence :** Ne faites pas entièrement confiance à l'IA et à ses résultats, réfléchissez à la manière dont vous ajouteriez un humain au processus pour vérifier le résultat. Envisagez également et mettez en œuvre d'autres moyens d'atteindre la confiance et la transparence.

- **Contrôle :** Donnez à l'utilisateur le contrôle des données qu'il fournit à l'application. Mettez en œuvre une façon pour l'utilisateur de choisir de participer ou non à la collecte de données dans l'application d'IA.

## Poursuivez votre apprentissage !

Après avoir terminé cette leçon, consultez notre [collection d'apprentissage sur l'IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à développer vos connaissances en IA générative !

Passez à la leçon 13 où nous verrons comment [sécuriser les applications d'IA](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) !

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.